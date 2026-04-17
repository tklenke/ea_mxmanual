# ABOUTME: Tests for WR page globbing — collecting slugs from the wiki reference directory.
# ABOUTME: Covers basic slug extraction and filtering of non-.md files.

import pytest
from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages


def test_returns_slugs_for_md_files(tmp_path):
    (tmp_path / "panels-canopy.md").write_text("")
    (tmp_path / "manual-standards.md").write_text("")
    slugs = glob_wr_pages(tmp_path)
    assert set(slugs) == {"panels-canopy", "manual-standards"}


def test_ignores_non_md_files(tmp_path):
    (tmp_path / "panels-canopy.md").write_text("")
    (tmp_path / "readme.txt").write_text("")
    (tmp_path / "LICENSE").write_text("")
    slugs = glob_wr_pages(tmp_path)
    assert slugs == ["panels-canopy"]
