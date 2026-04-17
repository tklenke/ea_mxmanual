# ABOUTME: Tests for broken link detection across the WR directory.
# ABOUTME: Covers cross-referencing extracted slugs against known pages, and deduplication.

from pathlib import Path
from wikicheck.broken_links import find_broken_links


def test_detects_broken_link(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]] for info.")
    # page-b.md does not exist
    broken = find_broken_links(tmp_path)
    assert broken == ["page-b"]


def test_no_broken_links(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]].")
    (tmp_path / "page-b.md").write_text("Content.")
    assert find_broken_links(tmp_path) == []


def test_deduplicates_broken_links(tmp_path):
    (tmp_path / "page-a.md").write_text("[[missing]] and [[missing]] again.")
    (tmp_path / "page-b.md").write_text("Also [[missing]].")
    broken = find_broken_links(tmp_path)
    assert broken == ["missing"]


def test_broken_links_sorted(tmp_path):
    (tmp_path / "page-a.md").write_text("[[zebra]] and [[alpha]]")
    broken = find_broken_links(tmp_path)
    assert broken == ["alpha", "zebra"]
