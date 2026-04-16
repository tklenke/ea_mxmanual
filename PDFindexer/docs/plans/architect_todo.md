# Architect Todo

## Phase 1: Design

- [x] Gather requirements from Tom
- [x] Evaluate PDF characteristics (born-digital, two-column layout, figure/table types)
- [x] Decide output granularity (paragraph-level files)
- [x] Design token-optimized output format (plain text, compact markers, rich index)
- [x] Design processing pipeline (TOC pass, content pass, output writing)
- [x] Document two-column extraction approach
- [x] Select library (pdfplumber)
- [x] Write design.md
- [x] Update claude/project_status.md
- [x] Create docs/plans/ structure

## Phase 2: Implementation Support

- [ ] Review programmer_todo.md tasks once Programmer begins
- [ ] Address any architectural questions that arise during implementation
- [ ] Review sample output from early implementation runs for quality
- [ ] Adjust design if extraction quality reveals issues with approach

## Phase 3: Validation

- [ ] Validate index.txt structure and completeness against TOC
- [ ] Spot-check several paragraph files for content accuracy
- [ ] Confirm output is usable by mxmanual Claude instance
