#!/usr/bin/env python3
"""Regenerate the Chinese SVGs for the core Diátaxis diagrams.

Run from any working directory with ``python3 scripts/generate-core-diagrams.py``.
The overview diagrams retain the original artwork's single-quadrant crops.
"""

from html import escape
from pathlib import Path


OUTPUT = Path(__file__).resolve().parents[1] / "source" / "images" / "zh_CN"
FONT = "'Noto Sans CJK SC','PingFang SC','Microsoft YaHei',sans-serif"
INK = "#181818"
ORANGE = "#e98224"
LINE = "#989898"


def text(x, y, content, size, color=INK, weight=400):
    return (
        f'<text x="{x}" y="{y}" text-anchor="middle" '
        f'font-size="{size}" font-weight="{weight}" fill="{color}">'
        f"{escape(content)}</text>"
    )


def line(x1, y1, x2, y2):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{LINE}" stroke-width="1.5"/>'
    )


def axis_label(x, y, primary, definition):
    """Keep Chinese labels upright, and distinguish the term from its gloss."""
    return "\n".join(
        [
            f'<rect x="{x - 58}" y="{y - 48}" width="116" height="96" fill="#fff"/>',
            text(x, y, primary, 44, weight=500),
            text(x, y + 34, f"（{definition}）", 24),
        ]
    )


def horizontal_label(x, primary, definition):
    return "\n".join(
        [
            f'<rect x="{x - 106}" y="302" width="212" height="68" fill="#fff"/>',
            f'<text x="{x}" y="352" text-anchor="middle" fill="{INK}">'
            f'<tspan font-size="44" font-weight="500">{primary}</tspan>'
            f'<tspan font-size="26">（{definition}）</tspan></text>',
        ]
    )


QUADRANTS = {
    "tutorials": (315, "教程", "学习", "行与学：教程帮助读者通过行动习得知识与技能。"),
    "how-to": (885, "实践指南", "目标", "行与用：实践指南帮助读者通过行动完成实际目标。"),
    "explanation": (315, "解释说明", "理解", "知与学：解释说明帮助读者建立认知、加深理解。"),
    "reference": (885, "参考资料", "信息", "知与用：参考资料提供读者在工作中查用的知识信息。"),
}


def diagram(quadrants=(), axes=("action", "cognition", "acquisition", "application")):
    elements = [line(0, 337.5, 1200, 337.5), line(600, 0, 600, 675)]
    if "action" in axes:
        elements.append(axis_label(600, 222, "行", "行动"))
    if "cognition" in axes:
        elements.append(axis_label(600, 453, "知", "认知"))
    if "acquisition" in axes:
        elements.append(horizontal_label(315, "学", "习得"))
    if "application" in axes:
        elements.append(horizontal_label(885, "用", "应用"))
    for name in quadrants:
        x, title, focus, _ = QUADRANTS[name]
        if name in ("tutorials", "how-to"):
            elements.extend([text(x, 210, title, 56), text(x, 266, focus, 32, ORANGE)])
        else:
            elements.extend([text(x, 442, focus, 32, ORANGE), text(x, 518, title, 56)])
    return "\n".join(elements)


def save(name, title, description, content, viewbox="0 0 1200 675", width=1200, height=675):
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{viewbox}" role="img" aria-labelledby="title desc" lang="zh-CN">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(description)}</desc>
  <rect width="1200" height="675" fill="#fff"/>
  <g font-family="{FONT}">
{content}
  </g>
</svg>
'''
    (OUTPUT / f"{name}.svg").write_text(svg, encoding="utf-8")


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    all_quadrants = tuple(QUADRANTS)
    full_description = (
        "Diátaxis 的两个维度是知与行、学与用。纵向上方为行（行动），下方为知（认知）；"
        "横向左侧为学（习得），右侧为用（应用）。左上是教程，重在学习；右上是实践指南，"
        "重在目标；左下是解释说明，重在理解；右下是参考资料，重在信息。"
    )
    save("diataxis", "Diátaxis：知与行、学与用", full_description, diagram(all_quadrants))
    save("axes-of-needs", "文档需求的两个维度", full_description, diagram(all_quadrants))
    save(
        "two-dimensions", "知与行、学与用两个维度",
        "纵向上方为行（行动），下方为知（认知）；横向左侧为学（习得），右侧为用（应用）。",
        diagram(),
    )
    overview_settings = {
        "tutorials": ("0 65 660 310.284", ("action", "acquisition")),
        "how-to": ("540 65 660 310.284", ("action", "application")),
        "explanation": ("0 300 660 310.284", ("cognition", "acquisition")),
        "reference": ("540 300 660 310.284", ("cognition", "application")),
    }
    for name, (viewbox, axes) in overview_settings.items():
        _, title, focus, description = QUADRANTS[name]
        save(f"overview-{name}", f"{title}：{focus}", description, diagram((name,), axes),
             viewbox=viewbox, width=1021, height=480)

    save(
        "action-cognition", "知与行：认知与行动",
        "横线分隔两种活动：上方的行指行动，下方的知指认知。",
        "\n".join([line(38, 337.5, 1162, 337.5),
                   axis_label(600, 250, "行", "行动"), axis_label(600, 453, "知", "认知")]),
    )
    save(
        "acquisition-application", "学与用：习得与应用",
        "竖线分隔两种目的：左侧的学指习得知识与技能，右侧的用指应用已有的知识与技能。",
        "\n".join([line(600, 14, 600, 661), horizontal_label(420, "学", "习得"),
                   horizontal_label(780, "用", "应用")]),
    )
    print(f"Generated 9 Chinese SVG diagrams in {OUTPUT}")


if __name__ == "__main__":
    main()
