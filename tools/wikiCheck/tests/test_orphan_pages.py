# ABOUTME: Tests for orphan page detection across the WR directory.
# ABOUTME: Covers pages that exist as .md files but are never linked to from other pages.

from pathlib import Path
from wikicheck.orphan_pages import find_orphan_pages


def test_unlinked_page_is_orphan(tmp_path):
    (tmp_path / "page-a.md").write_text("No links here.")
    assert find_orphan_pages(tmp_path) == ["page-a"]


def test_linked_page_is_not_orphan(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]].")
    (tmp_path / "page-b.md").write_text("Content.")
    assert find_orphan_pages(tmp_path) == ["page-a"]


def test_all_pages_linked_returns_empty(tmp_path):
    (tmp_path / "page-a.md").write_text("See [[page-b]].")
    (tmp_path / "page-b.md").write_text("See [[page-a]].")
    assert find_orphan_pages(tmp_path) == []


def test_empty_wr_dir_returns_empty(tmp_path):
    assert find_orphan_pages(tmp_path) == []


def test_orphan_pages_sorted(tmp_path):
    (tmp_path / "zebra.md").write_text("No links.")
    (tmp_path / "alpha.md").write_text("No links.")
    assert find_orphan_pages(tmp_path) == ["alpha", "zebra"]
