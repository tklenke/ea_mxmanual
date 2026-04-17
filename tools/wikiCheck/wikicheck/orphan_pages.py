# ABOUTME: Detects orphan pages in the WR — pages that exist but are never linked to.
# ABOUTME: A page is an orphan if its slug appears in known pages but not in any link target.

from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages
from wikicheck.broken_links import collect_referenced_slugs


def find_orphan_pages(wr_dir: Path) -> list[str]:
    known = set(glob_wr_pages(wr_dir))
    referenced = collect_referenced_slugs(wr_dir)
    return sorted(known - referenced)
