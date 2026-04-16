## Project Overview

**ea_mxmanual** is a maintenance manual for a Cozy Mark IV experimental aircraft, written as a collection of Markdown files served by Otterwiki. The manual is intended for use by the aircraft owner/builder performing maintenance and inspection.

## Project Status

The project is in early development. The reference materials have been extracted and indexed. The claude guidance files, roles, and project standards are being established. Manual content has not yet been written.

## Directory Structure

```
ea_mxmanual/
├── claude/                          - Claude guidance files for this project
│   ├── project_status.md            - This file
│   ├── content_development_overview.md - Standards applicable to all roles
│   └── roles/
│       ├── architect.md             - Architect role definition
│       ├── writer.md                - Writer role definition
│       └── reviewer.md              - Reviewer role definition
├── docs/
│   ├── plans/                       - Planning and standards documents
│   │   ├── toc_structure.md         - Manual table of contents structure
│   │   ├── standards.md             - Content formatting standards (NOTE format, etc.)
│   │   ├── architect_todo.md        - Architect task tracking
│   │   └── writer_todo.md           - Writer task tracking
│   └── references/                  - Source reference materials (READ ONLY)
│       ├── AC43_13/                 - FAA Advisory Circular 43.13 extracted text
│       │                              Files named by chapter and page: ch##_p###.txt
│       │                              Appendices: appendix_1_glossary.txt, etc.
│       └── tds/                     - Manufacturer Technical Data Sheets (PDF)
├── otterwiki/                       - Otterwiki instance (currently empty)
└── PDFindexer/                      - Python tool used to extract AC43_13 text
                                       Has its own CLAUDE.md — do not read it
```

## Key Documents

- **`docs/plans/toc_structure.md`** — The current table of contents for the manual. This is the authoritative structure for what sections exist and what pages are planned.
- **`docs/plans/standards.md`** — Formatting standards including NOTE format and source conflict NOTE format.
- **`docs/plans/architect_todo.md`** — Architect's current task list.
- **`docs/plans/writer_todo.md`** — Writer's current task list.

## Reference Materials

All files in `docs/references/` are **READ ONLY**. Never modify these files.

- **`docs/references/AC43_13/`** — FAA Advisory Circular 43.13, *Acceptable Methods, Techniques, and Practices — Aircraft Inspection and Repair*. Text files extracted from the PDF, organized by chapter and page.
- **`docs/references/tds/`** — Manufacturer Technical Data Sheets for specific products used on the aircraft. PDFs provided by manufacturers.

When AC 43.13 and a TDS conflict, the TDS takes precedence. See `claude/content_development_overview.md` and `docs/plans/standards.md` for full guidance.
