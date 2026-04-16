# ABOUTME: Tests for AppendixExtractor — verifies plain-text extraction of appendix pages.
# ABOUTME: Uses a 2-page fixture covering PDF pages 633-634 (start of Appendix 1: Glossary).

import pytest
import pdfplumber
from pdfindexer.appendix_extractor import extract_appendix

FIXTURE = "tests/fixtures/ac_43_13_appendix_excerpt.pdf"
TITLE = "Appendix 1: Glossary"


@pytest.fixture(scope="module")
def appendix_text():
    with pdfplumber.open(FIXTURE) as pdf:
        # Fixture has 2 pages; treat as pages 1-2 (1-indexed)
        yield extract_appendix(pdf, start_page=1, end_page=2, title=TITLE)


def test_returns_string(appendix_text):
    assert isinstance(appendix_text, str)
    assert len(appendix_text) > 100


def test_header_line_correct(appendix_text):
    first_line = appendix_text.split("\n")[0]
    assert first_line == "AC 43.13-1B  Appendix 1: Glossary"


def test_blank_line_after_header(appendix_text):
    lines = appendix_text.split("\n")
    assert lines[1] == ""


def test_known_glossary_term_present(appendix_text):
    assert "acetylene" in appendix_text


def test_known_glossary_term_bond_present(appendix_text):
    # "bond" appears on page 2 of the fixture
    assert "bond" in appendix_text


def test_soft_hyphens_joined(appendix_text):
    # "mid\xad\nway" should become "midway"
    assert "midway" in appendix_text
    assert "\xad" not in appendix_text


def test_regular_hyphens_in_compounds_preserved(appendix_text):
    # "low-impedance" is a genuine compound — hyphen must NOT be stripped
    assert "low-impedance" in appendix_text


def test_pua_leader_characters_removed(appendix_text):
    assert "\uf8e7" not in appendix_text


def test_in_pdf_appendix_title_stripped(appendix_text):
    # "APPENDIX 1. GLOSSARY" should not appear (we add our own header)
    assert "APPENDIX 1. GLOSSARY" not in appendix_text


def test_body_content_starts_after_blank_line(appendix_text):
    lines = appendix_text.split("\n")
    # Line 2 (index 2) should be non-empty body text, not the in-PDF title
    assert lines[2]  # non-empty
    assert not lines[2].startswith("APPENDIX")
