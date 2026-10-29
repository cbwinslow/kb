"""FastMCP agent service exposing scientific knowledge base tools."""

from __future__ import annotations

import logging
from typing import Any

from fastmcp import FastMCP
from sqlalchemy import select

from kb.codegen.compiler import FormulaCompiler
from kb.codegen.verifier import FormulaVerifier
from kb.enrich.openalex import OpenAlexClient
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import EmbeddingProtocol, LocalEmbeddingGenerator
from kb.storage.models import BenchmarkTable, Document, Formula
from kb.storage.search import HybridSearchEngine

logger = logging.getLogger(__name__)


def create_mcp_server(
    db_manager: DatabaseManager | None = None,
    embedder: EmbeddingProtocol | None = None,
    openalex_client: OpenAlexClient | None = None,
) -> FastMCP:
    """Creates and configures the FastMCP server with all KB query tools."""
    server = FastMCP(
        name="Scientific Knowledge Base (kb)",
        instructions=(
            "Grounds AI coding agents in verified scientific literature, formulas, and fixtures."
        ),
    )

    db = db_manager or DatabaseManager()
    active_embedder = embedder or LocalEmbeddingGenerator()
    active_openalex = openalex_client or OpenAlexClient()
    search_engine = HybridSearchEngine(db)

    @server.tool(
        name="kb_search_literature",
        description=(
            "Searches scientific papers for concepts, methodologies, or citations. "
            "Returns ranked chunks with section lineage, BibTeX citekeys, and relevance scores."
        ),
    )
    async def kb_search_literature(
        query: str,
        citekey: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Searches literature using hybrid ranking (sparse keyword + dense vector fusion)."""
        async with db.get_session() as session:
            results = await search_engine.hybrid_search(
                session=session,
                query_text=query,
                query_vector=None,
                embedder=active_embedder,
                limit=limit,
                citekey=citekey,
            )

            hits: list[dict[str, Any]] = []
            for r in results:
                hits.append(
                    {
                        "chunk_id": r.chunk_id,
                        "document_id": r.document_id,
                        "citekey": r.citekey,
                        "section_path": r.section_path,
                        "parent_section": r.parent_section,
                        "text": r.text,
                        "rrf_score": r.rrf_score,
                        "dense_rank": r.dense_rank,
                        "sparse_rank": r.sparse_rank,
                        "dense_score": r.dense_score,
                        "sparse_score": r.sparse_score,
                        "has_math": r.has_math,
                        "has_table": r.has_table,
                    }
                )
            return hits

    @server.tool(
        name="kb_get_formula",
        description=(
            "Retrieves verified mathematical formulas extracted from papers. "
            "Returns sanitized LaTeX, SymPy symbolic representation, and LHS/RHS equations."
        ),
    )
    async def kb_get_formula(
        citekey: str | None = None,
        formula_id: str | None = None,
        query: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Finds formulas matching a citekey, formula ID, or symbol query."""
        async with db.get_session() as session:
            stmt = select(Formula).limit(limit)
            if formula_id:
                stmt = stmt.where(Formula.id == formula_id)
            elif citekey:
                stmt = stmt.where(Formula.citekey == citekey)

            res = await session.execute(stmt)
            formulas = list(res.scalars().all())

            results: list[dict[str, Any]] = []
            for f in formulas:
                if query:
                    q = query.lower()
                    in_symbols = any(q in s.lower() for s in f.symbols)
                    in_latex = q in f.sanitized_latex.lower() or q in f.raw_latex.lower()
                    if not (in_symbols or in_latex):
                        continue

                results.append(
                    {
                        "formula_id": f.id,
                        "citekey": f.citekey,
                        "document_id": f.document_id,
                        "raw_latex": f.raw_latex,
                        "sanitized_latex": f.sanitized_latex,
                        "sympy_repr": f.sympy_repr,
                        "symbols": f.symbols,
                        "is_valid": f.is_valid,
                        "is_equality": f.is_equality,
                        "lhs": f.lhs,
                        "rhs": f.rhs,
                    }
                )
            return results

    @server.tool(
        name="kb_compile_formula",
        description=(
            "Compiles a scientific formula into executable Python code and a vectorized Polars expression. "
            "Returns typed python_source, polars_expression, parameters, and validity status."
        ),
    )
    async def kb_compile_formula(
        formula_id: str | None = None,
        citekey: str | None = None,
    ) -> dict[str, Any]:
        """Compile a formula to Python/Polars code."""
        compiler = FormulaCompiler()
        async with db.get_session() as session:
            stmt = select(Formula).where(Formula.is_valid.is_(True))
            if formula_id:
                stmt = stmt.where(Formula.id == formula_id)
            elif citekey:
                stmt = stmt.where(Formula.citekey == citekey)
            stmt = stmt.limit(1)

            res = await session.execute(stmt)
            f = res.scalar_one_or_none()
            if not f:
                return {"error": "Formula not found", "is_valid": False}

            comp_res = compiler.compile(
                formula_id=f.id,
                citekey=f.citekey,
                raw_latex=f.sanitized_latex or f.raw_latex,
                sympy_repr=f.sympy_repr,
            )
            return comp_res.to_dict()

    @server.tool(
        name="kb_execute_formula",
        description=(
            "Executes a compiled scientific formula with numerical input parameters. "
            "Returns the calculated float result and execution status."
        ),
    )
    async def kb_execute_formula(
        formula_id: str,
        parameters: dict[str, float],
    ) -> dict[str, Any]:
        """Execute a formula dynamically with given numeric parameters."""
        compiler = FormulaCompiler()
        verifier = FormulaVerifier(compiler=compiler)
        async with db.get_session() as session:
            stmt = select(Formula).where(Formula.id == formula_id).limit(1)
            res = await session.execute(stmt)
            f = res.scalar_one_or_none()
            if not f:
                return {"error": f"Formula '{formula_id}' not found", "success": False}

            comp_res = compiler.compile(
                formula_id=f.id,
                citekey=f.citekey,
                raw_latex=f.sanitized_latex or f.raw_latex,
                sympy_repr=f.sympy_repr,
            )
            if not comp_res.is_valid or not comp_res.python_source:
                return {"error": comp_res.error or "Compilation failed", "success": False}

            v_res = verifier.verify_with_inputs(comp_res, parameters)
            if not v_res.passed or not v_res.predicted_samples:
                return {"error": v_res.details, "success": False}

            return {
                "formula_id": formula_id,
                "citekey": f.citekey,
                "result": v_res.predicted_samples[0],
                "parameters": parameters,
                "success": True,
            }

    @server.tool(
        name="kb_get_benchmark_table",
        description=(
            "Retrieves empirical benchmark datasets and tables from scientific papers. "
            "Returns table schemas, dimensions, and golden fixture Parquet/CSV file paths."
        ),
    )
    async def kb_get_benchmark_table(
        citekey: str | None = None,
        table_id: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Finds benchmark tables matching a citekey or table ID."""
        async with db.get_session() as session:
            stmt = select(BenchmarkTable).limit(limit)
            if table_id:
                stmt = stmt.where(BenchmarkTable.id == table_id)
            elif citekey:
                stmt = stmt.where(BenchmarkTable.citekey == citekey)

            res = await session.execute(stmt)
            tables = list(res.scalars().all())

            results: list[dict[str, Any]] = []
            for t in tables:
                results.append(
                    {
                        "table_id": t.id,
                        "citekey": t.citekey,
                        "caption": t.caption,
                        "num_rows": t.num_rows,
                        "num_cols": t.num_cols,
                        "column_names": t.column_names,
                        "parquet_path": t.parquet_path,
                        "csv_path": t.csv_path,
                        "schema_metadata": t.schema_metadata,
                    }
                )
            return results

    @server.tool(
        name="kb_get_bibtex",
        description="Retrieves a complete, valid BibTeX citation entry for a given citekey.",
    )
    async def kb_get_bibtex(citekey: str) -> str:
        """Generates BibTeX formatted string for a paper."""
        async with db.get_session() as session:
            stmt = select(Document).where(Document.citekey == citekey)
            res = await session.execute(stmt)
            doc = res.scalar_one_or_none()

            if doc is None:
                return f"% Citation key '{citekey}' not found in KB database."

            authors_str = " and ".join(doc.authors) if doc.authors else "Unknown"
            year_val = str(doc.year) if doc.year is not None else ""
            doi_entry = f"  doi = {{{doc.doi}}},\n" if doc.doi else ""
            eprint_entry = f"  eprint = {{{doc.arxiv_id}}},\n" if doc.arxiv_id else ""

            bibtex = (
                f"@article{{{doc.citekey},\n"
                f"  title = {{{doc.title}}},\n"
                f"  author = {{{authors_str}}},\n"
                f"  year = {{{year_val}}},\n"
                f"{doi_entry}"
                f"{eprint_entry}"
                f"}}"
            )
            return bibtex

    @server.tool(
        name="kb_get_citations",
        description=(
            "Retrieves papers citing or referenced by a scientific work in the knowledge base. "
            "Returns titles, publication years, cited-by counts, and OpenAlex IDs."
        ),
    )
    async def kb_get_citations(
        citekey: str | None = None,
        openalex_id: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Finds papers citing the specified work via OpenAlex."""
        target_id = openalex_id
        if not target_id and citekey:
            async with db.get_session() as session:
                res = await session.execute(select(Document).where(Document.citekey == citekey))
                doc = res.scalar_one_or_none()
                if doc:
                    target_id = doc.openalex_id

        if not target_id:
            return []

        citing_works = await active_openalex.get_citations(target_id, limit=limit)
        return [
            {
                "id": w.id,
                "short_id": w.short_id,
                "title": w.title,
                "year": w.publication_year,
                "cited_by_count": w.cited_by_count,
                "authors": w.authors,
                "doi": w.doi,
            }
            for w in citing_works
        ]

    @server.tool(
        name="kb_get_related_papers",
        description=(
            "Retrieves related research papers by topic classification and citation lineage. "
            "Returns related paper titles, topics, citation counts, and landing page URLs."
        ),
    )
    async def kb_get_related_papers(
        citekey: str | None = None,
        openalex_id: str | None = None,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Finds conceptually and methodologically related research papers via OpenAlex."""
        target_id = openalex_id
        if not target_id and citekey:
            async with db.get_session() as session:
                res = await session.execute(select(Document).where(Document.citekey == citekey))
                doc = res.scalar_one_or_none()
                if doc:
                    target_id = doc.openalex_id

        if not target_id:
            return []

        related_works = await active_openalex.get_related_papers(target_id, limit=limit)
        return [
            {
                "id": w.id,
                "short_id": w.short_id,
                "title": w.title,
                "year": w.publication_year,
                "cited_by_count": w.cited_by_count,
                "topics": [t["name"] for t in w.topics],
                "landing_page_url": w.landing_page_url,
                "authors": w.authors,
            }
            for w in related_works
        ]

    return server


# Default module-level server instance
mcp = create_mcp_server()

if __name__ == "__main__":
    mcp.run()
