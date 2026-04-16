# ABOUTME: Extracts appendix content from AC 43.13-1B into plain text strings.
# ABOUTME: Each appendix is extracted as-is (no paragraph splitting) with a standard header line.

import re

# Match page_extractor's cutoffs so we strip the same header/footer band
_HEADER_CUTOFF = 65
_FOOTER_CUTOFF = 745


def extract_appendix(pdf, start_page, end_page, title):
    """Extract appendix pages from the PDF and return a cleaned plain text string.

    Args:
        pdf: open pdfplumber PDF object
        start_page: 1-indexed first page number of the appendix
        end_page: 1-indexed last page number of the appendix (inclusive)
        title: full appendix title for the header line (e.g., "Appendix 1: Glossary")

    Returns:
        Plain text string: standardized header line, blank line, then appendix body.
    """
    parts = []
    for page in pdf.pages[start_page - 1 : end_page]:
        # Crop out the header/footer band, then extract text preserving column order
        cropped = page.crop((0, _HEADER_CUTOFF, page.width, _FOOTER_CUTOFF))
        text = cropped.extract_text() or ""
        parts.append(text)

    text = "\n".join(parts)
    text = _replace_leaders(text)
    text = _join_hyphens(text)
    text = _strip_appendix_title_lines(text)

    return f"AC 43.13-1B  {title}\n\n" + text.strip() + "\n"


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _replace_leaders(text):
    """Replace runs of leader-dot characters (U+F8E7) with two spaces.

    In the PDF, U+F8E7 encodes dot leaders that separate a term from its
    definition (glossary) or an acronym from its expansion (acronym list).
    Replacing the run with two spaces preserves the term  definition structure.
    """
    return re.sub(r'\uf8e7+', '  ', text)


def _join_hyphens(text):
    """Join words hyphenated across line breaks (regular and soft hyphens)."""
    text = re.sub(r'\xad\n\s*', '', text)    # soft-hyphen line breaks (U+00AD)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)  # regular-hyphen line breaks
    text = text.replace('\xad', '')           # strip any residual soft hyphens
    return text


def _strip_appendix_title_lines(text):
    """Remove in-PDF appendix title lines (e.g., 'APPENDIX 1. GLOSSARY', 'Appendix 1').

    The standardized header is added separately by extract_appendix().
    """
    lines = text.split("\n")
    cleaned = [
        line for line in lines
        if not re.match(r'^APPENDIX\s+\d+[\.\s]', line)
        and not re.match(r'^Appendix\s+\d+\s*$', line)
    ]
    return "\n".join(cleaned)
