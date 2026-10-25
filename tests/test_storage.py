"""Unit and integration tests for KB storage layer, models, and hybrid search."""

from __future__ import annotations

import math
import uuid

import pytest
from sqlalchemy import select

from kb.storage import (
    BenchmarkTable,
    Chunk,
    DatabaseManager,
    Document,
    Formula,
    HybridSearchEngine,
    reciprocal_rank_fusion,
)


@pytest.fixture
def test_db_manager() -> DatabaseManager:
    """Creates an in-memory async SQLite database manager for hermetic unit testing."""
    # Use SQLite shared-cache in-memory database to allow multiple async connections
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_{db_id}?mode=memory&cache=shared&uri=true"
    return DatabaseManager(database_url=url, echo=False)


@pytest.mark.asyncio
async def test_database_manager_init_and_check(test_db_manager: DatabaseManager) -> None:
    """Verifies schema initialization and connection check."""
    await test_db_manager.init_db()
    ok, message = await test_db_manager.check_connection()
    assert ok is True
    assert "Connection established" in message
    await test_db_manager.close()


@pytest.mark.asyncio
async def test_database_connection_failure_handling() -> None:
    """Verifies that check_connection returns descriptive failure for unreachable server."""
    # 192.0.2.1 is TEST-NET-1 (non-routable)
    bad_manager = DatabaseManager(
        database_url="postgresql+asyncpg://kb_user:kb_pass@192.0.2.1:5432/kb",
        connect_args={"timeout": 0.5},
    )
    ok, message = await bad_manager.check_connection()
    assert ok is False
    assert "Database handshake failed" in message
    await bad_manager.close()


@pytest.mark.asyncio
async def test_document_and_relational_models(test_db_manager: DatabaseManager) -> None:
    """Verifies Document, Chunk, Formula, and BenchmarkTable creation and cascade deletion."""
    await test_db_manager.init_db()

    async with test_db_manager.get_session() as session:
        doc = Document(
            citekey="miller2005",
            title="A Derivation of the Pythagorean Expectation for Baseball",
            authors=["Steven J. Miller"],
            year=2005,
            arxiv_id="math/0509698",
        )
        session.add(doc)
        await session.flush()

        chunk_1 = Chunk(
            document_id=doc.id,
            chunk_index=0,
            citekey=doc.citekey,
            raw_text="In this paper we derive Pythagorean expectation using Weibull distributions.",
            enriched_text="[miller2005 | Introduction] We derive the Pythagorean expectation.",
            section_path=["1. Introduction"],
            parent_section="1. Introduction",
            has_math=False,
        )
        chunk_2 = Chunk(
            document_id=doc.id,
            chunk_index=1,
            citekey=doc.citekey,
            raw_text="W = \\frac{R_S^\\gamma}{R_S^\\gamma + R_A^\\gamma}",
            enriched_text="[miller2005 | Eq] W = \\frac{R_S^\\gamma}{R_S^\\gamma + R_A^\\gamma}",
            section_path=["2. Mathematical Models"],
            parent_section="2. Mathematical Models",
            has_math=True,
            previous_chunk_id=chunk_1.id,
        )
        session.add_all([chunk_1, chunk_2])
        await session.flush()

        formula = Formula(
            document_id=doc.id,
            chunk_id=chunk_2.id,
            citekey=doc.citekey,
            raw_latex="W = \\frac{RS^2}{RS^2 + RA^2}",
            sanitized_latex="W = \\frac{R_S^2}{R_S^2 + R_A^2}",
            sympy_repr="Eq(W, R_S**2 / (R_A**2 + R_S**2))",
            symbols=["W", "R_S", "R_A"],
            is_valid=True,
            is_equality=True,
            lhs="W",
            rhs="R_S**2 / (R_A**2 + R_S**2)",
        )
        session.add(formula)

        table = BenchmarkTable(
            document_id=doc.id,
            chunk_id=chunk_2.id,
            citekey=doc.citekey,
            caption="Empirical Exponent Fits across MLB Seasons",
            num_rows=30,
            num_cols=4,
            column_names=["Season", "Exponent_gamma", "StdErr", "R_Squared"],
        )
        session.add(table)

    # Verify retrieval
    async with test_db_manager.get_session() as session:
        stmt = select(Document).where(Document.citekey == "miller2005")
        result = await session.execute(stmt)
        retrieved_doc = result.scalar_one()

        assert retrieved_doc.title.startswith("A Derivation of the Pythagorean")
        assert len(retrieved_doc.chunks) == 2
        assert len(retrieved_doc.formulas) == 1
        assert len(retrieved_doc.benchmark_tables) == 1
        assert retrieved_doc.formulas[0].symbols == ["W", "R_S", "R_A"]
        assert retrieved_doc.benchmark_tables[0].num_rows == 30

    # Test cascade deletion
    async with test_db_manager.get_session() as session:
        stmt = select(Document).where(Document.citekey == "miller2005")
        result = await session.execute(stmt)
        retrieved_doc = result.scalar_one()
        await session.delete(retrieved_doc)

    async with test_db_manager.get_session() as session:
        chunk_res = await session.execute(select(Chunk))
        formula_res = await session.execute(select(Formula))
        table_res = await session.execute(select(BenchmarkTable))
        assert len(chunk_res.scalars().all()) == 0
        assert len(formula_res.scalars().all()) == 0
        assert len(table_res.scalars().all()) == 0

    await test_db_manager.close()


