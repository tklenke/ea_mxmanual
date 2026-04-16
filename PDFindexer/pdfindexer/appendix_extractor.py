# ABOUTME: Extracts appendix content from AC 43.13-1B into plain text strings.
# ABOUTME: Each appendix is extracted as-is (no paragraph splitting) with a standard header line.

import re
from pdfindexer.page_extractor import extract_page


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
        result = extract_page(page)
        parts.append(result["text"])

    text = "\n".join(parts)
    text = _join_hyphens(text)
    text = _strip_pua_lines(text)
    text = _strip_appendix_title_lines(text)

    return f"AC 43.13-1B  {title}\n\n" + text.strip() + "\n"


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _join_hyphens(text):
    """Join words hyphenated across line breaks (regular and soft hyphens)."""
    text = re.sub(r'\xad\n\s*', '', text)   # soft-hyphen line breaks
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)  # regular-hyphen line breaks
    text = text.replace('\xad', '')          # strip any residual soft hyphens
    return text


def _strip_pua_lines(text):
    """Remove lines containing Private Use Area characters (e.g., leader-dot cross-refs).

    The PDF uses U+F8E7 as leader dots in index cross-reference entries like
    'PTFE\uf8e7\uf8e7\uf8e7\uf8e7a' — these are navigation noise, not glossary content.
    """
    lines = text.split("\n")
    cleaned = [line for line in lines if '\uf8e7' not in line]
    return "\n".join(cleaned)


def _strip_appendix_title_lines(text):
    """Remove the in-PDF appendix title line (e.g., 'APPENDIX 1. GLOSSARY').

    The standardized header is added separately by extract_appendix().
    """
    lines = text.split("\n")
    cleaned = [line for line in lines if not re.match(r'^APPENDIX\s+\d+\.', line)]
    return "\n".join(cleaned)
