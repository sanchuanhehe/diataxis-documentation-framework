#!/usr/bin/env python3
"""渲染级校验：确认每条译文里的行内标记真的会被 docutils 解析，而不是原样显示.

`.po` 文件里写着 `**粗体**`，渲染出来却是一对星号，这是最隐蔽也最严重的一类缺陷：
句法校验看不出来，只有真正解析一遍才会暴露。

本脚本用与站点构建完全相同的设置（``source/docutils.conf`` 中的
``character-level-inline-markup``）逐条解析 msgstr，然后检查：

1. 渲染结果里不再残留 ``**``、``*``、`` ``` `` 、``:role:` `` 等未解析的标记；
2. 解析出的 <strong>/<em>/<literal> 节点数量与 msgid 中的标记数量一致。

用法:
    python3 tools/check-render.py                 # 全部
    python3 tools/check-render.py map tutorials   # 指定文件
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

from docutils import nodes
from docutils.core import publish_parts
from docutils.parsers.rst import roles

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib.machinery import SourceFileLoader

_dump = SourceFileLoader("dump_pairs", os.path.join(os.path.dirname(os.path.abspath(__file__)), "dump-pairs.py")).load_module()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PO_DIR = os.path.join(ROOT, "translation", "zh_CN", "LC_MESSAGES")

# 站点构建时真实存在的角色，这里用哑角色代替，只关心标记能否被识别
def _dummy_role(name, rawtext, text, *args, **kwargs):
    """哑角色：只验证标记被识别，产出不参与 strong/em/literal 计数。"""
    node = nodes.inline(rawtext, text)
    node["classes"].append("dsh-role")
    return [node], []


for _role in ("doc", "ref", "class", "meth", "func", "mod", "attr", "exc", "obj"):
    roles.register_local_role(_role, _dummy_role)


def docutils_conf_enabled() -> bool:
    """确认 source/docutils.conf 已开启字符级行内标记。"""
    path = os.path.join(ROOT, "source", "docutils.conf")
    if not os.path.exists(path):
        return False
    text = open(path, encoding="utf-8").read()
    return bool(re.search(r"character-level-inline-markup\s*=\s*true", text, re.I))


SETTINGS = {
    "character_level_inline_markup": True,
    "report_level": 5,      # 静音
    "halt_level": 5,
    "input_encoding": "unicode",
    "embed_stylesheet": False,
    "doctitle_xform": False,
    "sectsubtitle_xform": False,
    "docinfo_xform": False,
}


def render(text: str) -> str:
    """把一条 msgstr 当作单段落解析，返回 HTML 片段。"""
    flat = text.replace("\n", " ")
    # 用「占位前缀」挡住块级结构（行首的 * / - / # 等），不参与行内解析的判定
    try:
        body = publish_parts("Z" + flat, writer_name="html", settings_overrides=SETTINGS)["body"]
    except Exception as exc:  # pragma: no cover
        return f"<render-error>{exc}</render-error>"
    return re.sub(r"^<p>Z", "<p>", body.strip()).replace("\n", " ")


def counts(html: str) -> dict[str, int]:
    return {
        "strong": len(re.findall(r"<strong>", html)),
        "em": len(re.findall(r"<em>", html)),
        "literal": len(re.findall(r'class="docutils literal', html)),
        "reference": len(re.findall(r'<a class="reference', html)),
    }


def expected_counts(msgid: str) -> dict[str, int]:
    """从英文原文推算应有的节点数。"""
    strong = len(re.findall(r"\*\*[^*]+\*\*", msgid))
    # 字面量内容里可能含单个反引号（如 ``:doc:`tutorials` ...``），故用非贪婪 .+?
    literal = len(re.findall(r"``.+?``", msgid, re.S))
    stripped = re.sub(r"\*\*", "", msgid)
    stripped = re.sub(r"``.+?``", "", stripped, flags=re.S)
    em = len(re.findall(r"\*[^*]+\*", stripped))
    return {"strong": strong, "em": em, "literal": literal}


def main() -> int:
    parser = argparse.ArgumentParser(description="渲染级校验")
    parser.add_argument("names", nargs="*", help="资源名（默认全部）")
    args = parser.parse_args()

    if not docutils_conf_enabled():
        print("⚠️  source/docutils.conf 未开启 character-level-inline-markup，"
              "中文正文中紧贴汉字的行内标记将无法解析。\n")

    names = args.names or sorted(
        os.path.basename(p)[:-3] for p in glob.glob(os.path.join(PO_DIR, "*.po"))
    )

    problems: list[str] = []
    total = 0
    for name in names:
        for index, (msgid, msgstr) in enumerate(_dump.load(name), 1):
            total += 1
            html = render(msgstr)
            got = counts(html)

            # 1. 未解析的标记残留
            #    字面量内部的文本（如 ``:doc:`tutorials` ...`` 这个示例）不算残留
            outside_literals = re.sub(
                r'<tt class="docutils literal">.*?</tt>', "", html, flags=re.S
            )
            residue = []
            if re.search(r"\*\*", outside_literals):
                residue.append("**")
            plain = re.sub(r"<[^>]+>", "", outside_literals)
            if re.search(r"(?<![\w*])\*(?![\w*])", plain) and not re.search(r"\*", msgid):
                residue.append("*")
            if "``" in outside_literals:
                residue.append("``")
            if re.search(r":[a-z_]+:`", outside_literals):
                residue.append(":role:")
            if residue:
                problems.append(
                    f"[{name}#{index}] 标记未解析，原样输出 {'/'.join(residue)}：{html[:120]}"
                )
                continue

            # 2. 节点数量应与英文一致
            want = expected_counts(msgid)
            for kind, want_n in want.items():
                if got[kind] != want_n:
                    problems.append(
                        f"[{name}#{index}] {kind} 数量不符：原文应有 {want_n}，实际渲染 {got[kind]}"
                        f"\n        EN: {msgid[:100]}\n        ZH: {msgstr[:100]}"
                    )

    print(f"共解析 {len(names)} 个文件、{total} 条字符串")
    if problems:
        print(f"\n=== {len(problems)} 处渲染问题 ===")
        for item in problems[:60]:
            print("  " + item)
        if len(problems) > 60:
            print(f"  …另有 {len(problems) - 60} 处")
        return 1
    print("\n✅ 渲染级校验通过：所有行内标记均被正确解析")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
