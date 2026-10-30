"""Unit tests for OpenAlex Citation Graph Builder."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from kb.sync.citations import CitationGraphBuilder, CitationGraphResult


@pytest.fixture
def builder() -> CitationGraphBuilder:
    return CitationGraphBuilder()


@pytest.mark.asyncio
async def test_build_citation_graph(builder: CitationGraphBuilder) -> None:
    session = AsyncMock()
    session.add = MagicMock()

    # Document 1 cites Document 2 and an external work
    doc1 = MagicMock()
    doc1.id = "doc-1"
    doc1.openalex_id = "https://openalex.org/W111"
    doc1.referenced_works = ["https://openalex.org/W222", "https://openalex.org/W999"]

    # Document 2 cites Document 1
    doc2 = MagicMock()
    doc2.id = "doc-2"
    doc2.openalex_id = "https://openalex.org/W222"
    doc2.referenced_works = ["https://openalex.org/W111"]

    # Mock execute return values:
    # 1. select(Document) -> [doc1, doc2]
    # 2. select(CitationLink) -> []
    docs_result = MagicMock()
    docs_result.scalars.return_value.all.return_value = [doc1, doc2]

    links_result = MagicMock()
    links_result.all.return_value = []

    session.execute.side_effect = [docs_result, links_result]

    result = await builder.build_citation_graph(session=session)

    assert isinstance(result, CitationGraphResult)
    assert result.total_documents == 2
    assert result.total_edges_created == 3
    assert result.internal_edges == 2  # doc1->doc2 and doc2->doc1
    assert result.external_edges == 1  # doc1->W999
    assert session.commit.called


@pytest.mark.asyncio
async def test_link_single_document(builder: CitationGraphBuilder) -> None:
    session = AsyncMock()
    session.add = MagicMock()

    doc = MagicMock()
    doc.id = "doc-1"
    doc.referenced_works = ["https://openalex.org/W222", "https://openalex.org/W333"]

    doc_result = MagicMock()
    doc_result.scalar_one_or_none.return_value = doc

    all_docs_result = MagicMock()
    all_docs_result.all.return_value = [("doc-2", "https://openalex.org/W222")]

    existing_result = MagicMock()
    existing_result.scalars.return_value.all.return_value = []

    session.execute.side_effect = [doc_result, all_docs_result, existing_result]

    edges_added = await builder.link_document("doc-1", session=session)
    assert edges_added == 2
    assert session.commit.called
