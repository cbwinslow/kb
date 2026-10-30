"""OpenAlex Citation Graph Builder and Inter-Paper Lineage Engine."""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field
from sqlalchemy import select

from kb.storage.database import DatabaseManager
from kb.storage.models import CitationLink, Document

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class CitationGraphResult(BaseModel):
    """Execution summary of citation graph construction."""

    total_documents: int = Field(default=0, description="Documents examined")
    total_edges_created: int = Field(default=0, description="Total citation links established")
    internal_edges: int = Field(
        default=0, description="Citations linking two documents within local KB"
    )
    external_edges: int = Field(default=0, description="Citations to external OpenAlex works")
    duration_seconds: float = Field(default=0.0, description="Processing duration in seconds")


class CitationGraphBuilder:
    """Builds and maintains the paper-to-paper citation network in PostgreSQL."""

    def __init__(self, db_manager: DatabaseManager | None = None) -> None:
        """Initialize citation graph builder.

        Args:
            db_manager: Optional DatabaseManager. Default instantiated if None.
        """
        self.db_manager = db_manager or DatabaseManager()

    async def build_citation_graph(
        self,
        session: AsyncSession | None = None,
        year_filter: tuple[int, int] | None = None,
    ) -> CitationGraphResult:
        """Scan stored documents, resolve referenced works, and populate kb_citations.

        Args:
            session: Optional existing AsyncSession.
            year_filter: Optional tuple of (start_year, end_year) to filter documents.

        Returns:
            CitationGraphResult summarizing established citation edges.
        """
        start_time = time.perf_counter()

        if session is not None:
            return await self._execute_build(session, start_time, year_filter=year_filter)

        async with self.db_manager.get_session() as sess:
            return await self._execute_build(sess, start_time, year_filter=year_filter)

    async def link_document(
        self,
        document_id: str,
        session: AsyncSession | None = None,
    ) -> int:
        """Resolve and persist citation edges for a single document against corpus works.

        Args:
            document_id: Database ID of the document.
            session: Optional existing AsyncSession.

        Returns:
            Number of citation links created.
        """
        if session is not None:
            return await self._execute_link_single(session, document_id)

        async with self.db_manager.get_session() as sess:
            return await self._execute_link_single(sess, document_id)

    async def _execute_link_single(
        self,
        session: AsyncSession,
        document_id: str,
    ) -> int:
        """Internal helper linking a single document's references."""
        doc = (
            await session.execute(select(Document).where(Document.id == document_id))
        ).scalar_one_or_none()
        if not doc or not doc.referenced_works:
            return 0

        all_docs = (await session.execute(select(Document.id, Document.openalex_id))).all()
        oa_map: dict[str, str] = {}
        for d_id, oa_id in all_docs:
            if oa_id:
                clean = oa_id.strip()
                oa_map[clean] = d_id
                if "/" in clean:
                    oa_map[clean.split("/")[-1]] = d_id

        existing = (
            (
                await session.execute(
                    select(CitationLink.cited_openalex_id).where(
                        CitationLink.citing_document_id == document_id
                    )
                )
            )
            .scalars()
            .all()
        )
        existing_set = set(existing)

        edges_added = 0
        for ref_id in doc.referenced_works:
            ref_clean = str(ref_id).strip()
            if ref_clean in existing_set:
                continue

            short_ref = ref_clean.split("/")[-1] if "/" in ref_clean else ref_clean
            matched_id = oa_map.get(ref_clean) or oa_map.get(short_ref)

            link = CitationLink(
                citing_document_id=doc.id,
                cited_document_id=matched_id,
                cited_openalex_id=ref_clean,
            )
            session.add(link)
            existing_set.add(ref_clean)
            edges_added += 1

        if edges_added > 0:
            await session.commit()

        return edges_added

    async def _execute_build(
        self,
        session: AsyncSession,
        start_time: float,
        year_filter: tuple[int, int] | None = None,
    ) -> CitationGraphResult:
        """Internal worker executing citation resolution and persistence."""
        # 1. Fetch all documents in corpus
        stmt = select(Document)
        if year_filter:
            stmt = stmt.where(Document.year >= year_filter[0]).where(
                Document.year <= year_filter[1]
            )
        docs = (await session.execute(stmt)).scalars().all()

        # Build index: OpenAlex ID (and URL) -> Document ID
        openalex_to_doc_id: dict[str, str] = {}
        for d in docs:
            if d.openalex_id:
                clean_id = d.openalex_id.strip()
                openalex_to_doc_id[clean_id] = d.id
                # Strip URL prefix if present (e.g. https://openalex.org/W1234 -> W1234)
                if "/" in clean_id:
                    short_id = clean_id.split("/")[-1]
                    openalex_to_doc_id[short_id] = d.id

        # 2. Fetch existing citation links to avoid duplicating
        existing_stmt = select(CitationLink.citing_document_id, CitationLink.cited_openalex_id)
        existing_rows = (await session.execute(existing_stmt)).all()
        existing_pairs: set[tuple[str, str]] = {(r[0], r[1]) for r in existing_rows}

        total_edges = 0
        internal_edges = 0
        external_edges = 0

        # 3. Iterate over documents and create links
        for doc in docs:
            refs: list[str] = doc.referenced_works or []
            if not refs:
                continue

            for ref_id in refs:
                ref_clean = str(ref_id).strip()
                if (doc.id, ref_clean) in existing_pairs:
                    continue

                short_ref = ref_clean.split("/")[-1] if "/" in ref_clean else ref_clean
                matched_doc_id = openalex_to_doc_id.get(ref_clean) or openalex_to_doc_id.get(
                    short_ref
                )

                is_internal = matched_doc_id is not None
                if is_internal:
                    internal_edges += 1
                else:
                    external_edges += 1

                link = CitationLink(
                    citing_document_id=doc.id,
                    cited_document_id=matched_doc_id,
                    cited_openalex_id=ref_clean,
                )
                session.add(link)
                existing_pairs.add((doc.id, ref_clean))
                total_edges += 1

        if total_edges > 0:
            await session.commit()

        duration = time.perf_counter() - start_time
        return CitationGraphResult(
            total_documents=len(docs),
            total_edges_created=total_edges,
            internal_edges=internal_edges,
            external_edges=external_edges,
            duration_seconds=round(duration, 2),
        )
