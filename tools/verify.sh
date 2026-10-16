#!/usr/bin/env bash
# 中文译文交付前的完整验证：结构校验 → 术语校验 → 构建 → 产物抽查
#
# 用法: bash tools/verify.sh
set -uo pipefail

cd "$(dirname "$0")/.." || exit 2
PY=.venv/bin/python
OUT=_build/zh-verify
status=0

echo "════════ 1/5  .po 结构校验（标记、角色、字面量、排版） ════════"
if ! $PY tools/check-po.py --quiet; then
  status=1
fi

echo
echo "════════ 2/5  渲染级校验（标记是否真的被解析） ════════"
if ! $PY tools/check-render.py; then
  status=1
fi

echo
echo "════════ 3/5  跨文件术语一致性 ════════"
if ! $PY tools/check-terms.py; then
  status=1
fi

echo
echo "════════ 4/5  构建中文站点 ════════"
rm -rf "$OUT"
if ! $PY -m sphinx -b dirhtml -D language=zh_CN -W --keep-going source "$OUT" 2>&1 | tail -30; then
  echo "构建失败"
  status=1
fi

echo
echo "════════ 5/5  产物抽查 ════════"
$PY - "$OUT" <<'PYEOF'
import re, sys, pathlib

out = pathlib.Path(sys.argv[1])
SKIP = {"genindex", "search"}
pages = sorted(
    p.parent.name for p in out.glob("*/index.html") if p.parent.name not in SKIP
)
bad = 0
checked = 0

for page in pages:
    f = out / page / "index.html"
    html = f.read_text(encoding="utf-8")
    # sphinx-reredirects 生成的跳转页没有正文，跳过
    if "http-equiv" in html and "refresh" in html[:2000]:
        continue
    checked += 1
    # 只看正文，排除脚本、样式与侧边导航
    article = re.search(r"<article[^>]*>(.*?)</article>", html, re.S)
    body = article.group(1) if article else html
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S)
    # 字面量内部的文本不算未解析标记
    outside = re.sub(r'<(?:tt|code) class="docutils literal[^"]*">.*?</(?:tt|code)>', "", body, flags=re.S)
    text = re.sub(r"<[^>]+>", "", body)

    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    problems = []
    if re.search(r"\*\*", outside):
        problems.append("未解析的 **")
    if "``" in outside:
        problems.append("未解析的 ``")
    if re.search(r":[a-z_]+:`", outside):
        problems.append("未解析的 :role:")
    if re.search(r"`_[^ ]", outside):
        problems.append("未解析的链接标记 `_")

    if problems or cjk < 40:
        bad += 1
        note = "、".join(problems) or f"中文字符过少（{cjk}）"
        print(f"  ✗ {page:24s} {note}")
    else:
        print(f"  ✓ {page:24s} 中文字符 {cjk:5d}")

print(f"\n  已检查 {checked} 个正文页面（跳转页与索引页除外）")

# 中文图示是否被选用
svg = sorted(p.name for p in (out / "_images").glob("*.svg"))
zh = [s for s in svg if "diataxis" in s or "overview" in s or "axes" in s or "two-dim" in s]
print(f"\n  中文图示: {len(zh)} 张 → {', '.join(zh)}")
if len(zh) < 7:
    print("  ✗ 中文 SVG 数量不足，应至少有 7 张")
    bad += 1

print()
print("  ✅ 产物抽查通过" if not bad else f"  ❌ 产物抽查发现 {bad} 处问题")
sys.exit(1 if bad else 0)
PYEOF
[ $? -ne 0 ] && status=1

echo
if [ $status -eq 0 ]; then
  echo "✅ 全部验证通过"
else
  echo "❌ 验证未通过，请查看上方输出"
fi
exit $status
