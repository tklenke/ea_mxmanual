# EA MX Manual

A maintenance manual system for experimental aircraft, built on Claude Code and Otterwiki.

The manual itself lives in a separate wiki repository (the "WR") as a flat collection of
Markdown files served by Otterwiki. This repository (the "AR") holds everything that
supports writing the manual: planning documents, content standards, reference materials,
source documents, and the Claude role definitions that define how the AI assistant
behaves.

---

## What This System Is

Most homebuilders end up with maintenance notes scattered across binders, sticky notes,
and memory. This system replaces that with a searchable, versioned maintenance manual —
written collaboratively between you and an AI assistant (Claude Code), and published
through Otterwiki so it reads like a real manual.

The AI doesn't write the manual for you. It interviews you, researches your source
materials, drafts content, and flags gaps. You provide the knowledge. The result is
a manual that reflects what you actually know about your aircraft.

---

## The Workflow

There are three roles, each handled by Claude in a separate session:

**Architect** — Plans the structure. Defines sections, page hierarchy, and content scope.
You work with the Architect when making structural decisions: what goes where, how sections
are organized, what belongs in the manual vs. the POH.

**Writer** — Writes the content. Interviews you for knowledge you hold in your head,
researches your reference materials (FAA documents, manufacturer specs, etc.), drafts
pages, and flags anything it cannot verify. You feed the Writer new tasks by dropping
a text file into the `input/writer_todo/` directory before starting a session.

**Reviewer** — Reviews completed pages with you. Works through each page interactively,
fixing minor issues in-session. Flags anything that needs significant rework and logs it
as a future Writer task. Marks pages Approved in the review log after you sign off.

A typical flow:

1. You drop a task file into `input/writer_todo/` describing what you want written
2. Start Claude Code, select **Writer** role
3. Writer picks up the task, interviews you if needed, drafts the page
4. When enough pages are ready, start a **Reviewer** session
5. Reviewer works through pages with you, fixes minor issues, logs larger ones
6. Pages are committed to the wiki when you approve them

---

## What You Need

- **Claude Code** — Anthropic's AI coding assistant (subscription required)
- **Otterwiki** — a lightweight git-backed wiki server (open source, self-hosted)
- **Python 3** — for the wikiCheck integrity tool
- Two git repositories: one for this planning content (AR), one for your wiki pages (WR)

Detailed setup instructions are not included here — the system is designed for builders
willing to figure out tooling. If there's demand for a setup guide, it can be added.

---

## Adapting This for Your Aircraft

The content standards, section structure, and reference materials in this repo are
specific to N657CZ (a Cozy Mark IV). To adapt the system for your aircraft:

1. Fork or copy this repository
2. Replace `docs/references/` with your aircraft's source documents
3. Revise `docs/plans/toc_structure.md` to match your aircraft's systems
4. Update `CLAUDE.md` and the `claude/` role files to reference your aircraft
5. Start an **Architect** session and let Claude help you build out the structure

The writing standards, role definitions, and workflow are aircraft-agnostic and can be
used as-is.

---

## Repository Layout

```
ea_mxmanual/          ← this repo (AR)
├── claude/           ← role definitions and project context for Claude
├── docs/
│   ├── plans/        ← TOC, content plans, writing standards, task tracking
│   ├── notes/        ← review log, wikiCheck known issues
│   └── references/   ← source documents (FAA ACs, manufacturer specs) — read only
├── input/            ← drop tasks here between sessions
│   ├── writer_todo/
│   ├── architect_todo/
│   └── feedback/
└── tools/
    └── wikiCheck/    ← wiki integrity checker (broken links, orphan pages, review status)

N657CZDashTwo/        ← wiki repo (WR) — your Otterwiki content
    *.md              ← one file per manual page
```
