"""Unit tests for dense embedding generation and MockEmbeddingGenerator."""

from __future__ import annotations

import math
import uuid

import pytest
from sqlalchemy import select

from kb.cli import async_embed
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import (
    EMBEDDING_DIMENSION,
    EmbeddingProtocol,
    LocalEmbeddingGenerator,
    MockEmbeddingGenerator,
)
from kb.storage.models import Chunk, Document


def test_mock_embedding_dimensions_and_normalization() -> None:
    """Verifies that MockEmbeddingGenerator produces unit-normalized 1024-d vectors."""
    embedder = MockEmbeddingGenerator(dimension=EMBEDDING_DIMENSION)

    # 1. Single query embedding
    vec = embedder.embed_query("Pythagorean expectation in baseball")
    assert len(vec) == 1024
    norm = math.sqrt(sum(x * x for x in vec))
    assert math.isclose(norm, 1.0, rel_tol=1e-5)

    # 2. Batch embedding
    texts = [
        "A Derivation of the Pythagorean Expectation for Baseball",
        "Bayesian Hierarchical Models for Historical Player Evaluation",
        "Markov transition probabilities across base-out states",
    ]
    vecs = embedder.embed_texts(texts)
    assert len(vecs) == 3
    for v in vecs:
        assert len(v) == 1024
        v_norm = math.sqrt(sum(x * x for x in v))
        assert math.isclose(v_norm, 1.0, rel_tol=1e-5)


def test_mock_embedding_determinism() -> None:
    """Verifies that identical inputs produce identical embeddings and different inputs differ."""
    embedder = MockEmbeddingGenerator()

    v1 = embedder.embed_query("Weibull distribution")
    v2 = embedder.embed_query("Weibull distribution")
    v3 = embedder.embed_query("Poisson distribution")

    assert v1 == v2
    assert v1 != v3


def test_embedding_protocol_conformance() -> None:
    """Verifies that both Mock and Local generators satisfy EmbeddingProtocol."""
    mock_gen = MockEmbeddingGenerator()
    assert isinstance(mock_gen, EmbeddingProtocol)

    local_gen = LocalEmbeddingGenerator(device="cpu")
    assert isinstance(local_gen, EmbeddingProtocol)
    assert local_gen.model_name == "BAAI/bge-m3"


@pytest.mark.asyncio
async def test_async_embed_backfill() -> None:
    """Verifies that async_embed finds un-embedded chunks and populates their vectors."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_{db_id}?mode=memory&cache=shared&uri=true"
    manager = DatabaseManager(database_url=url, echo=False)
    await manager.init_db()

    async with manager.get_session() as session:
        doc = Document(
            citekey="test_key",
            title="Test Embedding Paper",
            authors=["Tester"],
            year=2026,
            file_path="data/test.pdf",
        )
        session.add(doc)
        await session.flush()

        c1 = Chunk(
            id="c1",
            document_id=doc.id,
            chunk_index=0,
            citekey="test_key",
            raw_text="Introduction to baseball statistics.",
            enriched_text="Document: Test Embedding Paper\n\nIntroduction to baseball statistics.",
            section_path="1. Introduction",
            has_math=False,
            has_table=False,
            embedding=None,
        )
        c2 = Chunk(
            id="c2",
            document_id=doc.id,
            chunk_index=1,
            citekey="test_key",
            raw_text="The Pythagorean formula approximates win percentage.",
            enriched_text=(
                "Document: Test Embedding Paper\n\n"
                "The Pythagorean formula approximates win percentage."
            ),
            section_path="2. Formula",
            has_math=True,
            has_table=False,
            embedding=None,
        )
        session.add_all([c1, c2])
        await session.flush()

    mock_embedder = MockEmbeddingGenerator()
    code = await async_embed(
        citekey="test_key",
        embedder=mock_embedder,
        manager=manager,
    )
    assert code == 0

    # Verify embeddings were populated
    async with manager.get_session() as session:
        res = await session.execute(select(Chunk).where(Chunk.citekey == "test_key"))
        updated_chunks = list(res.scalars().all())
        assert len(updated_chunks) == 2
        for c in updated_chunks:
            assert c.embedding is not None
            assert len(c.embedding) == 1024
            norm = math.sqrt(sum(x * x for x in c.embedding))
            assert math.isclose(norm, 1.0, rel_tol=1e-5)

    # Calling again should report no chunks missing embeddings
    code_second = await async_embed(
        citekey="test_key",
        embedder=mock_embedder,
        manager=manager,
    )
    assert code_second == 0
    await manager.close()

