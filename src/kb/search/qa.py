"""Research question answering and evidence-grounded scientific synthesis."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy import or_, select

from kb.codegen.compiler import FormulaCompiler
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import EmbeddingProtocol, LocalEmbeddingGenerator
from kb.storage.models import BenchmarkTable, Document, Formula
from kb.storage.search import HybridSearchEngine, SearchResult

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class ResearchAnswer:
    """Evidence-grounded scientific research brief."""

    question: str
    synthesis: str
    cited_sources: list[dict[str, Any]] = field(default_factory=list)
    grounding_chunks: list[dict[str, Any]] = field(default_factory=list)
    relevant_formulas: list[dict[str, Any]] = field(default_factory=list)
    relevant_tables: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert brief to dictionary representation."""
        return {
            "question": self.question,
            "synthesis": self.synthesis,
            "cited_sources": self.cited_sources,
            "grounding_chunks": self.grounding_chunks,
            "relevant_formulas": self.relevant_formulas,
            "relevant_tables": self.relevant_tables,
        }

    def format_terminal(self) -> str:
        """Render markdown-formatted summary for CLI presentation."""
        lines: list[str] = [
            "=" * 78,
            f"RESEARCH SYNTHESIS: {self.question}",
            "=" * 78,
            "",
            self.synthesis,
            "",
            "-" * 78,
            "RELEVANT MATHEMATICAL FORMULATIONS:",
            "-" * 78,
        ]
        if self.relevant_formulas:
            for f in self.relevant_formulas[:4]:
                lines.append(f"• [{f['citekey']}] {f['latex']}")
                if f.get("python_code"):
                    lines.append(f"  Code: {f['python_code'].strip()}")
        else:
            lines.append("  (No mathematical formulas extracted for this query)")

        lines.extend(
            [
                "",
                "-" * 78,
                "EMPIRICAL BENCHMARK FIXTURES:",
                "-" * 78,
            ]
        )
        if self.relevant_tables:
            for t in self.relevant_tables[:3]:
                cols = ", ".join(t.get("columns", [])[:6])
                lines.append(f"• [{t['citekey']}] {t.get('caption') or 'Table'}")
                lines.append(f"  Columns: {cols} ({t.get('num_rows', 0)} rows)")
        else:
            lines.append("  (No benchmark tables matched for this query)")

        lines.extend(
            [
                "",
                "-" * 78,
                "GROUNDING CITATIONS:",
                "-" * 78,
            ]
        )
        for src in self.cited_sources:
            authors_str = ", ".join(src.get("authors", [])[:3])
            lines.append(
                f'• [{src["citekey"]}] "{src["title"]}" ({src.get("year", "n.d.")}) - {authors_str}'
            )

        lines.append("=" * 78)
        return "\n".join(lines)


