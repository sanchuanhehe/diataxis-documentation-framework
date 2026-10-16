#!/usr/bin/env python3
"""生成「原文 → 原译 → 新译」的改动报告，供人工审校.

用法:
    python3 tools/diff-report.py                # 全部文件
    python3 tools/diff-report.py map quality    # 指定文件
    python3 tools/diff-report.py --stat         # 只打印统计
    python3 tools/diff-report.py --only-changed # 只列改动条目（默认）
    python3 tools/diff-report.py --all          # 连未改动条目一起列

以 git HEAD 中的版本为「原译」，工作区当前内容为「新译」。
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib.machinery import SourceFileLoader

_dump = SourceFileLoader("dump_pairs", os.path.join(os.path.dirname(os.path.abspath(__file__)), "dump-pairs.py")).load_module()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PO_DIR = os.path.join(ROOT, "translation", "zh_CN", "LC_MESSAGES")
STR_BLOCK = r'"(?:[^"\\]|\\.)*"(?:[ \t]*\n[ \t]*"(?:[^"\\]|\\.)*")*'
ENTRY_RE = re.compile(
    r"msgid (?P<id>" + STR_BLOCK + r")\nmsgstr (?P<str>" + STR_BLOCK + r")", re.M
)


def parse(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for match in ENTRY_RE.finditer(text):
        msgid = _dump.unquote(match.group("id"))
        if msgid:
            out[msgid] = _dump.unquote(match.group("str"))
    return out


def head_version(name: str) -> str:
    rel = os.path.relpath(os.path.join(PO_DIR, f"{name}.po"), ROOT)
    try:
        return subprocess.run(
            ["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout
    except subprocess.CalledProcessError:
        return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="生成译文改动报告")
    parser.add_argument("names", nargs="*", help="资源名（默认全部）")
    parser.add_argument("--stat", action="store_true", help="只打印统计")
    parser.add_argument("--all", action="store_true", help="连未改动条目一起列出")
    args = parser.parse_args()

    names = args.names or sorted(
        os.path.basename(p)[:-3] for p in glob.glob(os.path.join(PO_DIR, "*.po"))
    )

    grand_changed = grand_total = 0
    for name in names:
        before = parse(head_version(name))
        after = parse(open(os.path.join(PO_DIR, f"{name}.po"), encoding="utf-8").read())
        changed = [k for k in after if k in before and before[k] != after[k]]
        added = [k for k in after if k not in before]
        removed = [k for k in before if k not in after]
        grand_changed += len(changed)
        grand_total += len(after)

        line = f"{name:24s} {len(after):3d} 条  改动 {len(changed):3d}"
        if added:
            line += f"  新增 {len(added)}"
        if removed:
            line += f"  消失 {len(removed)}"
        print(line)
        if args.stat:
            continue

        for key in changed if not args.all else list(after):
            old = before.get(key, "")
            new = after[key]
            if not args.all and old == new:
                continue
            print(f"\n  ── [{name}]")
            print(f"  EN | {key}")
            if old:
                print(f"  旧 | {old}")
            print(f"  新 | {new}")

    print(f"\n合计：{grand_total} 条，改动 {grand_changed} 条")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
