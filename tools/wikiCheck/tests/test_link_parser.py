# ABOUTME: Tests for Otterwiki internal link extraction from page content.
# ABOUTME: Covers [[slug]] and [[Display Text|slug]] forms, and non-link content.

from wikicheck.link_parser import extract_links


def test_extracts_bare_slug():
    assert extract_links("See [[panels-canopy]] for details.") == ["panels-canopy"]


def test_extracts_display_text_form():
    assert extract_links("See [[Canopy Panels|panels-canopy]] here.") == ["panels-canopy"]


def test_extracts_multiple_links():
    content = "[[manual-standards]] and [[Canopy|panels-canopy]]"
    assert set(extract_links(content)) == {"manual-standards", "panels-canopy"}


def test_ignores_non_link_content():
    assert extract_links("No links here. Just plain text.") == []


def test_ignores_single_brackets():
    assert extract_links("[not a link]") == []
