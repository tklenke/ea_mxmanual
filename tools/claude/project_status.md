## Project Overview

**tools/** is a collection of Python utilities that support the ea_mxmanual project.

### Tools

**PDFindexer** — Reads the FAA AC 43.13-1B PDF ("Acceptable Methods, Techniques, and
Practices - Aircraft Inspection and Repair"), extracts its content by paragraph, and
writes a structured text index and paragraph-level text files. Output is consumed by
CMW (claude-maintenance-writer), the Claude instance writing aircraft-specific
maintenance procedures for the Cozy Mark IV ea_mxmanual project.

**wikiCheck** — Checks integrity of the wiki reference (WR) and the AR review log.
Detects broken internal links and tracks which WR pages have been reviewed.

---

## Shared Structure

```
tools/
  docs/
    acronyms.md              <- project-wide acronyms and domain terms
    style-guide.md           <- naming conventions and coding standards
    plans/
      architect_todo.md      <- architect task tracking across all tools
  claude/
    roles/                   <- role definitions (Architect, Programmer, Code Reviewer)
    project_status.md        <- this file
    software_development_overview.md
  CLAUDE.md
```

## Per-Tool Structure

Each tool lives in its own subdirectory with:
```
<tool>/
  docs/
    plans/
      design.md              <- architecture and design decisions
      programmer_todo.md     <- implementation task tracking
      required_from_tom.md   <- blocked items awaiting Tom's input
    references/              <- reference materials (READ ONLY)
  <package>/                 <- Python source package
  tests/                     <- test suite
  requirements.txt
  README.md (when complete)
  venv/                      <- Python virtual environment
```

---

## PDFindexer

### Status: Implementation in progress (Phases 1–7 likely complete; 8–10 pending)

### Output

The program writes to `PDFindexer/data/`:
- `index.txt` — master index listing all chapters, sections, and paragraph titles with filenames
- `ch##_p###.txt` — one plain text file per paragraph
- `appendix_1_glossary.txt`, `appendix_2_acronyms.txt`, `appendix_3_metric.txt`

Tom copies the contents of `PDFindexer/data/` to `../docs/references/FAA43_13/` in the
ea_mxmanual project after a successful run.

### Reference Materials
- `PDFindexer/docs/references/ac_43.13.pdf` — source PDF (646 pages, born-digital). READ ONLY.

### Environment Setup

```bash
cd PDFindexer
source venv/bin/activate
pip install -r requirements.txt
pytest
pytest tests/test_example.py
pytest -v
pytest -s
```

---

## wikiCheck

### Status: Design complete; implementation not started

### Paths
- WR (wiki reference): `/home/tom/projects/N657CZDashTwo`
- AR review log: `<ea_mxmanual>/docs/notes/review_log.md`

### Environment Setup

TBD — no requirements.txt yet.
