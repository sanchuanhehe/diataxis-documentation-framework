#!/usr/bin/env python3
"""跨文件术语一致性检查.

对 STYLE.md §1 的关键术语，检查「英文原文出现该词时，中文译文是否用了规定的译法」，
并报告同一英文词在不同条目里出现的多种译法，供人工裁决。

用法:
    python3 tools/check-terms.py            # 报告问题
    python3 tools/check-terms.py --variants # 列出每个术语实际用到的所有译法
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib.machinery import SourceFileLoader

_pairs = SourceFileLoader("dump_pairs", os.path.join(os.path.dirname(os.path.abspath(__file__)), "dump-pairs.py")).load_module()
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PO_DIR = os.path.join(ROOT, "translation", "zh_CN", "LC_MESSAGES")

LITERAL_RE = re.compile(r"``.+?``", re.S)
ROLE_RE = re.compile(r":([a-z_]+):`([^`]*)`")


def visible(text: str) -> str:
    """只保留读者可见的英文正文（剔除字面量与角色目标）。"""

    def role(match: re.Match[str]) -> str:
        body = match.group(2)
        # 没有显式 <target> 的角色由 Sphinx 用文档标题填充，检查阶段不可见
        if not re.search(r"<[^<>]+>\s*$", body.strip()):
            return " "
        return re.sub(r"\s*<[^<>]+>\s*$", " ", body)

    return ROLE_RE.sub(role, LITERAL_RE.sub(" ", text))


# 英文术语 -> (正则, 可接受的中文写法, 说明)
TERMS: list[tuple[str, str, tuple[str, ...], str]] = [
    ("tutorial", r"\btutorials?\b", ("教程",), "Tutorials 应译「教程」"),
    ("how-to guide", r"\bhow-to guides?\b", ("实践指南",), "How-to guides 应译「实践指南」"),
    ("reference", r"\breferences?\b", ("参考",), "Reference 应译「参考资料／参考指南」"),
    ("explanation", r"\bexplanations?\b", ("解释",), "Explanation 应译「解释说明」"),
    ("action", r"\baction\b", ("行动",), "action 应译「行动」"),
    ("cognition", r"\bcognition\b", ("认知",), "cognition 应译「认知」"),
    ("acquisition", r"\bacquisition\b", ("习得",), "acquisition 应译「习得」"),
    ("application", r"\bapplication\b", ("应用",), "application 应译「应用」"),
    ("craft", r"\bcraft\b", ("技艺",), "craft 应译「技艺」"),
    ("practitioner", r"\bpractitioners?\b", ("实践者",), "practitioner 应译「实践者」"),
    ("flow", r"\bflow\b", ("流畅",), "flow 应译「流畅感／流畅」"),
    ("reflection", r"\breflection\b", ("反思",), "reflection 应译「反思」"),
    # 名词用法统一作「相遇」（已确认保留的术语）；动词用法可用「接触／遇到／遇上」
    ("encounter", r"\bencounters?\b", ("相遇", "接触", "遇到", "遇上"), "encounter 作名词时统一用「相遇」"),
    ("heuristic", r"\bheuristic\b", ("启发式",), "heuristic 应译「启发式」"),
    ("machinery", r"\bmachinery\b", ("系统", "构造"), "machinery 统一译「系统」；「internal machinery」可作「内部构造」。不用「机制／设备／机器」"),
    ("deep quality", r"\bdeep quality\b", ("深层质量", "深层品质"), "deep quality 全文须统一"),
    ("functional quality", r"\bfunctional quality\b", ("功能质量", "功能品质"), "functional quality 全文须统一"),
    ("compass", r"\bcompass\b", ("指南针",), "compass 应译「指南针」"),
    ("propositional", r"\bpropositional\b", ("命题性",), "propositional 应译「命题性」"),
    ("austere", r"\baustere\b", ("严谨", "克制"), "austere 宜译「严谨克制」"),
]


# 英文把框架术语标成粗体时，中文必须给出「单字（完整词）」的注解形式。
# 这是中文版的核心本地化设计，与 source/images/zh_CN/*.svg 绑定，不得拆改。
# 值是可接受的形式：独立术语用「单字（完整词）」，句中成分用「完整词（单字）」
FRAMEWORK = [
    ("**action**", ("行（行动）",)),
    ("**cognition**", ("知（认知）",)),
    ("**acquired**", ("学（习得）", "习得（学）")),
    ("**applied**", ("用（应用）", "应用（用）")),
    ("**acquisition**", ("学（习得）", "习得（学）")),
    ("**application**", ("用（应用）", "应用（用）")),
    ("**study**", ("学",)),
    ("**work**", ("用",)),
]


# 这些 msgid 是坐标轴标题，按 §1.2 规则 2 固定译作「知与行」「学与用」，
# 不适用下面的单词级术语匹配。
AXIS_HEADINGS = {"Action/cognition", "Acquisition/application", "Two dimensions of craft"}

# 这里的 flow 是「水流」，不是框架术语「流畅感」
SKIP_MSGIDS = {'"To shut off the flow of water, turn the tap clockwise."'}


# 这些写法与主译法并存，但不算「不统一」（语境确实不同）
NON_COMPETING: dict[str, set[str]] = {
    "machinery": {"构造"},   # 「the product and its internal machinery」→「产品及其内部构造」
    # encounter 的动词用法（have an encounter with / encounter the kinds of...）
    # 用「接触／遇到／遇上」是自然的，不算与名词术语「相遇」冲突
    "encounter": {"接触", "遇到", "遇上"},
}

# 「单字（完整词）」只允许出现在「独立术语」位置。若它紧贴在一个汉字之后，
# 说明单字被硬塞进了句子里（如「指导行（行动）」「用户的学（习得）」），
# 汉语读不通——此时应改用「完整词（单字）」。见 STYLE.md §1.2。
AXIS_FIRST = re.compile(r"[知行学用]（(?:行动|认知|习得|应用)）")
HANZI = re.compile(r"[\u4e00-\u9fff]")

# 这些是连接词，其后的框架术语仍是「独立术语」，不算被塞进句子
CONJUNCTIONS = {"还是", "或者", "以及", "或是", "乃至", "抑或", "或", "和", "与", "及"}

# 结构助词与语气词，跟在框架术语之后不算「粘成生造词」
PARTICLES = set("的地得了着吗呢吧之")


def main() -> int:
    parser = argparse.ArgumentParser(description="跨文件术语一致性检查")
    parser.add_argument("names", nargs="*", help="只检查这些资源名（默认全部）")
    parser.add_argument("--variants", action="store_true", help="列出每个术语实际用到的所有译法")
    args = parser.parse_args()

    names = args.names or sorted(
        os.path.basename(p)[:-3] for p in glob.glob(os.path.join(PO_DIR, "*.po"))
    )
    entries: list[tuple[str, int, str, str]] = []
    for name in names:
        for index, (msgid, msgstr) in enumerate(_pairs.load(name), 1):
            entries.append((name, index, msgid, msgstr))

    issues: list[str] = []

    # 0. 框架术语「知／行／学／用」注解形式（与中文图示绑定，强制）
    framework_missing: list[str] = []
    for name, index, msgid, msgstr in entries:
        for english, accepted in FRAMEWORK:
            if english in msgid and not any(form in msgstr for form in accepted):
                framework_missing.append(
                    f"{name}#{index}: 英文 {english} 应作「{'／'.join(accepted)}」，实为 → {msgstr[:70]}"
                )
    # 0b. 「单字（完整词）」不得紧贴汉字（会被读成生造词）
    axis_glued: list[str] = []
    for name, index, msgid, msgstr in entries:
        for m in AXIS_FIRST.finditer(msgstr):
            before = msgstr[m.start() - 1] if m.start() > 0 else ""
            prev1 = msgstr[m.start() - 1 : m.start()]
            prev2 = msgstr[m.start() - 2 : m.start()]
            glued = (
                before
                and HANZI.match(before)
                and prev1 not in CONJUNCTIONS
                and prev2 not in CONJUNCTIONS
                and prev1 not in PARTICLES
            )
            # 右侧：跳过标记后若是汉字（非助词），说明单字在做动词或定语，粘到了后面的名词上
            after_idx = m.end()
            while after_idx < len(msgstr) and msgstr[after_idx] in "*`":
                after_idx += 1
            after = msgstr[after_idx] if after_idx < len(msgstr) else ""
            # 右侧紧接的若是连接词，术语仍是「独立术语」
            tail = ""
            probe = after_idx
            while probe < len(msgstr) and msgstr[probe] in "*`":
                probe += 1
            tail = msgstr[probe : probe + 2]
            if (
                after
                and HANZI.match(after)
                and after not in PARTICLES
                and tail not in CONJUNCTIONS
                and tail[:1] not in CONJUNCTIONS
            ):
                glued = True
            if glued:
                axis_glued.append(
                    f"{name}#{index}: 「{m.group(0)}」与汉字粘成生造词，"
                    f"应改用「完整词（单字）」→ …{msgstr[max(0, m.start() - 18):m.end() + 10]}…"
                )
    if axis_glued:
        issues.append(
            f"[知/行/学/用 注解位置] {len(axis_glued)} 处单字被塞进句子（STYLE §1.2）:\n      "
            + "\n      ".join(axis_glued[:12])
            + ("\n      …" if len(axis_glued) > 12 else "")
        )

    if framework_missing:
        issues.append(
            f"[知/行/学/用 框架术语] {len(framework_missing)} 条未按 §1.2 处理:\n      "
            + "\n      ".join(framework_missing[:14])
            + ("\n      …" if len(framework_missing) > 14 else "")
        )

    for label, pattern, expected_forms, note in TERMS:
        regex = re.compile(pattern, re.I)
        expected = expected_forms[0]
        usage: dict[str, int] = defaultdict(int)
        missing: list[str] = []
        for name, index, msgid, msgstr in entries:
            if msgid.strip() in AXIS_HEADINGS or msgid.strip() in SKIP_MSGIDS:
                continue
            src = visible(msgid)
            if not regex.search(src):
                continue
            hit = next((form for form in expected_forms if form in msgstr), None)
            if hit:
                usage[hit] += 1
            else:
                missing.append(f"{name}#{index}")
        competing = {k: v for k, v in usage.items() if k not in NON_COMPETING.get(label, set())}
        if len(competing) > 1:
            issues.append(
                f"[{label}] 同一术语出现多种译法 {competing}，须统一（{note}）"
            )
        if missing:
            issues.append(
                f"[{label}] {len(missing)} 条未使用「{'／'.join(expected_forms)}」（{note}）: "
                + ", ".join(missing[:10])
                + (" …" if len(missing) > 10 else "")
            )

        if args.variants:
            print(f"\n### {label} -> 「{'／'.join(expected_forms)}」")
            for name, index, msgid, msgstr in entries:
                if regex.search(visible(msgid)):
                    print(f"  [{name}#{index}] EN: {visible(msgid)[:70]}")
                    print(f"        ZH: {msgstr[:90]}")

    if issues:
        print(f"\n=== {len(issues)} 类术语问题 ===")
        for issue in issues:
            print("  " + issue)
        return 1
    print("✅ 术语一致性检查通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
