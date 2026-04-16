## File and Section Naming

Otterwiki uses lowercase hyphenated page names. Follow this convention exactly:
- Page names: `lowercase-hyphenated` (e.g., `brake-system-fluid-choice`)
- Wiki links: `[[page-name|Display Text]]`
- Section headings: Title Case for top-level, sentence case for sub-sections

Names must describe the content, not the document's history or status:
- NEVER use temporal or status terms in names (e.g., "new-procedure", "updated-checklist", "revised-spec")
- Names should be evergreen — valid regardless of when they are read


## Writing Style

- Write in the present tense. Content should be evergreen — valid regardless of when it is read.
- NEVER reference the document's own history ("this section was updated to...", "previously...", "as of this revision...")
- NEVER use marketing or evaluative language ("improved", "better", "enhanced")
- Use active voice and imperative mood for procedures (e.g., "Torque the bolt to 25 in-lbs" not "The bolt should be torqued...")
- Define acronyms on first use. Add new terms to `docs/acronyms.md`.
- Be specific. Vague guidance is dangerous in a maintenance manual. If you don't have a specific value, say so explicitly and flag it for research.


## Version Control

- If the project isn't in a git repo, STOP and ask permission to initialize one.
- YOU MUST STOP and ask how to handle uncommitted changes or untracked files when starting work. Suggest committing existing work first.
- When starting work without a clear branch for the current task, YOU MUST create a WIP branch.
- YOU MUST track all non-trivial changes in git.
- YOU MUST commit frequently throughout the writing process, even if high-level tasks are not yet done.
- NEVER SKIP, EVADE OR DISABLE A PRE-COMMIT HOOK
- NEVER use `git add -A` unless you've just done a `git status` — don't add unintended files to the repo.


## Issue Tracking

- You MUST use your TodoWrite tool to keep track of what you're doing.
- You MUST NEVER discard tasks from your TodoWrite todo list without Tom's explicit approval.


## Learning and Memory Management
NOTE: Journaling functionality may be added in the future to help track research findings, failed approaches, architectural decisions, and user preferences across conversations. This section is a placeholder for that capability.


## Reference Materials

All reference materials are in `docs/references/` and are **READ ONLY**. Never modify these files.

### Available References

- **`docs/references/AC43_13/`** — FAA Advisory Circular 43.13, *Acceptable Methods, Techniques, and Practices — Aircraft Inspection and Repair*. Files are named by chapter and page (e.g., `ch01_p001.txt`). Appendices are also available. This is the baseline reference for general aircraft maintenance practices.

- **`docs/references/tds/`** — Manufacturer Technical Data Sheets for specific products used on the aircraft (e.g., sealants, adhesives, thread compounds). These are product-specific documents from the manufacturer.

### How to Use References

When writing content that involves a procedure, specification, or value:

1. Check `docs/references/AC43_13/` for the relevant chapter and page
2. Check `docs/references/tds/` for any applicable manufacturer TDS
3. If both sources apply, they must both be cited

### Source Hierarchy and Conflicts

**When AC 43.13 and a manufacturer TDS conflict, the TDS takes precedence.**

The manufacturer's Technical Data Sheet specifies requirements for their specific product. AC 43.13 provides general guidance that may not account for product-specific requirements.

When a TDS supersedes AC 43.13:
- Follow the TDS
- Add a source conflict NOTE to the content (see `docs/plans/standards.md` for NOTE format)
- Cite both sources — the TDS that was followed and the AC 43.13 section it supersedes

### Citing Sources

All specific values, procedures, and specifications MUST include a citation. Use this format inline:

- AC 43.13 citation: `(AC 43.13, ch01_p001)`
- TDS citation: `(Permatex Thread Sealant TDS)`

If a value cannot be traced to a source in `docs/references/`, flag it with `@@TOM:` for resolution rather than presenting it without attribution.
