#!/usr/bin/env python3
"""Diátaxis 简体中文 .po 校验器.

用法:
    python3 tools/check-po.py                       # 校验全部 zh_CN .po
    python3 tools/check-po.py path/to/file.po ...   # 校验指定文件
    python3 tools/check-po.py --quiet               # 只输出问题

检查项:
    1. Sphinx 角色目标 (:doc:/:ref:/... 的 <target>) 与原文一致
    2. ``字面量`` 与原文一致
    3. URL 与原文一致
    4. 强调标记 (* / **) 的种类与数量与原文逐一对应（不得增删、升降级）
    5. 无残留的英文式破折号 ` - `
    6. 中文与行内标记之间无多余空格；全角标点前后无空格
    7. 省略号写作「……」
    8. 术语禁译（纪律、how-to 等）

退出码: 有 ERROR 时为 1，否则为 0。
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

try:
    from babel.messages.pofile import read_po
except ImportError:  # pragma: no cover
    print("需要 babel：pip install -r requirements.txt", file=sys.stderr)
    raise SystemExit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_GLOB = os.path.join(ROOT, "translation", "zh_CN", "LC_MESSAGES", "*.po")

# ---------------------------------------------------------------- 基础正则

ROLE_RE = re.compile(r":([a-z_]+):`([^`]*)`")
# 字面量内容里允许出现单个反引号（例如 ``:doc:`tutorials` - ...``）
LITERAL_RE = re.compile(r"``(.+?)``", re.S)
LINK_RE = re.compile(r"`([^`<]*?)<([^<>]+)>`__?")
URL_RE = re.compile(r"https?://[^\s>`\"']+")
URL_TRAILING = ".,;:!?。，；：！？、）)"
EMPH_RE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*", re.S)
MARKER_RE = re.compile(r"\*\*|\*")

CJK = r"\u3000-\u303f\u4e00-\u9fff\uff00-\uffef"
CJK_RE = re.compile(f"[{CJK}]")
FULLWIDTH_PUNCT = "，。；：、？！）】》」』…—"
SPACED_DASH_RE = re.compile(r"\S - \S")
DOUBLE_HALFWIDTH_SPACE_RE = re.compile(r"[^\s]  +[^\s]")
# 句中的 `...` 应写作 `……`；位于开头的标题续接符号不算错。
ELLIPSIS_RE = re.compile(r"(?<!^)\.\.\.")

# 术语禁译：在剔除行内标记后的正文上匹配（正则 -> 说明）
FORBIDDEN = [
    (re.compile(r"纪律"), "「discipline」被误译为「纪律」（应为「学科／专业领域／严谨」）"),
    (re.compile(r"(?<![“\"'])how-?to(?!\s*guide)"), "「how-to」未译成中文（应为「实践指南」）"),
    (re.compile(r"实践指南指南"), "重复的「指南」"),
    (re.compile(r"[a-zA-Z] +。"), "英文与句号之间不应有空格"),
]


# ---------------------------------------------------------------- 工具函数


def unescape_rst(text: str) -> str:
    """剔除行内标记，仅保留读者实际看到的正文。"""
    text = LITERAL_RE.sub("\x00", text)                     # 字面量整体隐去
    text = ROLE_RE.sub(lambda m: role_display(m.group(2)) or "\x00", text)
    text = LINK_RE.sub(lambda m: m.group(1).strip(), text)  # 链接保留显示文字
    return text


def role_display(body: str) -> str | None:
    """取角色的显示文字（`text <target>` -> `text`）。

    没有显式 `<target>` 的角色（如 ``:doc:`tutorials```）由 Sphinx 用文档标题
    填充，检查阶段无从得知，返回 None 表示「不可见」。
    """
    if not re.search(r"<[^<>]+>\s*$", body.strip()):
        return None
    return re.sub(r"\s*<[^<>]+>\s*$", "", body.strip())


def role_target(body: str) -> str:
    match = re.search(r"<([^<>]+)>\s*$", body.strip())
    return match.group(1).strip() if match else body.strip()


def inline_spans(text: str):
    """产出 (start, end, 显示文字) —— 所有会渲染成可见文字的行内标记。"""
    spans = []
    for match in EMPH_RE.finditer(text):
        spans.append((match.start(), match.end(), match.group(1) or match.group(2)))
    for match in LITERAL_RE.finditer(text):
        spans.append((match.start(), match.end(), match.group(1)))
    for match in ROLE_RE.finditer(text):
        display = role_display(match.group(2))
        if display:
            spans.append((match.start(), match.end(), display))
    for match in LINK_RE.finditer(text):
        spans.append((match.start(), match.end(), match.group(1)))
    return spans


# ---------------------------------------------------------------- 报告


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, message: str) -> None:
        self.errors.append(f"  ERROR {where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f"  WARN  {where}: {message}")

    @property
    def ok(self) -> bool:
        return not self.errors


# ---------------------------------------------------------------- 单项检查


def check_entry(rep: Report, where: str, msgid: str, msgstr: str) -> None:
    if not msgstr.strip():
        rep.error(where, "msgstr 为空（未翻译）")
        return

    # 1. Sphinx 角色目标
    src_t = sorted(role_target(b) for _r, b in ROLE_RE.findall(msgid))
    dst_t = sorted(role_target(b) for _r, b in ROLE_RE.findall(msgstr))
    if src_t != dst_t:
        rep.error(where, f"Sphinx 角色目标不一致: 原文={src_t} 译文={dst_t}")

    # 2. 字面量
    src_l = sorted(LITERAL_RE.findall(msgid))
    dst_l = sorted(LITERAL_RE.findall(msgstr))
    if src_l != dst_l:
        rep.error(where, f"``字面量`` 不一致: 原文={src_l} 译文={dst_l}")

    # 3. URL（末尾句读不计）
    src_u = sorted({u.rstrip(URL_TRAILING) for u in URL_RE.findall(msgid)})
    dst_u = sorted({u.rstrip(URL_TRAILING) for u in URL_RE.findall(msgstr)})
    if src_u != dst_u:
        rep.error(where, f"URL 不一致: 原文={src_u} 译文={dst_u}")

    # 4. 强调标记逐一对应
    src_m, dst_m = MARKER_RE.findall(msgid), MARKER_RE.findall(msgstr)
    if src_m != dst_m:
        rep.error(
            where,
            f"强调标记不一致: 原文 {src_m.count('**')} 粗 / {src_m.count('*')} 斜 "
            f"vs 译文 {dst_m.count('**')} 粗 / {dst_m.count('*')} 斜",
        )

    # 5. 英文式破折号
    if SPACED_DASH_RE.search(msgstr) and "``" not in msgstr:
        rep.error(where, "残留英文式破折号 ` - `，应改为 `——`")

    # 5b. msgstr 值内不应含真实换行（会被渲染成多余空格）
    if "\n" in msgstr:
        rep.error(where, f"msgstr 值内含换行符，会被渲染成多余空格: {msgstr[:70]!r}")

    # 6. 行内标记两侧的空格
    #    中文与中文之间的标记不留空格；拉丁字母与中文之间保留一个空格是正确排版。
    def is_cjk(char: str) -> bool:
        return bool(char) and bool(CJK_RE.match(char))

    for start, end, inner in inline_spans(msgstr):
        if not inner:
            continue
        before = msgstr[start - 1] if start > 0 else ""
        after = msgstr[end] if end < len(msgstr) else ""
        if before == " " and is_cjk(inner[0]):
            prev = msgstr[start - 2] if start >= 2 else ""
            if is_cjk(prev):
                rep.error(where, f"中文与行内标记之间多了空格: …{msgstr[max(0, start - 14):end + 4]}…")
        if after == " " and is_cjk(inner[-1]):
            nxt = msgstr[end + 1] if end + 1 < len(msgstr) else ""
            if is_cjk(nxt):
                rep.error(where, f"中文与行内标记之间多了空格: …{msgstr[start:end + 14]}…")

    # 7. 全角标点前后不得有空格
    for pattern, desc in (
        (re.compile(rf"\s+[{FULLWIDTH_PUNCT}]"), "全角标点前多了空格"),
        (re.compile(rf"[（「『【《]\s+"), "全角标点后多了空格"),
    ):
        match = pattern.search(msgstr)
        if match:
            rep.error(where, f"{desc}: …{msgstr[max(0, match.start() - 12):match.end() + 12]}…")

    if DOUBLE_HALFWIDTH_SPACE_RE.search(msgstr):
        rep.warn(where, "出现连续多个半角空格")

    # 8. 省略号写法（在剔除行内标记的正文上判断）
    stripped = unescape_rst(msgstr)
    for match in ELLIPSIS_RE.finditer(stripped):
        if stripped[: match.start()].strip():
            rep.error(where, f"省略号应写作「……」: …{stripped[max(0, match.start() - 14):match.end() + 10]}…")
            break

    # 9. 术语禁译
    prose = unescape_rst(msgstr)
    for pattern, desc in FORBIDDEN:
        if pattern.search(prose):
            rep.error(where, desc)

    # 10. 软性提示
    if msgstr.strip() == msgid.strip() and not re.fullmatch(r"[\w\s.:`<>/\\-]+", msgid.strip()):
        rep.warn(where, "msgstr 与 msgid 完全相同，确认是否为有意保留")
    if re.search(r"进行[了]?[一-龥]{2}", msgstr):
        rep.warn(where, "疑似「进行＋动词」冗余结构，可考虑直接用动词")


def check_file(path: str, rep: Report, quiet: bool) -> int:
    with open(path, encoding="utf-8") as handle:
        catalog = read_po(handle, locale="zh_CN")

    name = os.path.basename(path)
    count = 0
    for message in catalog:
        if not message.id:
            continue
        msgid = message.id if isinstance(message.id, str) else message.id[0]
        msgstr = message.string if isinstance(message.string, str) else (message.string or [""])[0]
        count += 1
        check_entry(rep, f"{name}#{count}", msgid, msgstr)

    if not quiet:
        print(f"{name}: {count} 条")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description="校验 Diátaxis zh_CN .po 文件")
    parser.add_argument("paths", nargs="*", help="要校验的 .po 文件（默认全部）")
    parser.add_argument("--quiet", action="store_true", help="只输出问题")
    args = parser.parse_args()

    paths = args.paths or sorted(glob.glob(DEFAULT_GLOB))
    rep = Report()
    total = 0
    for path in paths:
        total += check_file(path, rep, args.quiet)

    if not args.quiet:
        print(f"\n共校验 {len(paths)} 个文件、{total} 条字符串")

    if rep.errors:
        print(f"\n=== {len(rep.errors)} 个错误 ===")
        print("\n".join(rep.errors))
    if rep.warnings:
        print(f"\n=== {len(rep.warnings)} 个提示 ===")
        print("\n".join(rep.warnings))

    if rep.ok:
        print("\n✅ 全部通过")
        return 0
    print(f"\n❌ 存在 {len(rep.errors)} 个错误")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
