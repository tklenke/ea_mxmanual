# ABOUTME: Generates a seeded review_log.md when the AR log is missing.
# ABOUTME: Writes all WR slugs as unreviewed entries; returns a summary message string.

from pathlib import Path
from wikicheck.wr_pages import glob_wr_pages

_HEADER = """\
# Review Log
Last updated: {today}

| Page | Status | Last Reviewed |
|------|--------|---------------|
"""

_ROW = "| {slug} | unreviewed | — |\n"


def seed_review_log(wr_dir: Path, data_dir: Path, today: str) -> str:
    slugs = glob_wr_pages(wr_dir)
    lines = _HEADER.format(today=today)
    for slug in slugs:
        lines += _ROW.format(slug=slug)
    out_path = Path(data_dir) / "review_log.md"
    out_path.write_text(lines)
    return (
        f"Review log:              NOT FOUND — seeded template written to\n"
        f"                         {out_path}\n"
        f"                         move to: docs/notes/review_log.md"
    )