def test_reciprocal_rank_fusion_math() -> None:
    """Verifies Reciprocal Rank Fusion calculation with known numerical inputs."""
    dense = ["doc_A", "doc_B", "doc_C"]
    sparse = ["doc_B", "doc_D", "doc_A"]

    # k = 60
    # doc_A: dense 1 (1/61), sparse 3 (1/63) -> 1/61 + 1/63 = 0.016393 + 0.015873 = 0.032266
    # doc_B: dense 2 (1/62), sparse 1 (1/61) -> 1/62 + 1/61 = 0.016129 + 0.016393 = 0.032522
    # doc_C: dense 3 (1/63) -> 0.015873
    # doc_D: sparse 2 (1/62) -> 0.016129
    # doc_B should rank #1, doc_A should rank #2, doc_D #3, doc_C #4

    fused = reciprocal_rank_fusion(dense, sparse, k=60)
    assert len(fused) == 4

    top_id, top_score, d_rank, s_rank = fused[0]
    assert top_id == "doc_B"
    assert math.isclose(top_score, (1.0 / 62) + (1.0 / 61), rel_tol=1e-5)
    assert d_rank == 2
    assert s_rank == 1

    second_id, second_score, d_rank, s_rank = fused[1]
    assert second_id == "doc_A"
    assert math.isclose(second_score, (1.0 / 61) + (1.0 / 63), rel_tol=1e-5)
    assert d_rank == 1
    assert s_rank == 3


@pytest.mark.asyncio
async def test_hybrid_search_engine(test_db_manager: DatabaseManager) -> None:
    """Verifies end-to-end hybrid search combining dense and sparse retrieval."""
    await test_db_manager.init_db()

    engine = HybridSearchEngine(test_db_manager)

    # Populate test data
    async with test_db_manager.get_session() as session:
        doc1 = Document(citekey="miller2005", title="Pythagorean Derivation", authors=["Miller"])
        doc2 = Document(citekey="jensen2009", title="Bayesball Models", authors=["Jensen"])
        session.add_all([doc1, doc2])
        await session.flush()

        # Synthetic 1024-d unit vectors
        vec_pyth = [1.0] + [0.0] * 1023
        vec_bayes = [0.0, 1.0] + [0.0] * 1022
        vec_generic = [0.0, 0.0, 1.0] + [0.0] * 1021

        c1 = Chunk(
            document_id=doc1.id,
            chunk_index=0,
            citekey=doc1.citekey,
            raw_text="The Pythagorean expectation relates runs scored to winning ratio.",
            enriched_text="[miller2005 | Eq] Pythagorean expectation relates runs to win ratio.",
            section_path=["1. Formula"],
            embedding=vec_pyth,
            has_math=True,
        )
        c2 = Chunk(
            document_id=doc2.id,
            chunk_index=0,
            citekey=doc2.citekey,
            raw_text="Bayesball uses hierarchical Bayesian models to estimate player abilities.",
            enriched_text="[jensen2009 | Intro] Hierarchical Bayesian models in baseball.",
            section_path=["1. Intro"],
            embedding=vec_bayes,
            has_math=False,
        )
        c3 = Chunk(
            document_id=doc2.id,
            chunk_index=1,
            citekey=doc2.citekey,
            raw_text="Markov transition probabilities for the 24 base-out states.",
            enriched_text="[jensen2009 | States] Markov matrix for baseball base-out states.",
            section_path=["2. Markov Models"],
            embedding=vec_generic,
            has_table=True,
        )
        session.add_all([c1, c2, c3])

    async with test_db_manager.get_session() as session:
        # 1. Sparse keyword search
        sparse_hits = await engine.sparse_search(session, query_text="Pythagorean runs", limit=5)
        assert len(sparse_hits) >= 1
        assert sparse_hits[0][0].citekey == "miller2005"

        # 2. Dense vector search
        query_v = [0.9] + [0.0] * 1023
        dense_hits = await engine.dense_search(session, query_vector=query_v, limit=5)
        assert len(dense_hits) >= 1
        assert dense_hits[0][0].citekey == "miller2005"

        # 3. Hybrid search merging both
        hybrid_hits = await engine.hybrid_search(
            session=session,
            query_text="Pythagorean expectation",
            query_vector=query_v,
            limit=5,
        )
        assert len(hybrid_hits) >= 1
        top_hit = hybrid_hits[0]
        assert top_hit.citekey == "miller2005"
        assert top_hit.has_math is True
        assert top_hit.dense_rank == 1
        assert top_hit.sparse_rank == 1
        assert top_hit.rrf_score > 0

        # 4. Filter by citekey
        filtered_hits = await engine.hybrid_search(
            session=session,
            query_text="baseball",
            query_vector=None,
            citekey="jensen2009",
            limit=5,
        )
        for hit in filtered_hits:
            assert hit.citekey == "jensen2009"

    await test_db_manager.close()