class CorpusQAEngine:
    """Answers research queries with grounded citations, mathematical models, and empirical tables."""

    def __init__(
        self,
        db_manager: DatabaseManager | None = None,
        embedder: EmbeddingProtocol | None = None,
        compiler: FormulaCompiler | None = None,
    ) -> None:
        self.db_manager = db_manager or DatabaseManager()
        self.embedder = embedder or LocalEmbeddingGenerator()
        self.search_engine = HybridSearchEngine(db_manager=self.db_manager)
        self.compiler = compiler or FormulaCompiler()

    async def answer(
        self,
        question: str,
        top_k: int = 5,
        include_code: bool = True,
    ) -> ResearchAnswer:
        """Produce an evidence-grounded research answer for the given inquiry."""
        clean_q = question.strip()
        logger.info("Executing QA query: '%s' (top_k=%d)", clean_q, top_k)

        async with self.db_manager.session_factory() as session:
            # 1. Retrieve candidate chunks via hybrid dense+sparse search
            search_results: list[SearchResult] = await self.search_engine.search(
                session, query_text=clean_q, embedder=self.embedder, limit=top_k
            )

            if not search_results:
                return ResearchAnswer(
                    question=clean_q,
                    synthesis="No relevant literature or mathematical derivations were found in the corpus for this inquiry.",
                )

            chunk_ids = [r.chunk_id for r in search_results]
            citekeys = list(dict.fromkeys(r.citekey for r in search_results))

            # 2. Fetch full metadata for cited documents
            doc_stmt = select(Document).where(Document.citekey.in_(citekeys))
            doc_res = await session.execute(doc_stmt)
            docs = {d.citekey: d for d in doc_res.scalars().all()}

            # 3. Fetch relevant formulas (from either matching chunks or matching citekeys)
            f_stmt = (
                select(Formula)
                .where(
                    or_(
                        Formula.chunk_id.in_(chunk_ids),
                        Formula.citekey.in_(citekeys),
                    ),
                    Formula.is_valid == True,  # noqa: E712
                )
                .limit(6)
            )
            formulas = list((await session.execute(f_stmt)).scalars().all())

            # 4. Fetch relevant benchmark tables
            tbl_stmt = (
                select(BenchmarkTable)
                .where(
                    or_(
                        BenchmarkTable.chunk_id.in_(chunk_ids),
                        BenchmarkTable.citekey.in_(citekeys),
                    )
                )
                .limit(4)
            )
            tables = list((await session.execute(tbl_stmt)).scalars().all())

            # 5. Format formulas and compile executable AST
            formula_data: list[dict[str, Any]] = []
            for f in formulas:
                item: dict[str, Any] = {
                    "formula_id": f.id,
                    "citekey": f.citekey,
                    "latex": f.raw_latex,
                    "symbols": f.symbols,
                }
                if include_code:
                    code_res = self.compiler.compile(
                        formula_id=f.id,
                        citekey=f.citekey,
                        raw_latex=f.raw_latex,
                        sympy_repr=f.sympy_repr,
                    )
                    if code_res.is_valid:
                        item["python_code"] = code_res.python_source
                        item["polars_expression"] = code_res.polars_expression
                formula_data.append(item)

            # 6. Format benchmark tables
            table_data: list[dict[str, Any]] = [
                {
                    "table_id": t.id,
                    "citekey": t.citekey,
                    "caption": t.caption,
                    "columns": t.column_names,
                    "num_rows": t.num_rows,
                    "parquet_path": t.parquet_path,
                }
                for t in tables
            ]

            # 7. Format cited sources and grounding chunks
            sources_data: list[dict[str, Any]] = [
                {
                    "citekey": ck,
                    "title": docs[ck].title if ck in docs else ck,
                    "authors": docs[ck].authors if ck in docs else [],
                    "year": docs[ck].year if ck in docs else None,
                    "doi": docs[ck].doi if ck in docs else None,
                }
                for ck in citekeys
            ]

            grounding_data: list[dict[str, Any]] = [
                {
                    "chunk_id": r.chunk_id,
                    "citekey": r.citekey,
                    "score": round(r.rrf_score, 4),
                    "snippet": r.text[:280] + "..." if len(r.text) > 280 else r.text,
                    "section_path": r.section_path,
                }
                for r in search_results
            ]

            # 8. Synthesize scientific brief
            synthesis_parts: list[str] = [
                f"Based on evidence retrieved across {len(citekeys)} peer-reviewed documents in the knowledge base:",
                "",
            ]

            for r in search_results[:3]:
                sec = f" ({' > '.join(r.section_path)})" if r.section_path else ""
                synthesis_parts.append(f"• [{r.citekey}]{sec}: {r.text.strip()}")

            synthesis = "\n".join(synthesis_parts)

            return ResearchAnswer(
                question=clean_q,
                synthesis=synthesis,
                cited_sources=sources_data,
                grounding_chunks=grounding_data,
                relevant_formulas=formula_data,
                relevant_tables=table_data,
            )
