# PDFindexer Design

## Purpose

Extract the content of FAA AC 43.13-1B ("Acceptable Methods, Techniques, and Practices -
Aircraft Inspection and Repair") into a structured set of plain text files consumable by a
Claude instance assisting with the ea_mxmanual project. The consumer (Claude) looks up
relevant FAA guidance by paragraph when writing aircraft-specific maintenance procedures.

## Source Document

- File: `docs/references/ac_43.13.pdf`
- Type: Born-digital PDF (real selectable text, no OCR needed)
- Size: 600+ pages, 11 chapters, ~4 sections per chapter
- Layout: Two-column body text with embedded figures (images) and tables (PDF table objects)
- Page numbering: Chapter-relative format (e.g., Page 1-1, Page 1-2)
- Paragraph numbering: Chapter-relative format (e.g., 1-1, 1-2, 2-1, 2-2)
- TOC: Pages 2 through 34

## Output Location

`data/` within the PDFindexer repo. Tom will copy the output to the ea_mxmanual project
(`docs/references/FAA43_13/`) manually after the program runs successfully.

## Output Structure

```
data/
  index.txt         <- master index; Claude reads this first to identify relevant paragraphs
  ch01_p001.txt     <- paragraph 1-1
  ch01_p002.txt     <- paragraph 1-2
  ...
  ch11_p###.txt
```

### index.txt Format

Plain text. Optimized for Claude to scan quickly and identify relevant paragraphs without
opening any content files.

```
AC 43.13-1B — Acceptable Methods, Techniques, and Practices

CHAPTER 1: WOOD STRUCTURE

  SECTION 1: MATERIALS AND PRACTICES
    1-1  General [ch01_p001.txt]
    1-2  Woods [ch01_p002.txt]
    1-3  Modified Wood Products [ch01_p003.txt]
    1-4  Adhesives [ch01_p004.txt]
    ...

  SECTION 2: HEALTH AND SAFETY
    1-18  General [ch01_p018.txt]
    ...

CHAPTER 2: ...
```

### Paragraph File Format

Plain text (`.txt`). No markdown syntax. Optimized to minimize tokens while preserving
all content Claude needs.

```
AC 43.13-1B  Chapter 1: Wood Structure  Section 1: Materials and Practices

1-2. WOODS.

  a. Quality of Wood.  All wood and plywood used in the repair of aircraft structures
  should be of aircraft quality...

  [TABLE 1-1, p.1-2]

  b. Substitution of Original Wood.  The wood species used to repair a part should
  be the same as that of the original whenever possible...

  [FIG 1-1, p.1-1]
```

Header line on each file gives Claude context without requiring it to remember which
file it opened.

## Token Optimization Decisions

1. Plain text files, not markdown — no syntax overhead
2. Page headers/footers stripped — "9/8/98  AC 43.13-1B" and "Par X-X  Page X-X"
   repeat on every page and are pure noise
3. Compact figure/table markers — [FIG 1-1, p.1-1] and [TABLE 1-1, p.1-2]
4. Paragraph titles in index — Claude determines relevance from index alone without
   opening content files; typical query reads index once + 1-3 paragraph files
5. Short filenames — ch01_p001.txt not ch01_p001_general_wood_quality.txt;
   titles are already in the index
6. Paragraph-level granularity — finer than section-level so Claude reads only the
   specific paragraphs it needs rather than entire sections

## Processing Pipeline

### Phase 1: TOC Extraction (pages 2-34)

Parse the TOC to build the complete expected structure:
- Chapter numbers and titles
- Section numbers and titles per chapter
- Paragraph numbers and titles per section
- Page numbers (used for validation and index)

The TOC is the authoritative source of structure. Content extraction is guided by this
structure rather than trying to detect headings from body text alone.

### Phase 2: Content Extraction (pages 35+)

Walk pages sequentially. For each page:
1. Strip header (top of page: date + document number) and footer (bottom: Par X-X / Page X-X)
2. Extract text with column awareness (see Two-Column Handling below)
3. Detect paragraph boundaries using paragraph number markers (e.g., "1-2.", "1-3.")
4. Detect figures using pdfplumber image detection; insert [FIG X-X, p.X-X] marker
5. Detect tables using pdfplumber table extraction; insert [TABLE X-X, p.X-X] before
   table text content (tables are extracted as text, not skipped)

### Phase 3: Output Writing

For each paragraph accumulated during Phase 2:
- Write ch##_p###.txt with single-line header + content
- Paragraph number is zero-padded to 3 digits for consistent sorting

After all paragraphs written:
- Write index.txt from TOC structure with filenames filled in

## Two-Column Handling

The body text uses a two-column layout. Naive pdfplumber extraction interleaves columns.

Approach: Use pdfplumber `extract_words()` to get words with bounding boxes. For each
page, determine the column midpoint (approximately x=306 for a standard letter page).
Sort words into left column (x < midpoint) and right column (x >= midpoint), each sorted
top-to-bottom by y coordinate. Reconstruct text left column first, then right column.

## Library

**pdfplumber** — chosen for:
- Column-aware extraction via `extract_words()` with bounding boxes
- Built-in table detection and extraction
- Image/figure detection via `page.images`
- Pure Python, well-maintained

## Figure Handling

pdfplumber exposes `page.images` — a list of image objects with bounding boxes.
When an image is detected on a page, determine its y-position and insert the figure
marker at the appropriate point in the reconstructed text flow. The caption text
(e.g., "FIGURE 1-1. Relative shrinkage...") immediately follows the image in the PDF
and will be extracted as normal text.

## Table Handling

pdfplumber's `page.extract_tables()` returns table data as lists of rows/cells.
Tables are rendered as plain text (space-separated columns) with a [TABLE X-X, p.X-X]
marker preceding them. The table title (e.g., "TABLE 1-1. Selection and Properties...")
appears above the table in the PDF and will be extracted as normal text.

## Paragraph Numbering

Paragraphs are numbered chapter-relative (1-1 through 1-N for chapter 1, 2-1 through
2-N for chapter 2, etc.). Filenames use absolute sequential numbering within each
chapter, zero-padded to 3 digits: ch01_p001.txt, ch01_p002.txt, etc.

The paragraph number from the document (e.g., "1-36") is preserved in the file content.

## Known Challenges

- Reserved paragraph ranges (e.g., "1-12. 1-17. [RESERVED.]") — treat as a single
  short paragraph with content "[RESERVED]"
- Sub-paragraphs (a., b., c.) are part of the parent paragraph, not separate files
- Figure captions may be on a different page than the figure itself (handle gracefully)
- Some paragraphs may span multiple pages

## Out of Scope

- Image extraction (figures are noted with markers, not extracted as image files)
- Hyperlinks or cross-references
- Any output format other than plain text
