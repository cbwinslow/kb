"""Unit tests for OpenAlex bibliographic client and resolution."""

from __future__ import annotations

import uuid

import httpx
import pytest
from sqlalchemy import select

from kb.cli import async_enrich_openalex
from kb.enrich.openalex import OpenAlexClient
from kb.storage.database import DatabaseManager
from kb.storage.models import Document


class MockOpenAlexTransport(httpx.AsyncBaseTransport):
    """Hermetic mock transport simulating OpenAlex responses for unit tests."""

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        url_str = str(request.url)

        # 1. Single work by ID
        if "/works/W1533576069" in url_str:
            payload = {
                "id": "https://openalex.org/W1533576069",
                "title": "A Derivation of the Pythagorean Won-Loss Formula in Baseball",
                "doi": "https://doi.org/10.1080/09332480.2007.10722831",
                "publication_year": 2007,
                "cited_by_count": 50,
                "topics": [
                    {
                        "id": "https://openalex.org/T10123",
                        "display_name": "Sports Analytics and Performance",
                        "score": 0.99,
                        "subfield": {"display_name": "Applied Mathematics"},
                        "field": {"display_name": "Mathematics"},
                        "domain": {"display_name": "Physical Sciences"},
                    }
                ],
                "referenced_works": [
                    "https://openalex.org/W1111111111",
                    "https://openalex.org/W2222222222",
                ],
                "related_works": [
                    "https://openalex.org/W3333333333",
                ],
                "authorships": [
                    {"author": {"display_name": "Steven J. Miller"}},
                ],
                "best_oa_location": {
                    "landing_page_url": "https://arxiv.org/abs/math/0509698",
                    "pdf_url": "https://arxiv.org/pdf/math/0509698.pdf",
                },
            }
            return httpx.Response(200, json=payload, request=request)

        # 2. DOI lookup
        if "https://doi.org/10.1080/09332480.2007.10722831" in url_str:
            payload = {
                "id": "https://openalex.org/W1533576069",
                "title": "A Derivation of the Pythagorean Won-Loss Formula in Baseball",
                "doi": "https://doi.org/10.1080/09332480.2007.10722831",
                "publication_year": 2007,
                "cited_by_count": 50,
                "topics": [],
                "referenced_works": [],
                "related_works": [],
                "authorships": [],
            }
            return httpx.Response(200, json=payload, request=request)

        # 3. Citation query (filter=cites:W1533576069)
        if "cites" in url_str and "W1533576069" in url_str:
            payload = {
                "results": [
                    {
                        "id": "https://openalex.org/W2727607080",
                        "title": "Sports Data Mining: Predicting Results for College Football",
                        "publication_year": 2014,
                        "cited_by_count": 83,
                        "topics": [],
                        "referenced_works": [],
                        "related_works": [],
                        "authorships": [],
                    }
                ]
            }
            return httpx.Response(200, json=payload, request=request)

        # 4. Title search
        if "search=Steven+J.+Miller" in url_str or "search=A+Derivation" in url_str:
            payload = {
                "results": [
                    {
                        "id": "https://openalex.org/W1533576069",
                        "title": "A Derivation of the Pythagorean Won-Loss Formula in Baseball",
                        "publication_year": 2007,
                        "cited_by_count": 50,
                        "topics": [{"id": "T1", "display_name": "Sports Analytics", "score": 0.95}],
                        "referenced_works": [],
                        "related_works": [],
                        "authorships": [{"author": {"display_name": "Steven J. Miller"}}],
                    }
                ]
            }
            return httpx.Response(200, json=payload, request=request)

        # 5. Missing work (404)
        if "not_found" in url_str:
            return httpx.Response(404, json={"error": "Not found"}, request=request)

        # Default empty response
        return httpx.Response(200, json={"results": []}, request=request)


@pytest.mark.asyncio
async def test_openalex_get_work() -> None:
    """Verifies parsing of OpenAlex work entity, topics, authors, and references."""
    client = OpenAlexClient(transport=MockOpenAlexTransport())
    work = await client.get_work("W1533576069")

    assert work is not None
    assert work.short_id == "W1533576069"
    assert work.title == "A Derivation of the Pythagorean Won-Loss Formula in Baseball"
    assert work.publication_year == 2007
    assert work.cited_by_count == 50
    assert len(work.topics) == 1
    assert work.topics[0]["name"] == "Sports Analytics and Performance"
    assert work.authors == ["Steven J. Miller"]
    assert len(work.referenced_works) == 2


@pytest.mark.asyncio
async def test_openalex_resolve_by_doi_and_title() -> None:
    """Verifies resolve_work by DOI and fallback title search."""
    client = OpenAlexClient(transport=MockOpenAlexTransport())

    # 1. Resolve by DOI
    work_doi = await client.resolve_work(doi="10.1080/09332480.2007.10722831")
    assert work_doi is not None
    assert work_doi.short_id == "W1533576069"

    # 2. Resolve by title and author
    work_title = await client.resolve_work(
        title="A Derivation of the Pythagorean Won-Loss Formula in Baseball",
        authors=["Steven J. Miller"],
    )
    assert work_title is not None
    assert work_title.short_id == "W1533576069"

    # 3. Non-existent identifier
    work_none = await client.resolve_work(doi="not_found_doi")
    assert work_none is None


@pytest.mark.asyncio
async def test_openalex_get_citations() -> None:
    """Verifies retrieving citing papers for a work."""
    client = OpenAlexClient(transport=MockOpenAlexTransport())
    citations = await client.get_citations("W1533576069", limit=5)

    assert len(citations) == 1
    citing = citations[0]
    assert citing.short_id == "W2727607080"
    assert "Sports Data Mining" in citing.title
    assert citing.cited_by_count == 83


@pytest.mark.asyncio
async def test_async_enrich_openalex() -> None:
    """Verifies that async_enrich_openalex queries OpenAlex and updates Document records."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_{db_id}?mode=memory&cache=shared&uri=true"
    manager = DatabaseManager(database_url=url, echo=False)
    await manager.init_db()

    async with manager.get_session() as session:
        doc = Document(
            citekey="miller2005",
            title="A Derivation of the Pythagorean Won-Loss Formula in Baseball",
            authors=["Steven J. Miller"],
            year=2005,
            doi="10.1080/09332480.2007.10722831",
            file_path="data/fixtures/miller2005.pdf",
        )
        session.add(doc)
        await session.flush()

    mock_client = OpenAlexClient(transport=MockOpenAlexTransport())
    code = await async_enrich_openalex(
        citekey="miller2005",
        client=mock_client,
        manager=manager,
    )
    assert code == 0

    async with manager.get_session() as session:
        res = await session.execute(select(Document).where(Document.citekey == "miller2005"))
        updated_doc = res.scalar_one()
        assert updated_doc.openalex_id == "https://openalex.org/W1533576069"
        assert updated_doc.citation_count == 50

    await manager.close()

