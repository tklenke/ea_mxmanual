# Architect Todo

## pdf_page_to_svg.py — PDF diagram extraction tool (2026-04-18)

**What was done:** A standalone script `tools/pdf_page_to_svg.py` was created to extract
a single PDF page as an editable SVG using PyMuPDF (`fitz`). Unlike `pdftocairo`, PyMuPDF
preserves text as real `<text>/<tspan>` elements with readable content, making the SVG
easy to edit by y-coordinate filtering or content.

The script was used to extract Figure 2-1 (G3X system architecture diagram) from
`docs/references/tds/GarminG3XInstallationManual_az.pdf` page 25. The resulting SVG
(77KB vs 479KB for pdftocairo) lives at `docs/references/diagrams/g3x-system-architecture.svg`
in the AR.

**Location:** `tools/scripts/pdf_page_to_svg.py` — moved from tools/ root to scripts/ (2026-04-18).

**Requires pymupdf:** `pip install pymupdf`. A venv was set up at `/tmp/pdfenv/` during
the session that created this — ephemeral, not committed. Document venv setup if this
tool gets its own directory.

---

## PDFindexer

### Status: Complete (2026-04-18)

All phases complete, 64 tests passing. Index validated in production use by CMW.
README reviewed and accepted. Design documented in `PDFindexer/docs/plans/design.md`.

---

## wikiCheck

### Status: Complete (2026-04-18)

All phases complete, 103 tests passing. Design documented in `wikiCheck/docs/plans/design.md`.
