"""Multi-attribute document deduplication engine for scientific literature."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from sqlalchemy import func, or_, select

from kb.storage.database import DatabaseManager
from kb.storage.models import Document


def normalize_doi(doi: str | None) -> str | None:
    """Normalizes a DOI string by removing URL prefixes and casing."""
    if not doi:
        return None
    cleaned = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"^doi:\s*", "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip().lower() or None


def normalize_openalex_id(openalex_id: str | None) -> str | None:
    """Normalizes an OpenAlex identifier to canonical short form (e.g. 'W1234567890')."""
    if not openalex_id:
        return None
    cleaned = openalex_id.strip().split("/")[-1].upper()
    return cleaned if cleaned.startswith("W") else None


def normalize_arxiv_id(arxiv_id: str | None) -> str | None:
    """Extracts and normalizes standard arXiv ID (e.g. '2104.05678')."""
    if not arxiv_id:
        return None
    match = re.search(r"(\d{4}\.\d{4,5})", arxiv_id)
    return match.group(1) if match else None


def normalize_title(title: str | None) -> str:
    """Normalizes document title for robust string comparison."""
    if not title:
        return ""
    # Convert to lowercase, replace non-alphanumeric chars with spaces, collapse spaces
    cleaned = re.sub(r"[^\w\s]", " ", title.lower())
    return " ".join(cleaned.split())


@dataclass(frozen=True)
class DuplicateMatch:
    """Result of a multi-attribute duplicate evaluation."""

    is_duplicate: bool
    match_type: str | None = None
    matched_citekey: str | None = None
    matched_title: str | None = None
    document_id: str | None = None
    details: str | None = None


class DuplicateResolver:
    """Evaluates candidate documents against database records using multi-attribute matching."""

    def __init__(self, db_manager: DatabaseManager) -> None:
        """Initializes the DuplicateResolver with a database manager."""
        self.db = db_manager

    async def check_candidate(
        self,
        citekey: str | None = None,
        doi: str | None = None,
        openalex_id: str | None = None,
        arxiv_id: str | None = None,
        title: str | None = None,
        authors: list[str] | None = None,
        year: int | None = None,
    ) -> DuplicateMatch:
        """Checks if a candidate paper already exists in the database.

        Evaluation order:
        1. Exact citekey match
        2. Canonical DOI match
        3. Canonical OpenAlex ID match
        4. Canonical arXiv ID match
        5. Normalized title match (with author/year validation for short titles)
        """
        clean_doi = normalize_doi(doi)
        clean_openalex = normalize_openalex_id(openalex_id)
        clean_arxiv = normalize_arxiv_id(arxiv_id)
        clean_title = normalize_title(title)

        async with self.db.get_session() as session:
            # 1. Primary identifier check
            conditions: list[Any] = []
            if citekey:
                conditions.append(Document.citekey == citekey.strip())
            if clean_doi:
                conditions.append(func.lower(Document.doi) == clean_doi)
                conditions.append(Document.doi.ilike(f"%{clean_doi}"))
            if clean_openalex:
                conditions.append(Document.openalex_id.ilike(f"%{clean_openalex}"))
            if clean_arxiv:
                conditions.append(Document.arxiv_id.ilike(f"%{clean_arxiv}%"))

            if conditions:
                stmt = select(Document).where(or_(*conditions)).limit(1)
                existing = (await session.execute(stmt)).scalar_one_or_none()
                if existing:
                    match_type = "citekey"
                    if clean_doi and existing.doi and clean_doi in existing.doi.lower():
                        match_type = "doi"
                    elif clean_openalex and existing.openalex_id and clean_openalex in existing.openalex_id.upper():
                        match_type = "openalex_id"
                    elif clean_arxiv and existing.arxiv_id and clean_arxiv in existing.arxiv_id:
                        match_type = "arxiv_id"

                    return DuplicateMatch(
                        is_duplicate=True,
                        match_type=match_type,
                        matched_citekey=existing.citekey,
                        matched_title=existing.title,
                        document_id=existing.id,
                        details=f"Document '{existing.citekey}' already exists in database (matched via {match_type}).",
                    )

            # 2. Normalized title check
            if clean_title and len(clean_title) >= 10:
                # Direct equality check on normalized title
                stmt_title = select(Document).where(
                    func.lower(Document.title) == (title.strip().lower() if title else "")
                ).limit(5)
                candidates = (await session.execute(stmt_title)).scalars().all()

                if not candidates:
                    # Test broader token prefix matching
                    first_words = " ".join(clean_title.split()[:4])
                    if len(first_words) >= 12:
                        stmt_prefix = select(Document).where(
                            Document.title.ilike(f"%{first_words}%")
                        ).limit(10)
                        candidates = (await session.execute(stmt_prefix)).scalars().all()

                for cand in candidates:
                    cand_norm = normalize_title(cand.title)
                    if cand_norm == clean_title:
                        # Year check if both candidate and document have published years
                        if year is not None and cand.year is not None and abs(cand.year - year) > 2:
                            continue

                        # Exact normalized match
                        if len(clean_title) < 25 and authors and cand.authors:
                            # Require at least one author last name match for short titles
                            cand_surnames = {
                                a.split()[-1].lower() for a in cand.authors if a
                            }
                            input_surnames = {
                                a.split()[-1].lower() for a in authors if a
                            }
                            if not cand_surnames.intersection(input_surnames):
                                continue

                        return DuplicateMatch(
                            is_duplicate=True,
                            match_type="normalized_title",
                            matched_citekey=cand.citekey,
                            matched_title=cand.title,
                            document_id=cand.id,
                            details=f"Matched normalized title with '{cand.citekey}': '{cand.title}'",
                        )

        return DuplicateMatch(is_duplicate=False)

    async def filter_candidates(
        self,
        candidates: list[dict[str, Any]],
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        """Splits candidate list into (new_candidates, duplicate_candidates)."""
        new_list: list[dict[str, Any]] = []
        dup_list: list[dict[str, Any]] = []

        for cand in candidates:
            match = await self.check_candidate(
                citekey=cand.get("citekey"),
                doi=cand.get("doi"),
                openalex_id=cand.get("openalex_id") or cand.get("short_id"),
                arxiv_id=cand.get("arxiv_id"),
                title=cand.get("title"),
                authors=cand.get("authors"),
                year=cand.get("year"),
            )
            if match.is_duplicate:
                cand_copy = dict(cand)
                cand_copy["duplicate_reason"] = match.details
                dup_list.append(cand_copy)
            else:
                new_list.append(cand)

        return new_list, dup_list
