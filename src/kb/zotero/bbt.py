"""Better BibTeX citation key parser and fallback generator."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

# Better BibTeX citation key regex patterns in Zotero Extra field
BBT_EXTRA_PATTERNS = [
    re.compile(r"Citation Key:\s*([a-zA-Z0-9_\-:]+)", re.IGNORECASE),
    re.compile(r"bibtex:\s*([a-zA-Z0-9_\-:]+)", re.IGNORECASE),
]

# Standard BibTeX entry pattern: @type{citekey,
BIBTEX_ENTRY_RE = re.compile(
    r"@(?P<type>[a-zA-Z]+)\s*\{\s*(?P<citekey>[a-zA-Z0-9_\-:]+)\s*,\s*(?P<body>[\s\S]*?)(?=\n\s*@|\Z)",
    re.MULTILINE,
)

# BibTeX field pattern: fieldname = {value} or "value"
BIBTEX_FIELD_RE = re.compile(
    r"(?P<field>[a-zA-Z]+)\s*=\s*[\{\"](?P<value>[\s\S]*?)[\}\"],?",
)

STOPWORDS = {"a", "an", "the", "in", "on", "of", "and", "for", "to", "with", "by", "at"}


class BetterBibTeXParser:
    """Parses Better BibTeX citekeys from Zotero metadata and .bib files."""

    def extract_citekey_from_extra(self, extra_text: str) -> str | None:
        """Extracts citekey from Zotero item 'Extra' field if present."""
        if not extra_text:
            return None

        for pattern in BBT_EXTRA_PATTERNS:
            match = pattern.search(extra_text)
            if match:
                return match.group(1).strip()
        return None

    def generate_fallback_citekey(
        self,
        first_author: str,
        year: int | None,
        title: str,
    ) -> str:
        """Generates a canonical fallback citekey: [author][year][first_word].

        Example: 'Steven J. Miller', 2005, 'A Derivation of Pythagorean Expectation'
                 -> 'miller2005derivation'
        """
        # Extract last name: take the last word from first_author
        parts = [p.strip() for p in first_author.strip().split() if p.strip()]
        last_name = parts[-1] if parts else "unknown"
        author_name = self._clean_token(last_name)

        # Year part
        year_str = str(year) if year is not None else ""

        # First substantive word of title
        title_tokens = [
            self._clean_token(w)
            for w in title.split()
            if self._clean_token(w) and self._clean_token(w) not in STOPWORDS
        ]
        title_word = title_tokens[0] if title_tokens else "doc"

        return f"{author_name}{year_str}{title_word}".lower()

    def parse_bibtex_file(self, file_or_content: str | Path) -> dict[str, dict[str, str]]:
        """Parses a .bib file or BibTeX string into a dictionary keyed by citekey.

        Returns:
            Dict mapping citekey -> {field: value, ...}
        """
        if isinstance(file_or_content, Path):
            content = file_or_content.read_text(encoding="utf-8")
        elif "\n" not in file_or_content and Path(file_or_content).exists():
            content = Path(file_or_content).read_text(encoding="utf-8")
        else:
            content = file_or_content

        entries: dict[str, dict[str, str]] = {}
        for match in BIBTEX_ENTRY_RE.finditer(content):
            entry_type = match.group("type").strip().lower()
            citekey = match.group("citekey").strip()
            body = match.group("body")

            fields: dict[str, str] = {"_type": entry_type, "citekey": citekey}
            for field_match in BIBTEX_FIELD_RE.finditer(body):
                k = field_match.group("field").strip().lower()
                v = field_match.group("value").strip()
                fields[k] = v

            entries[citekey] = fields

        return entries

    @staticmethod
    def _clean_token(s: str) -> str:
        """Normalizes text by removing non-alphanumeric characters and diacritics."""
        norm = unicodedata.normalize("NFKD", s)
        ascii_text = norm.encode("ASCII", "ignore").decode("utf-8")
        return re.sub(r"[^a-zA-Z0-9]", "", ascii_text).lower()
