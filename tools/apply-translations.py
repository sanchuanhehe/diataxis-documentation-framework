#!/usr/bin/env python3
"""把一份「msgid -> 新 msgstr」的 JSON 安全地套用到 .po 文件上.

只替换 msgstr 块，其余内容（文件头、注释、msgid、顺序、flags）逐字节原样保留，
并按显示宽度重新折行（CJK 记 2 列），使 .po 排版统一。

用法:
    python3 tools/apply-translations.py <target.po> <translations.json> [--dry-run]

JSON 格式:
    {"<msgid 原文，逐字一致>": "<新的中文 msgstr>", ...}

任何键在目标 .po 中找不到都会报错并中止（除非 --allow-missing）。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

# PO 中的一个字符串块：一行或多行 "..."，行间以换行分隔。
# 注意不要把 entry 之间的空行吃掉。
STR_BLOCK = r'"(?:[^"\\]|\\.)*"(?:[ \t]*\n[ \t]*"(?:[^"\\]|\\.)*")*'

# 匹配一个 entry 的 msgid 块与紧随其后的 msgstr 块
ENTRY_RE = re.compile(
    r'(?P<lead>(?:^#[^\n]*\n)*)'          # 注释与 flags
    r'msgid (?P<id>' + STR_BLOCK + r')\n'
    r'msgstr (?P<str>' + STR_BLOCK + r')',
    re.M,
)

WIDTH = 78


_UNESCAPE = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "\\": "\\", "a": "\a", "b": "\b", "f": "\f", "v": "\v"}


def _decode(segment: str) -> str:
    """解码 PO 引号内的转义序列。"""
    out: list[str] = []
    index = 0
    while index < len(segment):
        char = segment[index]
        if char == "\\" and index + 1 < len(segment):
            nxt = segment[index + 1]
            out.append(_UNESCAPE.get(nxt, "\\" + nxt))
            index += 2
        else:
            out.append(char)
            index += 1
    return "".join(out)


def unquote(block: str) -> str:
    """把 PO 的多行引号块还原为实际字符串。"""
    return "".join(_decode(seg) for seg in re.findall(r'"((?:[^"\\]|\\.)*)"', block))


def _encode(text: str) -> str:
    """编码为 PO 引号内的转义序列。"""
    out: list[str] = []
    for char in text:
        if char == "\\":
            out.append("\\\\")
        elif char == '"':
            out.append('\\"')
        elif char == "\n":
            out.append("\\n")
        elif char == "\t":
            out.append("\\t")
        else:
            out.append(char)
    return "".join(out)


def quote(text: str) -> str:
    """把字符串写回 PO 的引号块，按显示宽度折行。

    折行只在「安全断点」处发生：不会把 URL、标识符或英文单词从中间劈开。
    """
    escaped = _encode(text)
    if not escaped:
        return '""'

    def cell(ch: str) -> int:
        return 2 if ord(ch) > 0x2E7F else 1

    # 连续 ASCII 词字符之间不允许断行
    wordish = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  "_-/.:@%+~?#=&")

    def safe_break(index: int) -> bool:
        """index 表示在 escaped[index-1] 与 escaped[index] 之间断开。"""
        if index <= 0 or index >= len(escaped):
            return False
        return not (escaped[index - 1] in wordish and escaped[index] in wordish)

    lines: list[str] = []
    start = 0
    width = 0
    last_safe = -1
    for index, char in enumerate(escaped):
        width += cell(char)
        if index > start and safe_break(index):
            last_safe = index
        if width > WIDTH - 2 and last_safe > start:
            # 注意：不可 rstrip，行尾空格属于字符串内容的一部分
            lines.append(escaped[start:last_safe])
            start = last_safe
            width = sum(cell(c) for c in escaped[start : index + 1])
            last_safe = -1
    lines.append(escaped[start:])

    if len(lines) == 1:
        return f'"{lines[0]}"'
    return "\n".join(f'"{line}"' for line in lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="套用 zh_CN 译文")
    parser.add_argument("po", help="目标 .po 文件")
    parser.add_argument("json", help="msgid -> msgstr 的 JSON 文件")
    parser.add_argument("--dry-run", action="store_true", help="只报告改动，不写回")
    parser.add_argument("--allow-missing", action="store_true", help="允许 JSON 中存在目标文件没有的键")
    args = parser.parse_args()

    with open(args.json, encoding="utf-8") as handle:
        updates: dict[str, str] = json.load(handle)

    with open(args.po, encoding="utf-8") as handle:
        original = handle.read()

    seen: set[str] = set()
    changed = 0
    unchanged = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changed, unchanged
        msgid = unquote(match.group("id"))
        if msgid not in updates:
            return match.group(0)
        seen.add(msgid)
        new = updates[msgid]
        old = unquote(match.group("str"))
        if old == new:
            unchanged += 1
        else:
            changed += 1
        return f'{match.group("lead")}msgid {match.group("id")}\nmsgstr {quote(new)}'

    result = ENTRY_RE.sub(replace, original)

    unused = set(updates) - seen
    if unused and not args.allow_missing:
        print(f"❌ JSON 中有 {len(unused)} 个 msgid 在目标 .po 中找不到：", file=sys.stderr)
        for key in list(unused)[:8]:
            print(f"   {key[:110]!r}", file=sys.stderr)
        return 2

    if args.dry_run:
        print(f"[dry-run] 将改动 {changed} 条，未变 {unchanged} 条，命中 {len(seen)} 条")
        return 0

    with open(args.po, "w", encoding="utf-8") as handle:
        handle.write(result)
    print(f"{os.path.basename(args.po)}: 改动 {changed} 条，未变 {unchanged} 条，命中 {len(seen)}/{len(updates)} 条")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
