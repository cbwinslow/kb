"""Adapter for auditing and migrating legacy documents into typed KB storage."""

from __future__ import annotations

import contextlib
import logging
import re
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from kb.math.extractor import FormulaExtractor
from kb.math.sanitizer import EquationSanitizer
from kb.storage.database import DatabaseManager
from kb.storage.models import Chunk, Document, Formula

logger = logging.getLogger(__name__)

# Default verified scientific and analytical research sources
DEFAULT_RESEARCH_SOURCES: list[str] = [
    "arxiv",
    "harvest-arxiv",
    "openalex",
    "harvest-openalex",
    "openalex-gap-ratings-models",
    "openalex-gap-validation-leakage",
    "openalex-gap-betting-markets",
    "project-cited",
    "sabr-journal",
    "abdwr3e-book",
    "fangraphs-library",
    "harvest-fangraphs-library",
    "retrosheet-research",
    "harvest-crawl:retrosheet",
    "tangotiger-blog",
    "harvest-tangotiger",
    "harvest-bp-research",
]


def parse_vector(val: Any) -> list[float] | None:
    """Parse raw vector column value into a list of floats.

    Supports string representations (e.g. '[-0.012, 0.345]'), Python sequences,
    or numpy arrays. Returns None if value is empty or unparseable.
    """
    if val is None:
        return None
    if isinstance(val, (list, tuple)):
        return [float(x) for x in val]
    if isinstance(val, str):
        cleaned = val.strip().strip("[]").strip()
        if not cleaned:
            return None
        try:
            return [float(x.strip()) for x in cleaned.split(",") if x.strip()]
        except ValueError:
            logger.warning("Failed to parse vector string: %.50s...", val)
            return None
    if hasattr(val, "tolist"):
        return [float(x) for x in val.tolist()]
    return None


@dataclass
class MigrationDocCandidate:
    """Metadata summary of a candidate legacy document eligible for migration."""

    doc_id: str
    title: str
    source: str
    url: str | None
    quality: int
    relevance: int
    topics: list[str] = field(default_factory=list)
    summary: str | None = None


@dataclass
class MigrationStats:
    """Metrics tracking the outcome of a migration batch."""

    scanned_candidates: int = 0
    migrated_documents: int = 0
    migrated_chunks: int = 0
    migrated_formulas: int = 0
    valid_formulas: int = 0
    skipped_documents: int = 0
    failed_documents: int = 0
    dry_run: bool = False
    errors: list[str] = field(default_factory=list)


