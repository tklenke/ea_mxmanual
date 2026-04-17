# ABOUTME: Extracts Otterwiki internal link slugs from page content.
# ABOUTME: Handles [[slug]] and [[Display Text|slug]] link formats.

import re

_LINK_RE = re.compile(r'\[\[(?:[^\]|]+\|)?([^\]|]+)\]\]')


def extract_links(content: str) -> list[str]:
    return _LINK_RE.findall(content)
