# ABOUTME: Collects WR page slugs by globbing .md files in the wiki reference directory.
# ABOUTME: Returns a sorted list of slug strings (filename without extension).

from pathlib import Path


def glob_wr_pages(wr_dir: Path) -> list[str]:
    return sorted(p.stem for p in Path(wr_dir).glob("*.md"))
