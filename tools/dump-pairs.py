#!/usr/bin/env python3
"""把某个 .po 的 msgid/msgstr 以对照形式打印出来，便于通读与改写.

用法:
    python3 tools/dump-pairs.py <name>            # 例如 tutorials
    python3 tools/dump-pairs.py <name> --json     # 输出 msgid -> msgstr 的 JSON
    python3 tools/dump-pairs.py --all             # 全部文件
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PO_DIR = os.path.join(ROOT, "translation", "zh_CN", "LC_MESSAGES")

STR_BLOCK = r'"(?:[^"\\]|\\.)*"(?:[ \t]*\n[ \t]*"(?:[^"\\]|\\.)*")*'
ENTRY_RE = re.compile(
    r"(?P<lead>(?:^#[^\n]*\n)*)msgid (?P<id>" + STR_BLOCK + r")\nmsgstr (?P<str>" + STR_BLOCK + r")",
    re.M,
)
_UNESCAPE = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "\\": "\\"}


def decode(segment: str) -> str:
    out, index = [], 0
    while index < len(segment):
        char = segment[index]
        if char == "\\" and index + 1 < len(segment):
            out.append(_UNESCAPE.get(segment[index + 1], "\\" + segment[index + 1]))
            index += 2
        else:
            out.append(char)
            index += 1
    return "".join(out)


def unquote(block: str) -> str:
    return "".join(decode(seg) for seg in re.findall(r'"((?:[^"\\]|\\.)*)"', block))


def load(name: str) -> list[tuple[str, str]]:
    path = os.path.join(PO_DIR, f"{name}.po")
    text = open(path, encoding="utf-8").read()
    pairs = []
    for match in ENTRY_RE.finditer(text):
        msgid = unquote(match.group("id"))
        if msgid:
            pairs.append((msgid, unquote(match.group("str"))))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(description="对照打印 .po 的原文与译文")
    parser.add_argument("name", nargs="?", help="资源名，如 tutorials")
    parser.add_argument("--all", action="store_true", help="处理全部文件")
    parser.add_argument("--json", action="store_true", help="输出 msgid -> msgstr 的 JSON")
    args = parser.parse_args()

    names = (
        sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(PO_DIR, "*.po")))
        if args.all
        else [args.name]
    )
    if not names or names == [None]:
        parser.error("请给出资源名，或使用 --all")

    if args.json:
        merged = {}
        for name in names:
            merged.update(dict(load(name)))
        json.dump(merged, sys.stdout, ensure_ascii=False, indent=1)
        print()
        return 0

    for name in names:
        print(f"\n{'=' * 90}\n{name}.po\n{'=' * 90}")
        for index, (msgid, msgstr) in enumerate(load(name), 1):
            print(f"\n[{index}]\nEN| {msgid}\nZH| {msgstr}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
