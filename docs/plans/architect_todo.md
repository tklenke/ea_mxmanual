# Architect Todo

## In Progress

## Backlog

### [x] Set up OtterWiki instance on local machine (2026-04-16)

Instance running. Pilot pages (panels-canopy, panels-canopy-cleaning) and home.md TOC reviewed and look good. Auto-generated sidebar acceptable so far.

### [ ] OtterWiki navigation sidebar strategy — confirm final decision

Options evaluated 2026-04-16:
- **Option A:** Hand-maintained `_sidebar.md`
- **Option B:** Derived from `toc_structure.md`
- **Option C:** OtterWiki built-in auto-generated index

**Current decision: Option C.** Auto-generated sidebar reviewed with initial content (2026-04-16) — acceptable so far. Revisit as content volume grows. Do not close until Tom confirms Option C is the permanent approach.

### [x] Migrate architecture_decisions.md to Otterwiki as Manual Standards page (2026-04-16)

Writer task created in writer_todo.md. See "Publish Manual Standards page (Section 1)".

### [x] Audit and revise toc_structure.md

Completed 2026-04-16. Full restructure: 18 sections, all pages defined, all content decisions documented in architecture_decisions.md.

The current TOC has significant problems identified on 2026-04-15. Do not begin writing content until this is resolved.

**Problems to address:**

1. **Section 16 (Avionics) is generic commercial-aircraft boilerplate.** The following items almost certainly don't exist on the Cozy Mark IV and should be removed or verified:
   - HF Communication
   - Instrument Landing System (ILS)
   - Fly-by-Wire Technology
   - Terrain Awareness and Warning Systems (TAWS)
   - Ground Proximity Warning Systems (GPWS)
   - Traffic Alert and Collision Avoidance System (TCAS)

2. **Section 14 (Electrical) is also suspiciously generic.** Needs to be audited against what is actually installed on the aircraft.

3. **Wildly inconsistent depth.** Sections 14 and 16 have elaborate sub-page trees; Sections 2, 6, 15, 17, 18 are completely empty. Section 6 (Inspection) should be one of the most developed sections for a maintenance manual — it is currently a skeleton.

4. **Duplicate section number.** Two entries labeled 7.2 in Section 7 (Structures).

5. **Section 1 meta-content.** "Instructions for development of Design and Troubleshooting Documentation" is a guidance doc for Claude/Tom, not content for a maintainer. Remove from the manual TOC.

6. **Missing weight and balance section.** Standard and important for a maintenance manual.

7. **Scope question to resolve with Tom.** Pages like `flight-controls-fabrication-notes` and `flipping-fuselage` — are we writing a maintenance manual, a build manual, or both? This needs an explicit decision before content is written.

**Plan to resolve:**
- Interview Tom: get an inventory of what avionics and electrical systems are actually installed on the aircraft
- Audit Sections 14 and 16 against that inventory — remove or stub pages for systems not present
- Fill in empty section skeletons (especially Section 6 Inspection)
- Fix duplicate 7.2
- Remove meta-content from Section 1
- Add weight and balance section
- Get explicit scope decision from Tom on fabrication content

## Backlog

### [x] Consider retiring standards files from docs/plans/ (NOTE FROM WRITER 2026-04-16) — resolved 2026-04-16

**Decision:** Keep AR copies. AR is the working copy; WR is the published snapshot — same pattern as `architecture_decisions.md` / `manual-standards.md`. Removing the AR copies would invert this pattern and make session startup dependent on OtterWiki availability.

**Drift prevention:** Two-layer approach added to `claude/roles/architect.md`:
1. When Architect modifies a standards file, create a Writer task to re-publish the corresponding WR page immediately.
2. Pre-commit drift check: compare `git log -1` dates on AR files vs WR files; create a Writer task if AR is newer and no task already exists.

---

### [x] Define workflow for the `input/` directory (NOTE FROM WRITER 2026-04-16) — resolved 2026-04-16

**Decision:** Writer's proposed workflow adopted with one addition:

- `input/architect_todo/` — Architect checks at session startup, adds tasks to `architect_todo.md`, deletes input file
- `input/writer_todo/` — Writer checks at session startup, adds tasks to `writer_todo.md`, deletes input file
- `input/feedback/` — Writer checks at session startup, processes feedback (updates content), deletes input file; escalates to Architect if feedback has structural implications
- Processed files are deleted (not archived) — git history preserves them if needed
- `input/` documented in `claude/project_status.md` directory structure
- Role startup reads updated in `claude/roles/architect.md` and `claude/roles/writer.md`

---

## Completed
