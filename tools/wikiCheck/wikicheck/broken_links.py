# ABOUTME: Detects broken internal links across the WR by cross-referencing slugs against .md files.
# ABOUTME: Returns a sorted, deduplicated list of slugs that have no corresponding page.

from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages
from wikicheck.link_parser import extract_links


def find_broken_links(wr_dir: Path) -> list[str]:
    known = set(glob_wr_pages(wr_dir))
    referenced = set()
    for md_file in Path(wr_dir).glob("*.md"):
        for slug in extract_links(md_file.read_text()):
            referenced.add(slug)
    return sorted(referenced - known)
