## Project Overview

**PDFindexer** is a simple python program that will read a PDF file of FAA 43.13, create appropriate index files and appropriate files of the content.

## Project Status

This repository is in active implementation.  

### Current Structure

- `kicad2wireBOM/` - Main package implementation
- `tests/` - Test suite with fixtures
- `docs/plans/` - Design specifications and implementation plans
  - `required_from_tom.md` - Items such as test fixtures needed from Tom
  - `architect_todo.md` - place for Programmer or Tom to give feedback to the architect
  - `programmer_todo.md` - place where architect gives direction to programmer on what steps to tackle next
- `docs/acronyms.md` - list of acronyms or terms relevant to this project
- `docs/references/` - Reference materials (READ ONLY)

## Documentation Management

### Reference Materials
- All files in `docs/references/` are READ ONLY. NEVER modify these files.
- These contain source materials like MIL-SPEC documents and Aeroelectric Connection excerpts.

## Environment Setup

A Python virtual environment is configured at `venv/`:

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run specific test file
pytest tests/test_example.py

# Run tests with verbose output
pytest -v

# Run tests and show print statements
pytest -s
```