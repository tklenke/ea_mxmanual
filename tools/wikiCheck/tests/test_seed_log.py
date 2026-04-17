# ABOUTME: Tests for seeding a review_log.md when the log is missing.
# ABOUTME: Covers file generation, content format, and summary output message.

from pathlib import Path
from wikicheck.seed_log import seed_review_log


def test_generates_seeded_log(tmp_path):
    wr_dir = tmp_path / "wr"
    wr_dir.mkdir()
    (wr_dir / "panels-canopy.md").write_text("")
    (wr_dir / "manual-standards.md").write_text("")
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    seed_review_log(wr_dir, data_dir, today="2026-04-16")

    out = data_dir / "review_log.md"
    assert out.exists()


def test_seeded_log_contains_all_slugs(tmp_path):
    wr_dir = tmp_path / "wr"
    wr_dir.mkdir()
    (wr_dir / "panels-canopy.md").write_text("")
    (wr_dir / "manual-standards.md").write_text("")
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    seed_review_log(wr_dir, data_dir, today="2026-04-16")

    content = (data_dir / "review_log.md").read_text()
    assert "panels-canopy" in content
    assert "manual-standards" in content


def test_seeded_log_all_unreviewed(tmp_path):
    wr_dir = tmp_path / "wr"
    wr_dir.mkdir()
    (wr_dir / "panels-canopy.md").write_text("")
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    seed_review_log(wr_dir, data_dir, today="2026-04-16")

    content = (data_dir / "review_log.md").read_text()
    assert "unreviewed" in content
    assert "Approved" not in content


def test_seeded_log_has_today_date(tmp_path):
    wr_dir = tmp_path / "wr"
    wr_dir.mkdir()
    (wr_dir / "page.md").write_text("")
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    seed_review_log(wr_dir, data_dir, today="2026-04-16")

    content = (data_dir / "review_log.md").read_text()
    assert "2026-04-16" in content


def test_seed_log_summary_message(tmp_path):
    wr_dir = tmp_path / "wr"
    wr_dir.mkdir()
    (wr_dir / "page.md").write_text("")
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    msg = seed_review_log(wr_dir, data_dir, today="2026-04-16")

    assert "NOT FOUND" in msg
    assert "review_log.md" in msg
