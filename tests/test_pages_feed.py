"""Chinese project sites keep feed URLs inside their deployed Pages path."""

import xml.etree.ElementTree as ET

from conftest import _build


def test_chinese_feed_at_project_root(tmp_path):
    base = "https://sanchuanhehe.github.io/diataxis-documentation-framework/"
    out = _build(
        tmp_path,
        "zh_CN",
        buildername="dirhtml",
        extra_config=(
            f"\natom_feed_base_url = {base!r}\n"
            "atom_feed_language_prefix = ''\n"
        ),
    )
    feed = ET.parse(out / "atom.xml").getroot()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    links = feed.findall("a:link", ns)
    assert {link.get("href") for link in links} == {
        base + "atom.xml",
        base + "news/",
    }
    for link in feed.findall("a:entry/a:link", ns):
        assert link.get("href").startswith(base + "news/#news-")
    html = (out / "news/index.html").read_text(encoding="utf-8")
    assert f'href="{base}atom.xml"' in html
