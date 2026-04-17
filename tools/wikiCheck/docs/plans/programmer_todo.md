# wikiCheck Programmer Todo

## Phase 1: Core data collection — [x] Complete

## Phase 2: Statistics — [x] Complete

## Phase 3: Output — [x] Complete

## Phase 4: CLI and integration — [x] Complete

## Phase 6: Orphan page detection

Orphan pages are WR pages that exist as `.md` files but are never referenced as link
targets from any other WR page. Logic is the inverse of broken links.

### [x] 6.1 Extract `collect_referenced_slugs()` helper (refactor)

- In `wikicheck/broken_links.py`, extract the inner loop into:
  `collect_referenced_slugs(wr_dir: Path) -> set[str]`
- Rewrite `find_broken_links()` to call it: `return sorted(referenced - known)`
- Tests: update `tests/test_broken_links.py` to cover the helper directly;
  existing broken-link tests must still pass

### [x] 6.2 Add `wikicheck/orphan_pages.py`

- `find_orphan_pages(wr_dir: Path) -> list[str]`
  - `known = set(glob_wr_pages(wr_dir))`
  - `referenced = collect_referenced_slugs(wr_dir)`
  - `return sorted(known - referenced)`
- File must start with ABOUTME comments
- Tests: new `tests/test_orphan_pages.py`
  - page never linked → appears in result
  - page linked from another page → not an orphan
  - all pages linked → empty result
  - empty WR dir → empty result

### [x] 6.3 Add `orphan_count` to `Stats`

- In `wikicheck/stats.py`:
  - Add `orphan_count: int` field to `Stats` dataclass
  - Call `find_orphan_pages(wr_dir)` in `compute_stats()` and set the field
- Tests: update `tests/test_stats.py` to assert `orphan_count` is correct

### [x] 6.4 Update `format_report()` and `format_detail()`

- In `wikicheck/report.py`:
  - Add orphan line to `format_report()` between broken links and approved:
    `f"Orphan pages:            {stats.orphan_count}  (exist in WR, never linked to)"`
    (right-align count in the same column as broken links count)
  - Add `orphan_pages: list` parameter to `format_detail()`
  - Add orphan section to `format_detail()` between broken links and unreviewed:
    `section("Orphan pages:", orphan_pages)`
  - Update `format_missing_log_report()` — no orphan line needed (log missing path
    does not report review log stats)
- Tests:
  - Update `tests/test_report.py` to assert orphan line appears in `format_report()`
    output and in correct position
  - Update `tests/test_detail.py` to assert orphan section appears and is correct

### [x] 6.5 Update `wiki_check.py` CLI

- Import `find_orphan_pages` from `wikicheck.orphan_pages`
- In the normal (log exists) path:
  - Compute `orphans = find_orphan_pages(WR_DIR)` inside the `--detail` block
  - Pass `orphan_pages=orphans` to `format_detail()`
- In the missing-log path:
  - Pass `orphan_pages=[]` to `format_detail()` (no orphan data without full scan)
- Tests:
  - Update `tests/test_cli.py` — orphan line present in `--detail` output
  - Update `tests/test_e2e.py` — end-to-end run includes orphan count in summary
    and orphan list in `--detail` output

## Phase 5: AR integration

### [ ] 5.1 Create `docs/notes/review_log.md` in ea_mxmanual project
- Run `wiki_check.py`, take the generated template from `data/`, move to `docs/notes/`
- Commit in ea_mxmanual repo

### [ ] 5.2 Update `claude/roles/reviewer.md` in ea_mxmanual project
- Add wikiCheck startup sequence per design.md spec
- Add post-review log update step
- Commit in ea_mxmanual repo

### [ ] 5.3 Update `claude/project_status.md` in ea_mxmanual project
- Document `docs/notes/` directory and `review_log.md`
- Commit in ea_mxmanual repo
