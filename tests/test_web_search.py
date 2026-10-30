"""Tests for scholarly web search engine."""

from __future__ import annotations

import unittest.mock as mock

import pytest

from kb.enrich.web_search import ScholarlyWebSearcher, SearchResult

SAMPLE_ARXIV_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2301.01234v1</id>
    <title>Physics-Informed Neural Networks for Trajectory Tracking</title>
    <summary>This paper proposes PINNs for aerodynamic trajectory modeling.</summary>
    <published>2023-01-05T12:00:00Z</published>
    <author>
      <name>John Doe</name>
    </author>
    <author>
      <name>Jane Smith</name>
    </author>
    <arxiv:doi>10.1234/arxiv.2301.01234</arxiv:doi>
    <link title="pdf" href="http://arxiv.org/pdf/2301.01234v1.pdf" type="application/pdf"/>
  </entry>
</feed>
"""

SAMPLE_OPENALEX_JSON = {
    "results": [
        {
            "id": "https://openalex.org/W123456789",
            "display_name": "Aerodynamic Drag of Baseballs in Flight",
            "publication_year": 2021,
            "cited_by_count": 42,
            "doi": "https://doi.org/10.1000/182",
            "authorships": [
                {"author": {"display_name": "Alan Nathan"}}
            ],
            "abstract_inverted_index": {
                "The": [0],
                "drag": [1],
                "coefficient": [2],
                "of": [3],
                "a": [4],
                "baseball": [5],
                "is": [6],
                "measured.": [7]
            },
            "open_access": {
                "oa_url": "https://example.com/baseball_drag.pdf"
            }
        }
    ]
}


@pytest.mark.asyncio
async def test_search_result_model():
    """Verify SearchResult model fields and serialization."""
    res = SearchResult(
        title="Test Paper",
        authors=["Alice", "Bob"],
        year=2024,
        abstract="A test abstract.",
        source="arxiv",
        url="https://arxiv.org/abs/2401.0001",
        pdf_url="https://arxiv.org/pdf/2401.0001.pdf",
        citation_count=10,
        doi="10.1000/test",
        arxiv_id="2401.0001",
    )
    assert res.title == "Test Paper"
    assert len(res.authors) == 2
    assert res.source == "arxiv"
    assert res.year == 2024


@pytest.mark.asyncio
async def test_search_arxiv_mock():
    """Verify arXiv XML parsing into SearchResult objects."""
    searcher = ScholarlyWebSearcher()

    mock_resp = mock.MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = SAMPLE_ARXIV_XML

    with mock.patch("httpx.AsyncClient.get", return_value=mock_resp):
        results = await searcher.search_arxiv("physics trajectory", limit=5)

    assert len(results) == 1
    r = results[0]
    assert r.title == "Physics-Informed Neural Networks for Trajectory Tracking"
    assert r.authors == ["John Doe", "Jane Smith"]
    assert r.year == 2023
    assert r.arxiv_id == "2301.01234v1"
    assert r.doi == "10.1234/arxiv.2301.01234"
    assert r.pdf_url == "http://arxiv.org/pdf/2301.01234v1.pdf"
    assert r.source == "arxiv"


@pytest.mark.asyncio
async def test_search_openalex_mock():
    """Verify OpenAlex JSON parsing into SearchResult objects."""
    searcher = ScholarlyWebSearcher()

    mock_resp = mock.MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = SAMPLE_OPENALEX_JSON

    with mock.patch("httpx.AsyncClient.get", return_value=mock_resp):
        results = await searcher.search_openalex("baseball drag", limit=5)

    assert len(results) == 1
    r = results[0]
    assert r.title == "Aerodynamic Drag of Baseballs in Flight"
    assert r.authors == ["Alan Nathan"]
    assert r.year == 2021
    assert r.citation_count == 42
    assert r.doi == "10.1000/182"
    assert r.abstract == "The drag coefficient of a baseball is measured."
    assert r.pdf_url == "https://example.com/baseball_drag.pdf"
    assert r.source == "openalex"


@pytest.mark.asyncio
async def test_search_all_deduplication():
    """Verify search(source='all') deduplicates results by title and DOI."""
    searcher = ScholarlyWebSearcher()

    paper1 = SearchResult(
        title="Common Paper Title",
        authors=["Author One"],
        year=2022,
        source="arxiv",
        url="https://arxiv.org/abs/2201.001",
        doi="10.1000/common",
    )
    paper2 = SearchResult(
        title="Common Paper Title!",
        authors=["Author One"],
        year=2022,
        source="openalex",
        url="https://doi.org/10.1000/common",
        doi="10.1000/common",
    )
    paper3 = SearchResult(
        title="Unique Paper Title",
        authors=["Author Two"],
        year=2023,
        source="openalex",
        url="https://openalex.org/W999",
    )

    with (
        mock.patch.object(searcher, "search_arxiv", return_value=[paper1]),
        mock.patch.object(searcher, "search_openalex", return_value=[paper2, paper3]),
    ):
        combined = await searcher.search("common", source="all", limit=10)

    # Should deduplicate paper1 and paper2
    assert len(combined) == 2
    titles = [p.title for p in combined]
    assert "Unique Paper Title" in titles
