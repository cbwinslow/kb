"""Unit tests for multi-attribute document deduplication engine."""

from __future__ import annotations

import uuid

import pytest

from kb.ingest.dedup import (
    DuplicateResolver,
    normalize_arxiv_id,
    normalize_doi,
    normalize_openalex_id,
    normalize_title,
)
from kb.storage.database import DatabaseManager
from kb.storage.models import Document


def test_normalization_utilities() -> None:
    """Verifies identifier and title normalization functions."""
    assert normalize_doi("https://doi.org/10.1007/s12283-020-00334-1") == "10.1007/s12283-020-00334-1"
    assert normalize_doi("http://dx.doi.org/10.1016/j.jbiomech.2023.111890") == "10.1016/j.jbiomech.2023.111890"
    assert normalize_doi("doi: 10.1234/XYZ.99") == "10.1234/xyz.99"
    assert normalize_doi(None) is None

    assert normalize_openalex_id("https://openalex.org/W2128912345") == "W2128912345"
    assert normalize_openalex_id("w42918231") == "W42918231"
    assert normalize_openalex_id("invalid_id") is None
    assert normalize_openalex_id(None) is None

    assert normalize_arxiv_id("http://arxiv.org/abs/2104.05678v2") == "2104.05678"
    assert normalize_arxiv_id("arxiv:2401.12345") == "2401.12345"
    assert normalize_arxiv_id("invalid") is None

    assert normalize_title("Aerodynamics of the Baseball: Spin & Seam Effects!") == "aerodynamics of the baseball spin seam effects"
    assert normalize_title("   Multiple   Spaces   and  Punctuation: -- ") == "multiple spaces and punctuation"


@pytest.mark.asyncio
async def test_duplicate_resolver_citekey_and_ids() -> None:
    """Verifies that DuplicateResolver detects duplicates by citekey, DOI, OpenAlex ID, and arXiv ID."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_dedup_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.get_session() as session:
        doc1 = Document(
            id="doc1",
            citekey="nathan2008physics",
            title="The Physics of Baseball Bat-Ball Collisions",
            authors=["Alan Nathan"],
            doi="10.1119/1.123456",
            arxiv_id="0801.1234",
            openalex_id="W1234567890",
            year=2008,
        )
        session.add(doc1)
        await session.commit()

    resolver = DuplicateResolver(db)

    # 1. Match citekey
    res_cite = await resolver.check_candidate(citekey="nathan2008physics")
    assert res_cite.is_duplicate is True
    assert res_cite.match_type == "citekey"
    assert res_cite.matched_citekey == "nathan2008physics"

    # 2. Match DOI with URL prefix
    res_doi = await resolver.check_candidate(
        citekey="other_citekey_2008",
        doi="https://doi.org/10.1119/1.123456",
    )
    assert res_doi.is_duplicate is True
    assert res_doi.match_type == "doi"

    # 3. Match OpenAlex ID with URI
    res_oa = await resolver.check_candidate(
        citekey="oa_candidate",
        openalex_id="https://openalex.org/W1234567890",
    )
    assert res_oa.is_duplicate is True
    assert res_oa.match_type == "openalex_id"

    # 4. Match arXiv ID with version suffix
    res_arxiv = await resolver.check_candidate(
        citekey="arxiv_cand",
        arxiv_id="http://arxiv.org/abs/0801.1234v2",
    )
    assert res_arxiv.is_duplicate is True
    assert res_arxiv.match_type == "arxiv_id"

    # 5. Non-duplicate
    res_new = await resolver.check_candidate(
        citekey="brand_new_paper_2025",
        doi="10.1000/999999",
        openalex_id="W9999999999",
        arxiv_id="2501.99999",
        title="Novel Biomechanical Modeling of Swing Velocity",
    )
    assert res_new.is_duplicate is False


@pytest.mark.asyncio
async def test_duplicate_resolver_normalized_title() -> None:
    """Verifies that DuplicateResolver matches documents by normalized title across variations."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_dedup_title_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.get_session() as session:
        doc = Document(
            id="doc_title",
            citekey="smith2023pitching",
            title="Bayesian Forecasting of Major League Baseball Pitch Outcomes",
            authors=["Jane Smith", "Bob Jones"],
            year=2023,
        )
        session.add(doc)
        await session.commit()

    resolver = DuplicateResolver(db)

    # Candidate with different citekey and casing/punctuation in title
    res = await resolver.check_candidate(
        citekey="different_slug_2023",
        title="Bayesian Forecasting of Major League Baseball Pitch Outcomes!",
    )
    assert res.is_duplicate is True
    assert res.match_type == "normalized_title"
    assert res.matched_citekey == "smith2023pitching"


@pytest.mark.asyncio
async def test_duplicate_resolver_filter_candidates() -> None:
    """Verifies batch candidate filtering into new and duplicate subsets."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_dedup_batch_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.get_session() as session:
        doc = Document(
            id="doc_exist",
            citekey="existing_key",
            title="Existing Baseball Study",
            doi="10.5555/baseball.1",
        )
        session.add(doc)
        await session.commit()

    resolver = DuplicateResolver(db)

    candidates = [
        {"citekey": "existing_key", "title": "Existing Study"},
        {"citekey": "fresh_key_1", "doi": "10.5555/fresh.1", "title": "Fresh Study 1"},
        {"citekey": "fresh_key_2", "doi": "10.5555/baseball.1", "title": "Existing by DOI"},
        {"citekey": "fresh_key_3", "title": "Fresh Study 3"},
    ]

    new_cands, dup_cands = await resolver.filter_candidates(candidates)
    assert len(new_cands) == 2
    assert [c["citekey"] for c in new_cands] == ["fresh_key_1", "fresh_key_3"]
    assert len(dup_cands) == 2
    assert [c["citekey"] for c in dup_cands] == ["existing_key", "fresh_key_2"]