class LegacyMigrationAdapter:
    """Audits legacy tables in read-only mode and migrates records into typed KB storage."""

    def __init__(
        self,
        db_manager: DatabaseManager,
        doc_table: str = "public.documents",
        chunk_table: str = "public.chunks",
        formula_table: str = "public.formulas",
    ) -> None:
        self.db = db_manager
        # On SQLite, unqualified table names are standard; on PostgreSQL, public. prefix is explicit
        if db_manager and getattr(db_manager, "is_sqlite", False):
            self.doc_table = doc_table.replace("public.", "")
            self.chunk_table = chunk_table.replace("public.", "")
            self.formula_table = formula_table.replace("public.", "")
        else:
            self.doc_table = doc_table
            self.chunk_table = chunk_table
            self.formula_table = formula_table
        self.sanitizer = EquationSanitizer()
        self.formula_extractor = FormulaExtractor(sanitizer=self.sanitizer)

    async def get_existing_legacy_doc_ids(self, session: AsyncSession) -> set[str]:
        """Fetch all legacy document IDs already imported into kb_documents."""
        bind = session.bind
        dialect_name = bind.dialect.name if bind is not None else "postgresql"
        existing: set[str] = set()

        try:
            if dialect_name == "postgresql":
                # Fast JSONB lookup on postgresql
                stmt = text(
                    "SELECT extra_metadata->>'legacy_doc_id' "
                    "FROM kb_documents WHERE extra_metadata ? 'legacy_doc_id';"
                )
                res = await session.execute(stmt)
                for row in res.fetchall():
                    if row[0]:
                        existing.add(str(row[0]))
            else:
                # SQLite fallback
                stmt = select(Document.extra_metadata)
                res = await session.execute(stmt)
                for meta in res.scalars().all():
                    if isinstance(meta, dict) and "legacy_doc_id" in meta:
                        existing.add(str(meta["legacy_doc_id"]))
        except Exception as exc:
            logger.warning("Could not query existing legacy_doc_ids: %s", exc)

        return existing

    async def get_all_citekeys(self, session: AsyncSession) -> set[str]:
        """Fetch all existing citekeys in kb_documents to avoid collisions."""
        stmt = select(Document.citekey)
        res = await session.execute(stmt)
        return {k.lower() for k in res.scalars().all()}

    async def scan_candidates(
        self,
        session: AsyncSession,
        min_quality: int = 7,
        min_relevance: int = 7,
        sources: list[str] | None = None,
        limit: int | None = None,
    ) -> list[MigrationDocCandidate]:
        """Query candidate documents from the legacy schema meeting quality and source criteria."""
        allowed_sources = sources if sources is not None else DEFAULT_RESEARCH_SOURCES
        existing_doc_ids = await self.get_existing_legacy_doc_ids(session)

        # Build parameterized query
        source_placeholders = ", ".join(f":s_{i}" for i in range(len(allowed_sources)))
        query_sql = f"""
            SELECT doc_id, title, source, url, quality, relevance, topics, summary
            FROM {self.doc_table}
            WHERE quality >= :min_quality
              AND relevance >= :min_relevance
              AND source IN ({source_placeholders})
            ORDER BY quality DESC, relevance DESC, doc_id ASC
        """
        if limit is not None:
            query_sql += f" LIMIT {int(limit)}"

        params: dict[str, Any] = {
            "min_quality": min_quality,
            "min_relevance": min_relevance,
        }
        for i, src in enumerate(allowed_sources):
            params[f"s_{i}"] = src

        res = await session.execute(text(query_sql), params)
        candidates: list[MigrationDocCandidate] = []

        for row in res.mappings().fetchall():
            d = dict(row)
            doc_id = str(d["doc_id"])
            if doc_id in existing_doc_ids:
                continue

            raw_topics = d.get("topics")
            topics_list: list[str] = []
            if isinstance(raw_topics, (list, tuple)):
                topics_list = [str(t) for t in raw_topics]

            candidates.append(
                MigrationDocCandidate(
                    doc_id=doc_id,
                    title=str(d.get("title") or "Untitled Document").strip(),
                    source=str(d.get("source") or "unknown").strip(),
                    url=str(d.get("url")) if d.get("url") else None,
                    quality=int(d.get("quality") or 0),
                    relevance=int(d.get("relevance") or 0),
                    topics=topics_list,
                    summary=str(d.get("summary")) if d.get("summary") else None,
                )
            )

        return candidates

    def synthesize_citekey(
        self,
        candidate: MigrationDocCandidate,
        first_chunk_text: str | None,
        existing_citekeys: set[str],
    ) -> str:
        """Generate a deterministic, clean alphanumeric citation key."""
        base_key = ""

        # Check for arXiv ID in url
        if candidate.url:
            arxiv_match = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", candidate.url)
            if arxiv_match:
                arxiv_num = arxiv_match.group(1).replace(".", "_")
                base_key = f"arxiv_{arxiv_num}"

        # Try extracting author and year from first chunk text (e.g. "by Author Name Month Year")
        if not base_key and first_chunk_text:
            by_match = re.search(
                r"by\s+([A-Z][a-z]+)\s+([A-Z][a-z]+)(?:.*?\b(20[0-2][0-9]|19[89][0-9]))?",
                first_chunk_text[:300],
            )
            if by_match:
                last_name = by_match.group(2).lower()
                year = by_match.group(3) or ""
                # short title slug
                slug = re.sub(r"[^a-z0-9]", "", candidate.title.lower())[:10]
                base_key = f"{last_name}{year}_{slug}" if slug else f"{last_name}{year}"

        # If still no base key, derive from source and title
        if not base_key:
            src_clean = (
                candidate.source.lower()
                .replace("harvest-", "")
                .replace("-library", "")
                .replace("-blog", "")
            )
            src_prefix = re.sub(r"[^a-z0-9]", "", src_clean)
            title_slug = re.sub(r"[^a-z0-9]+", "_", candidate.title.lower()).strip("_")
            short_slug = "_".join(title_slug.split("_")[:3])
            if short_slug:
                base_key = f"{src_prefix}_{short_slug}"
            else:
                base_key = f"{src_prefix}_{candidate.doc_id[:8]}"

        # Normalize key
        clean_key = re.sub(r"[^a-z0-9_]", "", base_key.lower()).strip("_")
        if not clean_key:
            clean_key = f"doc_{candidate.doc_id[:8]}"

        # Collision resolution
        candidate_key = clean_key
        counter = 2
        while candidate_key in existing_citekeys:
            candidate_key = f"{clean_key}_{counter}"
            counter += 1

        existing_citekeys.add(candidate_key)
        return candidate_key

    async def fetch_legacy_chunks(self, session: AsyncSession, doc_id: str) -> list[dict[str, Any]]:
        """Fetch all chunks belonging to a legacy document in position order."""
        stmt = text(f"""
            SELECT chunk_id, position, text, emb_bgem3, context
            FROM {self.chunk_table}
            WHERE doc_id = :doc_id
            ORDER BY position ASC
        """)
        res = await session.execute(stmt, {"doc_id": doc_id})
        return [dict(r) for r in res.mappings().fetchall()]

    async def fetch_legacy_formulas(
        self, session: AsyncSession, doc_id: str
    ) -> list[dict[str, Any]]:
        """Fetch all mathematical formulas associated with a legacy document."""
        stmt = text(f"""
            SELECT formula_id, section, label, latex
            FROM {self.formula_table}
            WHERE doc_id = :doc_id
        """)
        res = await session.execute(stmt, {"doc_id": doc_id})
        return [dict(r) for r in res.mappings().fetchall()]

    async def migrate_candidate(
        self,
        session: AsyncSession,
        candidate: MigrationDocCandidate,
        existing_citekeys: set[str],
        dry_run: bool = False,
    ) -> tuple[int, int, int]:
        """Migrate a single candidate document, its chunks, and formulas.

        Returns:
            tuple of (chunk_count, formula_count, valid_formula_count)
        """
        raw_chunks = await self.fetch_legacy_chunks(session, candidate.doc_id)
        raw_formulas = await self.fetch_legacy_formulas(session, candidate.doc_id)

        first_text = raw_chunks[0]["text"] if raw_chunks else ""
        citekey = self.synthesize_citekey(candidate, first_text, existing_citekeys)

        # Detect arXiv ID from URL or citekey
        arxiv_id: str | None = None
        if candidate.url and "arxiv.org" in candidate.url:
            m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)", candidate.url)
            if m:
                arxiv_id = m.group(1)

        # Extract year if detected
        year: int | None = None
        year_match = re.search(r"\b(20[0-2][0-9]|19[89][0-9])\b", first_text[:400])
        if year_match:
            with contextlib.suppress(ValueError):
                year = int(year_match.group(1))

        if dry_run:
            valid_f_count = sum(
                1 for f in raw_formulas if f.get("latex") and len(f["latex"].strip()) > 1
            )
            return len(raw_chunks), len(raw_formulas), valid_f_count

        # Create Document record
        doc_record = Document(
            id=str(uuid.uuid4()),
            citekey=citekey,
            title=candidate.title,
            authors=[],
            year=year,
            doi=None,
            arxiv_id=arxiv_id,
            abstract=candidate.summary,
            file_path=candidate.url,
            extra_metadata={
                "legacy_doc_id": candidate.doc_id,
                "legacy_source": candidate.source,
                "legacy_quality": candidate.quality,
                "legacy_relevance": candidate.relevance,
                "legacy_topics": candidate.topics,
            },
        )
        session.add(doc_record)
        await session.flush()

        # Build chunks
        created_chunks: list[Chunk] = []
        chunk_id_map: dict[int, str] = {}  # position -> chunk.id

        for idx, rc in enumerate(raw_chunks):
            raw_text = str(rc.get("text") or "").strip()
            embedding_val = parse_vector(rc.get("emb_bgem3"))
            context_note = rc.get("context")

            # Check for math and table markup
            has_math = bool(re.search(r"\$|\\begin\{", raw_text))
            has_table = bool(re.search(r"\|.*\|.*\|", raw_text))

            # Breadcrumb enrichment
            if context_note:
                section_label = str(context_note)[:60]
            else:
                section_label = f"Section {rc.get('position', idx)}"

            if raw_text.startswith("[Document:"):
                enriched_text = raw_text
            else:
                enriched_text = (
                    f"[Document: {candidate.title} | Citekey: {citekey} | "
                    f"Section: {section_label}]\n\n{raw_text}"
                )

            c_id = str(uuid.uuid4())
            chunk_id_map[rc.get("position", idx)] = c_id

            chunk_record = Chunk(
                id=c_id,
                document_id=doc_record.id,
                chunk_index=idx,
                citekey=citekey,
                raw_text=raw_text,
                enriched_text=enriched_text,
                section_path=[candidate.title, section_label],
                parent_section=section_label,
                has_math=has_math,
                has_table=has_table,
                embedding=embedding_val,
            )
            created_chunks.append(chunk_record)

        # Relational chunk linkage
        for i, c in enumerate(created_chunks):
            if i > 0:
                c.previous_chunk_id = created_chunks[i - 1].id
            if i < len(created_chunks) - 1:
                c.next_chunk_id = created_chunks[i + 1].id
            session.add(c)

        await session.flush()

        # Process and link formulas
        valid_formulas = 0
        for rf in raw_formulas:
            latex_str = str(rf.get("latex") or "").strip()
            if not latex_str:
                continue

            sanitized = self.sanitizer.sanitize(latex_str)
            # Associate with chunk if possible
            matched_chunk_id: str | None = None
            for c in created_chunks:
                if latex_str in c.raw_text or (len(sanitized) > 5 and sanitized in c.raw_text):
                    matched_chunk_id = c.id
                    c.has_math = True
                    break

            # Attempt symbolic parse
            is_valid = False
            sympy_repr: str | None = None
            symbols_list: list[str] = []
            is_eq = False
            lhs: str | None = None
            rhs: str | None = None

            try:
                extracted = self.formula_extractor.parse_latex_string(sanitized)
                if extracted.is_valid and extracted.sympy_expr is not None:
                    is_valid = True
                    valid_formulas += 1
                    sympy_repr = str(extracted.sympy_expr)
                    symbols_list = extracted.symbols
                    is_eq = extracted.is_equality
                    lhs = extracted.lhs
                    rhs = extracted.rhs
            except Exception:
                # Keep formula record even if SymPy parse fails
                pass

            f_record = Formula(
                id=str(uuid.uuid4()),
                document_id=doc_record.id,
                chunk_id=matched_chunk_id or (created_chunks[0].id if created_chunks else None),
                citekey=citekey,
                raw_latex=latex_str,
                sanitized_latex=sanitized,
                sympy_repr=sympy_repr,
                symbols=symbols_list,
                is_valid=is_valid,
                is_equality=is_eq,
                lhs=lhs,
                rhs=rhs,
            )
            session.add(f_record)

        return len(created_chunks), len(raw_formulas), valid_formulas

    async def migrate_batch(
        self,
        min_quality: int = 7,
        min_relevance: int = 7,
        sources: list[str] | None = None,
        limit: int | None = None,
        dry_run: bool = False,
        on_progress: Callable[[int, int, MigrationDocCandidate], None] | None = None,
    ) -> MigrationStats:
        """Scan, filter, and migrate candidate documents in controlled transactions."""
        stats = MigrationStats(dry_run=dry_run)

        async with self.db.get_session() as session:
            candidates = await self.scan_candidates(
                session=session,
                min_quality=min_quality,
                min_relevance=min_relevance,
                sources=sources,
                limit=limit,
            )
            stats.scanned_candidates = len(candidates)
            existing_citekeys = await self.get_all_citekeys(session)

        for i, candidate in enumerate(candidates):
            try:
                async with self.db.get_session() as session:
                    c_count, f_count, v_count = await self.migrate_candidate(
                        session=session,
                        candidate=candidate,
                        existing_citekeys=existing_citekeys,
                        dry_run=dry_run,
                    )
                    stats.migrated_documents += 1
                    stats.migrated_chunks += c_count
                    stats.migrated_formulas += f_count
                    stats.valid_formulas += v_count

                    if on_progress:
                        on_progress(i + 1, len(candidates), candidate)
            except Exception as exc:
                stats.failed_documents += 1
                safe_title = candidate.title.encode("ascii", errors="replace").decode("ascii")
                err_msg = f"Failed migrating {candidate.doc_id} ('{safe_title}'): {exc}"
                logger.error(err_msg, exc_info=True)
                stats.errors.append(err_msg)

        return stats
