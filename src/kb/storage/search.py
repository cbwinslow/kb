"""Hybrid search engine combining pgvector dense cosine retrieval and full-text keyword ranking."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from kb.storage.database import DatabaseManager
from kb.storage.embeddings import EmbeddingProtocol
from kb.storage.models import Chunk

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SearchResult:
    """Consolidated search hit with RRF ranking and source metadata."""

    chunk_id: str
    document_id: str
    citekey: str
    section_path: list[str]
    parent_section: str | None
    text: str
    rrf_score: float
    dense_rank: int | None
    sparse_rank: int | None
    dense_score: float | None
    sparse_score: float | None
    has_math: bool
    has_table: bool


def reciprocal_rank_fusion(
    dense_ranked_ids: list[str],
    sparse_ranked_ids: list[str],
    k: int = 60,
) -> list[tuple[str, float, int | None, int | None]]:
    """Merges two ranked lists of entity IDs using Reciprocal Rank Fusion (RRF).

    Formula: RRF_score(d) = sum(1 / (k + rank_m(d))) for each system m in which d appears.
    Ranks are 1-based. Returns a list of (entity_id, rrf_score, dense_rank, sparse_rank)
    sorted by rrf_score descending.
    """
    scores: dict[str, float] = {}
    dense_rank_map: dict[str, int] = {}
    sparse_rank_map: dict[str, int] = {}

    for idx, entity_id in enumerate(dense_ranked_ids):
        rank = idx + 1
        dense_rank_map[entity_id] = rank
        scores[entity_id] = scores.get(entity_id, 0.0) + (1.0 / (k + rank))

    for idx, entity_id in enumerate(sparse_ranked_ids):
        rank = idx + 1
        sparse_rank_map[entity_id] = rank
        scores[entity_id] = scores.get(entity_id, 0.0) + (1.0 / (k + rank))

    sorted_entities = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    results: list[tuple[str, float, int | None, int | None]] = []
    for entity_id, score in sorted_entities:
        results.append((
            entity_id,
            score,
            dense_rank_map.get(entity_id),
            sparse_rank_map.get(entity_id),
        ))

    return results


class HybridSearchEngine:
    """Executes dense vector queries, sparse full-text queries, and merged RRF retrieval."""

    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db = db_manager

    async def dense_search(
        self,
        session: AsyncSession,
        query_vector: list[float],
        limit: int = 20,
        citekey: str | None = None,
    ) -> list[tuple[Chunk, float, int]]:
        """Finds closest chunks by cosine distance.

        Returns list of (Chunk, similarity_score, rank_1_based).
        """
        bind = session.bind
        dialect_name = bind.dialect.name if bind is not None else "postgresql"

        if dialect_name == "postgresql":
            # Vector cosine distance <=> supported natively on PostgreSQL + pgvector
            dist_expr = Chunk.embedding.cosine_distance(query_vector)
            stmt = (
                select(Chunk, dist_expr.label("distance"))
                .where(Chunk.embedding.is_not(None))
                .order_by(dist_expr.asc())
                .limit(limit)
            )
            if citekey:
                stmt = stmt.where(Chunk.citekey == citekey)

            res = await session.execute(stmt)
            rows = list(res.all())

            results: list[tuple[Chunk, float, int]] = []
            for idx, row in enumerate(rows):
                chunk: Chunk = row[0]
                distance = float(row[1]) if row[1] is not None else 1.0
                similarity = 1.0 - distance
                results.append((chunk, similarity, idx + 1))

            return results

        # Portable fallback for SQLite / unit testing: Python cosine calculation
        stmt = select(Chunk).where(Chunk.embedding.is_not(None))
        if citekey:
            stmt = stmt.where(Chunk.citekey == citekey)

        res = await session.execute(stmt)
        candidates: list[Chunk] = list(res.scalars().all())

        import math

        def cosine_similarity(v1: list[float], v2: list[float]) -> float:
            dot = sum(a * b for a, b in zip(v1, v2, strict=False))
            norm1 = math.sqrt(sum(a * a for a in v1))
            norm2 = math.sqrt(sum(b * b for b in v2))
            if norm1 == 0.0 or norm2 == 0.0:
                return 0.0
            return dot / (norm1 * norm2)

        scored: list[tuple[Chunk, float]] = []
        for c in candidates:
            if c.embedding is not None:
                sim = cosine_similarity(query_vector, c.embedding)
                scored.append((c, sim))

        scored.sort(key=lambda item: item[1], reverse=True)
        top_candidates = scored[:limit]

        return [(chunk, sim, idx + 1) for idx, (chunk, sim) in enumerate(top_candidates)]

    async def sparse_search(
        self,
        session: AsyncSession,
        query_text: str,
        limit: int = 20,
        citekey: str | None = None,
    ) -> list[tuple[Chunk, float, int]]:
        """Finds most relevant chunks by keyword full-text matching.

        Uses PostgreSQL websearch_to_tsquery and ts_rank_cd if running on PostgreSQL,
        or case-insensitive term matching with fallback scoring on SQLite.
        """
        bind = session.bind
        dialect_name = bind.dialect.name if bind is not None else "postgresql"

        if dialect_name == "postgresql":
            # PostgreSQL native tsvector ranking
            tsquery = func.websearch_to_tsquery("english", query_text)
            rank_expr = func.ts_rank_cd(
                func.to_tsvector("english", Chunk.enriched_text), tsquery
            )
            stmt = (
                select(Chunk, rank_expr.label("rank"))
                .where(func.to_tsvector("english", Chunk.enriched_text).op("@@")(tsquery))
                .order_by(rank_expr.desc())
                .limit(limit)
            )
            if citekey:
                stmt = stmt.where(Chunk.citekey == citekey)

            res = await session.execute(stmt)
            rows = list(res.all())
            if not rows:
                import re

                # Fallback to OR-joined tokens if strict AND produced no results
                raw_tokens = [re.sub(r"[^\w]", "", t).strip() for t in query_text.split()]
                valid_tokens = [t for t in raw_tokens if t]
                if len(valid_tokens) > 1:
                    or_query = " | ".join(valid_tokens)
                    or_tsquery = func.to_tsquery("english", or_query)
                    or_rank = func.ts_rank_cd(
                        func.to_tsvector("english", Chunk.enriched_text), or_tsquery
                    )
                    stmt_or = (
                        select(Chunk, or_rank.label("rank"))
                        .where(
                            func.to_tsvector("english", Chunk.enriched_text).op("@@")(or_tsquery)
                        )
                        .order_by(or_rank.desc())
                        .limit(limit)
                    )
                    if citekey:
                        stmt_or = stmt_or.where(Chunk.citekey == citekey)
                    res_or = await session.execute(stmt_or)
                    rows = list(res_or.all())

            return [(row[0], float(row[1]), idx + 1) for idx, row in enumerate(rows)]

        # Portable fallback for SQLite / testing: token matching
        tokens = [t.strip().lower() for t in query_text.split() if t.strip()]
        if not tokens:
            return []

        stmt = select(Chunk)
        if citekey:
            stmt = stmt.where(Chunk.citekey == citekey)

        res = await session.execute(stmt)
        all_chunks: list[Chunk] = list(res.scalars().all())

        scored_chunks: list[tuple[Chunk, float]] = []
        for chunk in all_chunks:
            text_lower = chunk.enriched_text.lower()
            matches = sum(1 for token in tokens if token in text_lower)
            if matches > 0:
                score = matches / len(tokens)
                scored_chunks.append((chunk, score))

        scored_chunks.sort(key=lambda x: x[1], reverse=True)
        top_chunks = scored_chunks[:limit]

        return [(chunk, score, idx + 1) for idx, (chunk, score) in enumerate(top_chunks)]

    async def hybrid_search(
        self,
        session: AsyncSession,
        query_text: str,
        query_vector: list[float] | None = None,
        embedder: EmbeddingProtocol | None = None,
        limit: int = 10,
        k: int = 60,
        citekey: str | None = None,
    ) -> list[SearchResult]:
        """Combines dense vector retrieval and sparse full-text retrieval using RRF."""
        chunk_map: dict[str, Chunk] = {}
        dense_ranks: list[str] = []
        dense_scores: dict[str, float] = {}
        sparse_ranks: list[str] = []
        sparse_scores: dict[str, float] = {}

        # 0. Vectorize query text if embedder is provided and query_vector is None
        effective_vector = query_vector
        if effective_vector is None and embedder is not None and query_text.strip():
            effective_vector = embedder.embed_query(query_text)

        # 1. Execute dense search if query vector is provided
        if effective_vector is not None:
            dense_results = await self.dense_search(
                session=session,
                query_vector=effective_vector,
                limit=limit * 2,
                citekey=citekey,
            )
            for chunk, sim_score, _ in dense_results:
                chunk_map[chunk.id] = chunk
                dense_ranks.append(chunk.id)
                dense_scores[chunk.id] = sim_score

        # 2. Execute sparse search if query text is provided
        if query_text.strip():
            sparse_results = await self.sparse_search(
                session=session,
                query_text=query_text,
                limit=limit * 2,
                citekey=citekey,
            )
            for chunk, bm25_score, _ in sparse_results:
                chunk_map[chunk.id] = chunk
                sparse_ranks.append(chunk.id)
                sparse_scores[chunk.id] = bm25_score

        # 3. Fuse via Reciprocal Rank Fusion
        fused = reciprocal_rank_fusion(dense_ranks, sparse_ranks, k=k)

        # 4. Construct final SearchResult list
        final_results: list[SearchResult] = []
        for chunk_id, rrf_score, d_rank, s_rank in fused[:limit]:
            chunk = chunk_map.get(chunk_id)
            if chunk is None:
                continue
            final_results.append(
                SearchResult(
                    chunk_id=chunk.id,
                    document_id=chunk.document_id,
                    citekey=chunk.citekey,
                    section_path=chunk.section_path,
                    parent_section=chunk.parent_section,
                    text=chunk.enriched_text,
                    rrf_score=rrf_score,
                    dense_rank=d_rank,
                    sparse_rank=s_rank,
                    dense_score=dense_scores.get(chunk_id),
                    sparse_score=sparse_scores.get(chunk_id),
                    has_math=chunk.has_math,
                    has_table=chunk.has_table,
                )
            )

        return final_results
