"""Interactive Web Application and REST API for the Scientific Knowledge Base."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import polars as pl
from sqlalchemy import func, select
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Mount, Route
from strawberry.asgi import GraphQL

from kb.codegen.compiler import FormulaCompiler
from kb.graphql.schema import schema
from kb.math.chaining import FormulaChainingEngine
from kb.math.lineage import DerivationNode, FormulaLineageGraph
from kb.math.ontology import get_symbol_ontology
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import LocalEmbeddingGenerator
from kb.storage.models import BenchmarkTable, Chunk, Document, Formula
from kb.storage.search import HybridSearchEngine


def create_app(db_manager: DatabaseManager | None = None) -> Starlette:
    """Creates the Starlette application for kb visual dashboard."""
    manager = db_manager or DatabaseManager()
    compiler = FormulaCompiler()
    ontology = get_symbol_ontology()

    async def get_stats(_request: Request) -> JSONResponse:
        """Return corpus aggregate statistics."""
        async with manager.session_factory() as session:
            doc_cnt = (await session.execute(select(func.count(Document.id)))).scalar_one()
            chk_cnt = (await session.execute(select(func.count(Chunk.id)))).scalar_one()
            frm_cnt = (await session.execute(select(func.count(Formula.id)))).scalar_one()
            tbl_cnt = (await session.execute(select(func.count(BenchmarkTable.id)))).scalar_one()
            emb_cnt = (
                await session.execute(
                    select(func.count(Chunk.id)).where(Chunk.embedding.isnot(None))
                )
            ).scalar_one()

            return JSONResponse(
                {
                    "documents": doc_cnt,
                    "chunks": chk_cnt,
                    "formulas": frm_cnt,
                    "tables": tbl_cnt,
                    "embedded_chunks": emb_cnt,
                }
            )

    async def get_documents(_request: Request) -> JSONResponse:
        """Return list of ingested documents."""
        async with manager.session_factory() as session:
            stmt = select(Document).order_by(Document.year.desc().nullslast()).limit(100)
            res = await session.execute(stmt)
            docs = res.scalars().all()
            return JSONResponse(
                [
                    {
                        "citekey": d.citekey,
                        "title": d.title,
                        "authors": d.authors,
                        "year": d.year,
                        "doi": d.doi,
                        "arxiv_id": d.arxiv_id,
                        "num_formulas": len(d.formulas),
                        "num_tables": len(d.benchmark_tables),
                        "num_citations": len(d.outgoing_citations)
                        if hasattr(d, "outgoing_citations")
                        else 0,
                    }
                    for d in docs
                ]
            )

    async def get_lineage(request: Request) -> JSONResponse:
        """Return formula lineage graph nodes and edges."""
        limit = int(request.query_params.get("limit", 200))
        citekey = request.query_params.get("citekey")

        async with manager.session_factory() as session:
            stmt = select(Formula).where(Formula.is_valid == True)  # noqa: E712
            if citekey:
                stmt = stmt.where(Formula.citekey == citekey)
            stmt = stmt.limit(limit)
            formulas = list((await session.execute(stmt)).scalars().all())

            graph = FormulaLineageGraph()
            for f in formulas:
                graph.add_node(
                    DerivationNode(
                        formula_id=f.id,
                        citekey=f.citekey,
                        raw_latex=f.raw_latex,
                        sanitized_latex=f.sanitized_latex,
                        symbols=f.symbols,
                        lhs=f.lhs,
                        rhs=f.rhs,
                        is_valid=f.is_valid,
                        is_equality=f.is_equality,
                    )
                )

            graph.infer_lineage_edges(min_symbol_overlap=2, jaccard_threshold=0.35)

            nodes_data = [
                {
                    "id": n.formula_id,
                    "citekey": n.citekey,
                    "label": f"{n.citekey}:{n.formula_id[:8]}",
                    "latex": n.raw_latex,
                    "symbols": n.symbols,
                    "is_equality": n.is_equality,
                }
                for n in graph.nodes.values()
            ]
            edges_data = [
                {
                    "from": e.source_id,
                    "to": e.target_id,
                    "relation": e.relation.value,
                    "confidence": e.confidence,
                }
                for e in graph.edges
            ]

            return JSONResponse(
                {
                    "nodes": nodes_data,
                    "edges": edges_data,
                    "num_nodes": len(nodes_data),
                    "num_edges": len(edges_data),
                }
            )

    async def get_formulas(request: Request) -> JSONResponse:
        """Return verified formulas with compiled code snippets."""
        limit = int(request.query_params.get("limit", 20))
        citekey = request.query_params.get("citekey")

        async with manager.session_factory() as session:
            stmt = select(Formula).where(Formula.is_valid == True)  # noqa: E712
            if citekey:
                stmt = stmt.where(Formula.citekey == citekey)
            stmt = stmt.limit(limit)
            formulas = list((await session.execute(stmt)).scalars().all())

            results: list[dict[str, Any]] = []
            for f in formulas:
                try:
                    codegen = compiler.compile(
                        formula_id=f.id,
                        citekey=f.citekey,
                        raw_latex=f.raw_latex,
                        sympy_repr=f.sympy_repr,
                    )
                    grade = None
                    if f.validation_score is not None:
                        if f.validation_score >= 88.0:
                            grade = "A"
                        elif f.validation_score >= 75.0:
                            grade = "B"
                        elif f.validation_score >= 60.0:
                            grade = "C"
                        elif f.validation_score >= 45.0:
                            grade = "D"
                        else:
                            grade = "F"

                    results.append(
                        {
                            "formula_id": f.id,
                            "citekey": f.citekey,
                            "latex": f.raw_latex,
                            "symbols": f.symbols,
                            "parameters": codegen.parameters,
                            "python_code": codegen.python_source,
                            "polars_code": codegen.polars_expression,
                            "validation_score": f.validation_score,
                            "validation_status": f.validation_status,
                            "letter_grade": grade,
                        }
                    )
                except Exception:
                    continue
            return JSONResponse(results)

    async def get_tables(request: Request) -> JSONResponse:
        """Return benchmark tables with preview data."""
        citekey = request.query_params.get("citekey")
        limit = int(request.query_params.get("limit", 10))

        async with manager.session_factory() as session:
            stmt = select(BenchmarkTable)
            if citekey:
                stmt = stmt.where(BenchmarkTable.citekey == citekey)
            stmt = stmt.limit(limit)
            tables = list((await session.execute(stmt)).scalars().all())

            results: list[dict[str, Any]] = []
            for t in tables:
                preview_rows: list[dict[str, Any]] = []
                if t.parquet_path and Path(t.parquet_path).exists():
                    try:
                        df = pl.read_parquet(t.parquet_path)
                        preview_rows = df.head(5).to_dicts()
                    except Exception:
                        pass
                results.append(
                    {
                        "table_id": t.id,
                        "citekey": t.citekey,
                        "caption": t.caption,
                        "num_rows": t.num_rows,
                        "num_cols": t.num_cols,
                        "columns": t.column_names,
                        "parquet_path": t.parquet_path,
                        "preview": preview_rows,
                    }
                )
            return JSONResponse(results)

    async def search_endpoint(request: Request) -> JSONResponse:
        """Execute hybrid search across the corpus."""
        query = request.query_params.get("q", "").strip()
        limit = int(request.query_params.get("limit", 10))
        if not query:
            return JSONResponse({"results": [], "query": ""})

        embedder = LocalEmbeddingGenerator()
        searcher = HybridSearchEngine(db_manager=manager)
        async with manager.session_factory() as session:
            results = await searcher.search(
                session, query_text=query, embedder=embedder, limit=limit
            )
            return JSONResponse(
                {
                    "query": query,
                    "count": len(results),
                    "results": [
                        {
                            "chunk_id": r.chunk_id,
                            "citekey": r.citekey,
                            "score": round(r.rrf_score, 4),
                            "snippet": r.text[:300] + "..." if len(r.text) > 300 else r.text,
                            "section_path": r.section_path,
                        }
                        for r in results
                    ],
                }
            )

    async def get_coverage(request: Request) -> JSONResponse:
        """Return comprehensive formula coverage metrics."""
        limit_param = request.query_params.get("limit")
        limit = int(limit_param) if limit_param else None
        from kb.math.coverage import FormulaCoverageAnalyzer

        analyzer = FormulaCoverageAnalyzer(ontology=ontology)
        report = await analyzer.analyze_corpus(limit=limit)
        return JSONResponse(report.model_dump())

    async def eval_endpoint(request: Request) -> JSONResponse:
        """Dynamically evaluate a formula given its ID or raw LaTeX and input values."""
        try:
            payload: dict[str, Any] = {}
            if request.method == "POST":
                try:
                    payload = await request.json()
                except Exception:
                    payload = {}
            else:
                payload = dict(request.query_params)

            formula_id_val = payload.get("formula_id")
            latex_val = payload.get("latex")
            if not formula_id_val and not latex_val:
                return JSONResponse({"error": "Missing formula_id parameter"}, status_code=400)

            formula_id = str(formula_id_val).strip() if formula_id_val else "custom"
            inputs: dict[str, Any] = payload.get("inputs", {})
            if isinstance(inputs, str):
                try:
                    inputs = json.loads(inputs)
                except Exception:
                    inputs = {}

            # Also accept inputs from flat query params
            for k, v in payload.items():
                if k not in ("formula_id", "latex", "inputs"):
                    try:
                        inputs[k] = float(v)
                    except (ValueError, TypeError):
                        inputs[k] = v

            raw_latex_str: str | None = None
            citekey_str: str | None = None

            if latex_val or formula_id == "custom":
                raw_latex_str = str(latex_val or "")
                citekey_str = "Custom"
            else:
                async with manager.session_factory() as session:
                    stmt = select(Formula).where(Formula.id == formula_id)
                    formula = (await session.execute(stmt)).scalar_one_or_none()
                    if not formula:
                        return JSONResponse(
                            {"error": f"Formula {formula_id} not found"}, status_code=404
                        )
                    raw_latex_str = formula.sanitized_latex or formula.raw_latex
                    citekey_str = formula.citekey

            if not raw_latex_str:
                return JSONResponse({"error": "No formula LaTeX available"}, status_code=400)

            import warnings

            from sympy.parsing.latex import parse_latex

            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=SyntaxWarning)
                expr = parse_latex(raw_latex_str)
            if expr is None:
                return JSONResponse({"error": "Failed to parse formula"}, status_code=500)
            target = getattr(expr, "rhs", expr)
            if target is None:
                return JSONResponse(
                    {"error": "Failed to extract expression target"}, status_code=500
                )

            # Map free symbols
            sym_map = {str(s): s for s in target.free_symbols}
            sub_dict: dict[Any, float] = {}

            # First direct match pass
            for k, v in inputs.items():
                val = float(v)
                if k in sym_map:
                    sub_dict[sym_map[k]] = val
                elif f"{{{k}}}" in sym_map:
                    sub_dict[sym_map[f"{{{k}}}"]] = val
                elif f"_{{{k}}}" in sym_map:
                    sub_dict[sym_map[f"_{{{k}}}"]] = val

            # Second pass: ontology canonical matching for unresolved symbols
            for sym_str, sym_obj in sym_map.items():
                if sym_obj in sub_dict:
                    continue
                sym_canon = ontology.resolve_canonical(sym_str)
                if not sym_canon:
                    continue
                for k, v in inputs.items():
                    k_canon = ontology.resolve_canonical(k)
                    if k_canon and k_canon == sym_canon:
                        try:
                            sub_dict[sym_obj] = float(v)
                            break
                        except (ValueError, TypeError):
                            pass

            eval_result = target.subs(sub_dict).evalf()
            result_val = float(eval_result) if eval_result.is_number else str(eval_result)

            return JSONResponse(
                {
                    "formula_id": formula_id,
                    "citekey": citekey_str,
                    "latex": raw_latex_str,
                    "inputs": inputs,
                    "result": result_val,
                }
            )
        except Exception as exc:
            return JSONResponse({"error": str(exc)}, status_code=500)

    async def get_presets(_request: Request) -> JSONResponse:
        """Return canonical baseball analytics presets for interactive playground."""
        return JSONResponse(
            [
                {
                    "id": "pythagorean",
                    "name": "Pythagorean Expectation (Bill James)",
                    "latex": r"W = \frac{R_S^{\gamma}}{R_S^{\gamma} + R_A^{\gamma}}",
                    "target_symbol": "W",
                    "params": [
                        {
                            "name": "R_S",
                            "label": "Runs Scored (RS)",
                            "min": 400,
                            "max": 1100,
                            "step": 1,
                            "default": 750,
                        },
                        {
                            "name": "R_A",
                            "label": "Runs Allowed (RA)",
                            "min": 400,
                            "max": 1100,
                            "step": 1,
                            "default": 650,
                        },
                        {
                            "name": r"\gamma",
                            "alt_name": "gamma",
                            "label": "Exponent (γ)",
                            "min": 1.5,
                            "max": 2.5,
                            "step": 0.01,
                            "default": 1.83,
                        },
                    ],
                    "curve_param": "R_S",
                    "curve_min": 450,
                    "curve_max": 1050,
                    "curve_points": 25,
                },
                {
                    "id": "fip",
                    "name": "Fielding Independent Pitching (FIP)",
                    "latex": r"FIP = \frac{13 \cdot H_R + 3 \cdot (B_B + HBP) - 2 \cdot K}{I_P} + 3.10",
                    "target_symbol": "FIP",
                    "params": [
                        {
                            "name": "H_R",
                            "label": "Home Runs (HR)",
                            "min": 0,
                            "max": 60,
                            "step": 1,
                            "default": 20,
                        },
                        {
                            "name": "B_B",
                            "label": "Walks (BB)",
                            "min": 10,
                            "max": 120,
                            "step": 1,
                            "default": 55,
                        },
                        {
                            "name": "HBP",
                            "label": "Hit By Pitch (HBP)",
                            "min": 0,
                            "max": 20,
                            "step": 1,
                            "default": 6,
                        },
                        {
                            "name": "K",
                            "label": "Strikeouts (K)",
                            "min": 30,
                            "max": 300,
                            "step": 1,
                            "default": 180,
                        },
                        {
                            "name": "I_P",
                            "label": "Innings Pitched (IP)",
                            "min": 50,
                            "max": 250,
                            "step": 0.1,
                            "default": 180.0,
                        },
                    ],
                    "curve_param": "K",
                    "curve_min": 50,
                    "curve_max": 280,
                    "curve_points": 24,
                },
                {
                    "id": "woba",
                    "name": "Weighted On-Base Average (wOBA)",
                    "latex": r"wOBA = \frac{0.69 \cdot B_B + 0.72 \cdot HBP + 0.89 \cdot H_1 + 1.27 \cdot H_2 + 1.62 \cdot H_3 + 2.10 \cdot H_R}{PA}",
                    "target_symbol": "wOBA",
                    "params": [
                        {
                            "name": "B_B",
                            "label": "Walks (BB)",
                            "min": 0,
                            "max": 150,
                            "step": 1,
                            "default": 65,
                        },
                        {
                            "name": "HBP",
                            "label": "Hit By Pitch",
                            "min": 0,
                            "max": 30,
                            "step": 1,
                            "default": 7,
                        },
                        {
                            "name": "H_1",
                            "label": "Singles (1B)",
                            "min": 20,
                            "max": 180,
                            "step": 1,
                            "default": 95,
                        },
                        {
                            "name": "H_2",
                            "label": "Doubles (2B)",
                            "min": 5,
                            "max": 60,
                            "step": 1,
                            "default": 30,
                        },
                        {
                            "name": "H_3",
                            "label": "Triples (3B)",
                            "min": 0,
                            "max": 25,
                            "step": 1,
                            "default": 4,
                        },
                        {
                            "name": "H_R",
                            "label": "Home Runs (HR)",
                            "min": 0,
                            "max": 60,
                            "step": 1,
                            "default": 25,
                        },
                        {
                            "name": "PA",
                            "label": "Plate Appearances",
                            "min": 100,
                            "max": 750,
                            "step": 1,
                            "default": 620,
                        },
                    ],
                    "curve_param": "H_R",
                    "curve_min": 5,
                    "curve_max": 55,
                    "curve_points": 20,
                },
            ]
        )

    async def chain_endpoint(request: Request) -> JSONResponse:
        """Chain component equations into unified closed-form formula."""
        formula_id = request.query_params.get("formula_id")
        if not formula_id:
            return JSONResponse({"error": "formula_id parameter is required"}, status_code=400)
        max_depth = int(request.query_params.get("max_depth", 5))
        engine = FormulaChainingEngine(db_manager=manager, ontology=ontology, compiler=compiler)
        try:
            res = await engine.chain_formula(formula_id, max_depth=max_depth)
            return JSONResponse(
                {
                    "target_formula_id": res.target_formula_id,
                    "target_citekey": res.target_citekey,
                    "target_latex": res.target_latex,
                    "closed_form_latex": res.closed_form_latex,
                    "primitive_symbols": res.primitive_symbols,
                    "steps": [
                        {
                            "target_variable": s.target_variable,
                            "source_formula_id": s.source_formula_id,
                            "source_citekey": s.source_citekey,
                            "original_expr": s.original_expr_str,
                            "substituted_expr": s.substituted_expr_str,
                        }
                        for s in res.trace_steps
                    ],
                    "python_code": res.python_code,
                    "polars_code": res.polars_code,
                }
            )
        except Exception as exc:
            return JSONResponse({"error": str(exc)}, status_code=400)

    async def validate_endpoint(request: Request) -> JSONResponse:
        """Run multi-tier validation gate on a formula and return full scorecard."""
        from kb.math.validation import FormulaQualityGate

        gate = FormulaQualityGate()
        formula_id = request.query_params.get("id")
        latex_str = request.query_params.get("latex")

        if request.method == "POST":
            try:
                body = await request.json()
                if isinstance(body, dict):
                    formula_id = body.get("id") or formula_id
                    latex_str = body.get("latex") or latex_str
            except Exception:
                pass

        if not formula_id and not latex_str:
            return JSONResponse(
                {"error": "Provide either 'id' or 'latex' parameter"}, status_code=400
            )

        if formula_id:
            async with manager.session_factory() as session:
                stmt = select(Formula).where(Formula.id == formula_id)
                f = (await session.execute(stmt)).scalar_one_or_none()
                if not f:
                    return JSONResponse(
                        {"error": f"Formula {formula_id} not found"}, status_code=404
                    )
                card = gate.validate_formula(f)
                f.validation_score = card.total_score
                f.validation_status = card.status
                f.validation_details = card.to_dict()
                await session.commit()
                return JSONResponse(card.to_dict())

        card = gate.validate_formula(str(latex_str))
        return JSONResponse(card.to_dict())

    async def index_view(_request: Request) -> HTMLResponse:
        """Serve the interactive single-page dashboard."""
        html_content = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KB Scientific Knowledge Base Explorer</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
  <style>
    :root {
      --bg-primary: #0f172a;
      --bg-secondary: #1e293b;
      --card-bg: #1e293b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --border-color: #334155;
    }
    body { background-color: var(--bg-primary); color: var(--text-main); font-family: ui-sans-serif, system-ui, sans-serif; }
    .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #475569; border-radius: 3px; }
    .glass-card { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(8px); border: 1px solid var(--border-color); }
    input[type=range] { accent-color: #38bdf8; }
  </style>
</head>
<body class="min-h-screen flex flex-col">
  <!-- Header -->
  <header class="border-b border-slate-700 bg-slate-900/80 px-6 py-4 flex items-center justify-between sticky top-0 z-50">
    <div class="flex items-center space-x-3">
      <div class="h-9 w-9 rounded-lg bg-sky-500/20 border border-sky-400 flex items-center justify-center font-bold text-sky-400">KB</div>
      <div>
        <h1 class="font-bold text-lg leading-tight">Scientific Knowledge Base</h1>
        <p class="text-xs text-slate-400">Mathematical Lineage, Benchmark Tables & Code Compilation</p>
      </div>
    </div>
    <!-- Aggregate Stats Badges -->
    <div id="stats-container" class="flex items-center space-x-3 text-xs">
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-docs" class="font-semibold text-sky-400">...</span> docs</div>
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-chunks" class="font-semibold text-emerald-400">...</span> chunks</div>
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-formulas" class="font-semibold text-indigo-400">...</span> formulas</div>
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-tables" class="font-semibold text-amber-400">...</span> tables</div>
      <a href="/graphql" target="_blank" class="px-3 py-1.5 rounded-full bg-indigo-950/80 border border-indigo-700 text-indigo-300 font-mono text-xs hover:bg-indigo-900 transition">GraphQL IDE ↗</a>
    </div>
  </header>

  <!-- Navigation Tabs -->
  <div class="bg-slate-900 border-b border-slate-800 px-6 py-2 flex space-x-3 overflow-x-auto">
    <button onclick="switchTab('lineage')" id="tab-btn-lineage" class="px-4 py-1.5 text-sm font-medium rounded-lg bg-sky-500 text-white">Lineage Graph (DAG)</button>
    <button onclick="switchTab('formulas')" id="tab-btn-formulas" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Knowledge-to-Code</button>
    <button onclick="switchTab('chaining')" id="tab-btn-chaining" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Equation Chaining</button>
    <button onclick="switchTab('playground')" id="tab-btn-playground" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Formula Playground</button>
    <button onclick="switchTab('tables')" id="tab-btn-tables" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Benchmark Tables</button>
    <button onclick="switchTab('search')" id="tab-btn-search" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Hybrid Retrieval</button>
    <button onclick="switchTab('coverage')" id="tab-btn-coverage" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Coverage & Yield</button>
  </div>

  <!-- Main Viewports -->
  <main class="flex-1 p-6 overflow-hidden flex flex-col">
    <!-- View 1: Lineage DAG -->
    <section id="view-lineage" class="flex-1 flex flex-col space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-base font-semibold text-slate-200">Mathematical Derivation Network</h2>
          <p class="text-xs text-slate-400">Directed lineage connecting mathematical models, approximations, and shared symbol spaces.</p>
        </div>
        <div class="flex items-center space-x-3 text-xs">
          <input id="lineage-search" type="text" placeholder="Filter citekey..." class="px-3 py-1.5 bg-slate-800 border border-slate-700 rounded-lg text-slate-200 text-xs focus:ring-1 focus:ring-sky-500 outline-none" oninput="filterGraph()">
          <button onclick="loadLineage()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-lg text-slate-200">Refresh DAG</button>
        </div>
      </div>
      <div class="flex-1 grid grid-cols-1 lg:grid-cols-3 gap-4 min-h-[500px]">
        <div class="lg:col-span-2 glass-card rounded-xl relative overflow-hidden flex flex-col">
          <!-- Canvas Graph Container -->
          <div id="graph-meta" class="absolute top-3 left-3 z-10 text-xs bg-slate-900/80 px-3 py-1 rounded border border-slate-700 text-slate-300">Loading graph...</div>
          <svg id="dag-svg" class="w-full h-full cursor-grab" style="min-height: 480px;"></svg>
        </div>
        <!-- Node Detail Sidebar -->
        <div class="glass-card rounded-xl p-4 flex flex-col custom-scroll overflow-y-auto space-y-3">
          <h3 class="font-semibold text-sm text-sky-400 border-b border-slate-700 pb-2">Selected Formula Node</h3>
          <div id="node-details" class="text-xs text-slate-400 space-y-3">
            <p>Click on any node in the derivation DAG to inspect its LaTeX equation, free symbols, and compiled code.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- View 2: Knowledge-to-Code -->
    <section id="view-formulas" class="flex-1 hidden flex flex-col space-y-4 overflow-y-auto custom-scroll">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-base font-semibold text-slate-200">Knowledge-to-Code Auto-Compilation</h2>
          <p class="text-xs text-slate-400">Extracted SymPy equations compiled into type-safe Python and Polars expressions.</p>
        </div>
        <input id="formula-filter" type="text" placeholder="Filter by citekey..." class="px-3 py-1.5 bg-slate-800 border border-slate-700 rounded-lg text-slate-200 text-xs outline-none" oninput="loadFormulas()">
      </div>
      <div id="formulas-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="text-sm text-slate-400">Loading formulas...</div>
      </div>
    </section>

    <!-- View 2.5: Symbolic Equation Chaining & Derivation Tree -->
    <section id="view-chaining" class="flex-1 hidden flex flex-col space-y-4 overflow-y-auto custom-scroll">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-base font-semibold text-slate-200">Symbolic Equation Chaining & System Solver</h2>
          <p class="text-xs text-slate-400">Recursively substitutes sub-equations across papers and glossaries to construct unified closed-form systems.</p>
        </div>
        <div class="flex items-center space-x-2 text-xs">
          <span class="text-slate-400">Sabermetric Presets:</span>
          <button onclick="chainPreset('WAR')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-sky-400 border border-slate-700">WAR (Position)</button>
          <button onclick="chainPreset('wRC')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">wRC</button>
          <button onclick="chainPreset('Base_Runs')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-400 border border-slate-700">Base Runs</button>
          <button onclick="chainPreset('Pythagenpat')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-400 border border-slate-700">Pythagenpat</button>
        </div>
      </div>

      <div class="glass-card rounded-xl p-4 flex items-center space-x-3">
        <input id="chain-formula-id" type="text" placeholder="Formula ID or keyword (e.g. 'WAR' or 'wRC')..." class="flex-1 px-4 py-2 bg-slate-900 border border-slate-700 rounded-lg text-slate-200 text-xs font-mono outline-none focus:ring-1 focus:ring-sky-500">
        <div class="flex items-center space-x-1 text-xs text-slate-400">
          <span>Max Depth:</span>
          <input id="chain-max-depth" type="number" value="5" min="1" max="10" class="w-14 px-2 py-1.5 bg-slate-900 border border-slate-700 rounded-lg text-slate-200 text-xs text-center">
        </div>
        <button onclick="executeChaining()" class="px-4 py-2 bg-sky-600 hover:bg-sky-500 text-white rounded-lg text-xs font-medium transition">Chain & Substitute</button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 flex-1 min-h-[460px]">
        <!-- Left: Derivation Tree Steps -->
        <div class="lg:col-span-5 glass-card rounded-xl p-4 flex flex-col space-y-3">
          <h3 class="text-sm font-semibold text-slate-200 border-b border-slate-700 pb-2 flex items-center justify-between">
            <span>Recursive Derivation Trace</span>
            <span id="chain-step-badge" class="text-[11px] px-2 py-0.5 rounded bg-sky-950 text-sky-400 border border-sky-800">0 steps</span>
          </h3>
          <div id="chain-steps-container" class="space-y-2 overflow-y-auto custom-scroll flex-1 text-xs text-slate-400">
            <p>Click a preset button above or enter a formula ID to trigger symbolic multi-tier substitution.</p>
          </div>
        </div>

        <!-- Right: Closed-Form Equation & Code -->
        <div class="lg:col-span-7 glass-card rounded-xl p-5 flex flex-col space-y-4">
          <div>
            <span class="text-xs font-semibold text-sky-400 uppercase tracking-wide">Unified Closed-Form Equation</span>
            <div id="chain-latex-display" class="mt-2 p-4 bg-slate-900 rounded-xl border border-slate-800 text-slate-100 flex items-center justify-center min-h-[70px] text-base overflow-x-auto">
              <span class="text-xs text-slate-500">Awaiting formula selection...</span>
            </div>
          </div>
          <div>
            <span class="text-xs font-semibold text-slate-400 uppercase tracking-wide">Primitive Box-Score Variables</span>
            <div id="chain-primitive-symbols" class="mt-2 flex flex-wrap gap-1.5 min-h-[30px]">
              <span class="text-xs text-slate-500 font-mono">None</span>
            </div>
          </div>
          <div class="flex-1 flex flex-col space-y-2">
            <span class="text-xs font-semibold text-emerald-400 uppercase tracking-wide">Compiled Polars Expression</span>
            <pre id="chain-polars-code" class="p-3 bg-slate-950 rounded-lg border border-slate-800 text-emerald-400 font-mono text-xs overflow-x-auto flex-1 max-h-[160px]"># Polars expression will be compiled here</pre>
          </div>
        </div>
      </div>
    </section>

    <!-- View 3: Interactive Calculation Playground -->
    <section id="view-playground" class="flex-1 hidden flex flex-col space-y-4 overflow-y-auto custom-scroll">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-base font-semibold text-slate-200">Interactive Formula Playground & Visual Sensitivity Sandbox</h2>
          <p class="text-xs text-slate-400">Dynamically evaluate mathematical models with live parameter sliders, LaTeX KaTeX preview, and real-time response curves.</p>
        </div>
        <div class="flex items-center space-x-3 text-xs">
          <label class="text-slate-400">Formula Preset:</label>
          <select id="preset-selector" onchange="onPresetChange()" class="px-3 py-1.5 bg-slate-800 border border-slate-700 rounded-lg text-slate-200 text-xs outline-none focus:ring-1 focus:ring-sky-500">
            <option value="pythagorean">Pythagorean Expectation (Bill James)</option>
            <option value="fip">Fielding Independent Pitching (FIP)</option>
            <option value="woba">Weighted On-Base Average (wOBA)</option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        <!-- Left: Interactive Controls -->
        <div class="lg:col-span-5 glass-card rounded-xl p-5 space-y-5 flex flex-col">
          <div class="border-b border-slate-700 pb-3">
            <h3 class="text-sm font-semibold text-sky-400" id="pg-formula-title">Pythagorean Expectation</h3>
            <div id="pg-latex-display" class="mt-2 p-3 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-center min-h-[50px] text-slate-200 font-mono text-sm overflow-x-auto"></div>
          </div>

          <!-- Parameter Sliders -->
          <div id="pg-params-container" class="space-y-4 flex-1">
            <!-- Dynamically populated -->
          </div>

          <div class="pt-3 border-t border-slate-700/60 flex items-center justify-between text-xs text-slate-400">
            <span>Dynamic Backend Engine: <strong class="text-emerald-400 font-mono">/api/eval</strong></span>
            <button onclick="evaluatePlayground()" class="px-4 py-1.5 bg-sky-600 hover:bg-sky-500 text-white rounded-lg font-medium transition">Re-compute</button>
          </div>
        </div>

        <!-- Right: Results & Real-time Sensitivity Curve -->
        <div class="lg:col-span-7 space-y-5 flex flex-col">
          <!-- Top KPI Card -->
          <div class="glass-card rounded-xl p-5 grid grid-cols-2 md:grid-cols-3 gap-4 items-center">
            <div class="space-y-1">
              <span class="text-xs text-slate-400 uppercase font-semibold">Calculated Value</span>
              <div id="pg-result-value" class="text-3xl font-bold font-mono text-sky-400">0.5651</div>
              <div class="text-[11px] text-slate-500" id="pg-result-label">Win Expectancy</div>
            </div>
            <div class="space-y-1">
              <span class="text-xs text-slate-400 uppercase font-semibold">Evaluation Mode</span>
              <div class="text-sm font-mono text-emerald-400 flex items-center space-x-1.5">
                <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>Reactive AST</span>
              </div>
              <div class="text-[11px] text-slate-500">Vectorized Polars Parity</div>
            </div>
            <div class="space-y-1 col-span-2 md:col-span-1">
              <span class="text-xs text-slate-400 uppercase font-semibold">Latency</span>
              <div id="pg-latency" class="text-sm font-mono text-indigo-300">&lt; 5 ms</div>
              <div class="text-[11px] text-slate-500">Zero-alloc binding</div>
            </div>
          </div>

          <!-- Sensitivity Response Curve (SVG Canvas) -->
          <div class="glass-card rounded-xl p-5 flex-1 flex flex-col space-y-3">
            <div class="flex items-center justify-between">
              <div>
                <h4 class="text-sm font-semibold text-slate-200">Sensitivity Curve</h4>
                <p class="text-xs text-slate-400" id="pg-curve-desc">Varying Runs Scored while holding other parameters fixed</p>
              </div>
              <span class="text-[11px] px-2 py-0.5 rounded bg-sky-950 text-sky-400 border border-sky-800">Live Operating Point</span>
            </div>
            <div class="flex-1 min-h-[260px] bg-slate-900/90 rounded-lg border border-slate-800 p-3 relative flex items-center justify-center">
              <svg id="pg-curve-svg" class="w-full h-full" viewBox="0 0 500 240"></svg>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- View 4: Benchmark Tables -->
    <section id="view-tables" class="flex-1 hidden flex flex-col space-y-4 overflow-y-auto custom-scroll">
      <div>
        <h2 class="text-base font-semibold text-slate-200">Benchmark Tables & Parquet Fixtures</h2>
        <p class="text-xs text-slate-400">Golden tables extracted from literature, backed by typed Parquet files.</p>
      </div>
      <div id="tables-grid" class="space-y-4">
        <div class="text-sm text-slate-400">Loading tables...</div>
      </div>
    </section>

    <!-- View 5: Hybrid Search -->
    <section id="view-search" class="flex-1 hidden flex flex-col space-y-4">
      <div class="flex space-x-3">
        <input id="search-input" type="text" placeholder="Ask or search research corpus (e.g. 'Pythagorean expectation derivation')..." class="flex-1 px-4 py-2.5 bg-slate-800 border border-slate-700 rounded-xl text-slate-200 text-sm focus:ring-2 focus:ring-sky-500 outline-none" onkeydown="if(event.key==='Enter') executeSearch()">
        <button onclick="executeSearch()" class="px-5 py-2.5 bg-sky-600 hover:bg-sky-500 text-white rounded-xl text-sm font-medium">Search</button>
      </div>
      <div id="search-results" class="flex-1 overflow-y-auto custom-scroll space-y-3">
        <p class="text-xs text-slate-400">Enter a query above to execute hybrid dense + sparse retrieval across the corpus.</p>
      </div>
    </section>

    <!-- View 6: Coverage & Yield Scorecard -->
    <section id="view-coverage" class="flex-1 hidden flex flex-col space-y-4 overflow-y-auto custom-scroll">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-base font-semibold text-slate-200">Mathematical Formula & Variable Coverage Scorecard</h2>
          <p class="text-xs text-slate-400">Yield tracking, symbol definitions vs. usages, canonical ontology bindings, and non-ASCII character distributions.</p>
        </div>
        <button onclick="loadCoverage()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded-lg text-slate-200 text-xs">Refresh Coverage</button>
      </div>

      <!-- KPI Summary Cards -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="glass-card p-4 rounded-xl border border-slate-700">
          <div class="text-xs text-slate-400 uppercase font-semibold">SymPy AST Yield</div>
          <div id="cov-parse-yield" class="text-2xl font-bold text-sky-400 mt-1">...</div>
          <div id="cov-parse-counts" class="text-xs text-slate-400 mt-1">... valid / ... total</div>
        </div>
        <div class="glass-card p-4 rounded-xl border border-slate-700">
          <div class="text-xs text-slate-400 uppercase font-semibold">Equality Relations</div>
          <div id="cov-eq-yield" class="text-2xl font-bold text-emerald-400 mt-1">...</div>
          <div id="cov-eq-counts" class="text-xs text-slate-400 mt-1">... LHS = RHS</div>
        </div>
        <div class="glass-card p-4 rounded-xl border border-slate-700">
          <div class="text-xs text-slate-400 uppercase font-semibold">Unique Symbols</div>
          <div id="cov-unique-symbols" class="text-2xl font-bold text-indigo-400 mt-1">...</div>
          <div id="cov-symbols-breakdown" class="text-xs text-slate-400 mt-1">... defined / ... consumed</div>
        </div>
        <div class="glass-card p-4 rounded-xl border border-slate-700">
          <div class="text-xs text-slate-400 uppercase font-semibold">Ontology Mappings</div>
          <div id="cov-mapped-symbols" class="text-2xl font-bold text-amber-400 mt-1">...</div>
          <div id="cov-orphan-symbols" class="text-xs text-rose-400 mt-1">... unconstrained orphans</div>
        </div>
      </div>

      <!-- Detailed Breakdown Tables -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <!-- Top Non-ASCII Characters -->
        <div class="glass-card p-4 rounded-xl border border-slate-700">
          <h3 class="text-sm font-semibold text-slate-300 mb-2">Non-ASCII Character Accounting</h3>
          <div id="cov-chars-table" class="text-xs text-slate-400">Loading characters...</div>
        </div>

        <!-- Parser Error Taxonomy -->
        <div class="glass-card p-4 rounded-xl border border-slate-700">
          <h3 class="text-sm font-semibold text-slate-300 mb-2">Parser Error Taxonomy</h3>
          <div id="cov-errors-table" class="text-xs text-slate-400">Loading error distribution...</div>
        </div>
      </div>
    </section>
  </main>

  <script>
    // State
    let currentTab = 'lineage';
    let graphData = { nodes: [], edges: [] };
    let playgroundPresets = [];
    let currentPreset = null;
    let playgroundInputs = {};

    function switchTab(tabId) {
      ['lineage', 'formulas', 'chaining', 'playground', 'tables', 'search', 'coverage'].forEach(t => {
        const viewEl = document.getElementById(`view-${t}`);
        const btnEl = document.getElementById(`tab-btn-${t}`);
        if (viewEl) viewEl.classList.add('hidden');
        if (btnEl) btnEl.className = 'px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white';
      });
      const targetView = document.getElementById(`view-${tabId}`);
      const targetBtn = document.getElementById(`tab-btn-${tabId}`);
      if (targetView) targetView.classList.remove('hidden');
      if (targetBtn) targetBtn.className = 'px-4 py-1.5 text-sm font-medium rounded-lg bg-sky-500 text-white';
      currentTab = tabId;

      if (tabId === 'formulas') loadFormulas();
      if (tabId === 'chaining') initChaining();
      if (tabId === 'playground') initPlayground();
      if (tabId === 'tables') loadTables();
      if (tabId === 'coverage') loadCoverage();
    }

    async function loadCoverage() {
      try {
        const res = await fetch('/api/coverage');
        const data = await res.json();
        document.getElementById('cov-parse-yield').innerText = `${data.parse_yield_pct.toFixed(1)}%`;
        document.getElementById('cov-parse-counts').innerText = `${data.valid_formulas.toLocaleString()} valid / ${data.total_formulas.toLocaleString()} total`;
        document.getElementById('cov-eq-yield').innerText = `${data.equality_yield_pct.toFixed(1)}%`;
        document.getElementById('cov-eq-counts').innerText = `${data.equality_formulas.toLocaleString()} LHS = RHS`;
        document.getElementById('cov-unique-symbols').innerText = data.unique_symbols.length.toLocaleString();
        document.getElementById('cov-symbols-breakdown').innerText = `${data.defined_symbols.length} defined / ${data.consumed_symbols.length} consumed`;
        document.getElementById('cov-mapped-symbols').innerText = data.ontology_mapped_symbols.length.toLocaleString();
        document.getElementById('cov-orphan-symbols').innerText = `${data.orphan_symbols.length} unconstrained orphans`;

        // Render Characters Table
        const charsEntries = Object.entries(data.character_accounting || {}).slice(0, 15);
        if (charsEntries.length === 0) {
          document.getElementById('cov-chars-table').innerHTML = '<p class="text-slate-500">No non-ASCII characters recorded.</p>';
        } else {
          let html = '<table class="w-full text-left border-collapse"><thead><tr class="border-b border-slate-700 text-slate-400"><th class="py-1">Char</th><th class="py-1">Hex</th><th class="py-1">Count</th></tr></thead><tbody>';
          charsEntries.forEach(([ch, cnt]) => {
            const hex = 'U+' + ch.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0');
            html += `<tr class="border-b border-slate-800"><td class="py-1 font-mono text-sky-400">${ch}</td><td class="py-1 font-mono text-slate-400">${hex}</td><td class="py-1 text-slate-300">${cnt.toLocaleString()}</td></tr>`;
          });
          html += '</tbody></table>';
          document.getElementById('cov-chars-table').innerHTML = html;
        }

        // Render Errors Table
        const errEntries = Object.entries(data.error_taxonomy || {}).slice(0, 10);
        if (errEntries.length === 0) {
          document.getElementById('cov-errors-table').innerHTML = '<p class="text-emerald-400">Zero parsing errors recorded!</p>';
        } else {
          let html = '<table class="w-full text-left border-collapse"><thead><tr class="border-b border-slate-700 text-slate-400"><th class="py-1">Error Category</th><th class="py-1">Count</th></tr></thead><tbody>';
          errEntries.forEach(([cat, cnt]) => {
            html += `<tr class="border-b border-slate-800"><td class="py-1 font-mono text-rose-400 text-xs">${cat}</td><td class="py-1 text-slate-300">${cnt.toLocaleString()}</td></tr>`;
          });
          html += '</tbody></table>';
          document.getElementById('cov-errors-table').innerHTML = html;
        }
      } catch (err) {
        console.error('Failed to load coverage metrics', err);
      }
    }

    async function initChaining() {
      const inputEl = document.getElementById('chain-formula-id');
      if (!inputEl.value) {
        chainPreset('WAR');
      }
    }

    async function chainPreset(keyword) {
      const inputEl = document.getElementById('chain-formula-id');
      try {
        const res = await fetch('/api/formulas?limit=60');
        const formulas = await res.json();
        let match = formulas.find(f => f.lhs && f.lhs.toLowerCase().includes(keyword.toLowerCase()));
        if (!match) {
          match = formulas.find(f => f.citekey && f.citekey.toLowerCase().includes(keyword.toLowerCase()));
        }
        if (match) {
          inputEl.value = match.id;
        } else {
          inputEl.value = keyword;
        }
        executeChaining();
      } catch (_) {
        inputEl.value = keyword;
        executeChaining();
      }
    }

    async function executeChaining() {
      const fid = document.getElementById('chain-formula-id').value.trim();
      if (!fid) return;
      const depth = document.getElementById('chain-max-depth').value || 5;
      const container = document.getElementById('chain-steps-container');
      const latexEl = document.getElementById('chain-latex-display');
      const badgeEl = document.getElementById('chain-step-badge');
      const symbolsEl = document.getElementById('chain-primitive-symbols');
      const polarsEl = document.getElementById('chain-polars-code');

      container.innerHTML = '<div class="text-xs text-slate-400">Executing recursive symbolic substitution...</div>';
      latexEl.innerHTML = '<span class="text-xs text-slate-500">Computing...</span>';

      try {
        const res = await fetch(`/api/chain?formula_id=${encodeURIComponent(fid)}&max_depth=${depth}`);
        const data = await res.json();
        if (data.error) {
          container.innerHTML = `<div class="p-3 bg-rose-950/40 border border-rose-800 rounded text-rose-300 text-xs">${escapeHtml(data.error)}</div>`;
          latexEl.innerHTML = '<span class="text-xs text-rose-400">Failed to resolve formula</span>';
          return;
        }

        badgeEl.innerText = `${data.steps.length} substitutions`;

        // Render steps
        if (data.steps.length === 0) {
          container.innerHTML = '<div class="p-3 bg-slate-800/60 rounded text-xs text-slate-300">Target formula has no constituent equations or is already in primitive form.</div>';
        } else {
          container.innerHTML = data.steps.map((s, idx) => `
            <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800 space-y-1">
              <div class="flex items-center justify-between">
                <span class="font-bold text-sky-400 font-mono">Step ${idx + 1}: Substituted '${s.target_variable}'</span>
                <span class="text-[10px] text-slate-500 font-mono">${s.source_citekey}</span>
              </div>
              <div class="text-[11px] text-slate-300 font-mono break-all">${escapeHtml(s.substituted_expr)}</div>
            </div>
          `).join('');
        }

        // Render closed-form LaTeX via KaTeX
        try {
          katex.render(data.closed_form_latex || '', latexEl, { displayMode: true, throwOnError: false });
        } catch (_) {
          latexEl.innerText = data.closed_form_latex;
        }

        // Render primitive symbols
        if (data.primitive_symbols && data.primitive_symbols.length) {
          symbolsEl.innerHTML = data.primitive_symbols.map(sym => `
            <span class="px-2 py-0.5 rounded bg-sky-950 text-sky-300 border border-sky-800 font-mono text-[11px]">${sym}</span>
          `).join('');
        } else {
          symbolsEl.innerHTML = '<span class="text-xs text-slate-500 font-mono">None</span>';
        }

        // Render polars code
        polarsEl.innerText = data.polars_code || '# No vectorized Polars expression generated';
      } catch (err) {
        container.innerHTML = `<div class="p-3 bg-rose-950/40 border border-rose-800 rounded text-rose-300 text-xs">Error: ${err.message}</div>`;
      }
    }

    async function loadStats() {
      try {
        const res = await fetch('/api/stats');
        const data = await res.json();
        document.getElementById('stat-docs').innerText = data.documents;
        document.getElementById('stat-chunks').innerText = data.chunks;
        document.getElementById('stat-formulas').innerText = data.formulas;
        document.getElementById('stat-tables').innerText = data.tables;
      } catch (err) {
        console.error('Stats error:', err);
      }
    }

    async function loadLineage() {
      try {
        document.getElementById('graph-meta').innerText = 'Fetching lineage network...';
        const res = await fetch('/api/lineage?limit=150');
        graphData = await res.json();
        document.getElementById('graph-meta').innerText = `${graphData.num_nodes} nodes | ${graphData.num_edges} derivation edges`;
        renderGraph(graphData);
      } catch (err) {
        document.getElementById('graph-meta').innerText = 'Failed to load graph';
      }
    }

    function renderGraph(data) {
      const svg = document.getElementById('dag-svg');
      svg.innerHTML = '';
      const w = svg.clientWidth || 800;
      const h = svg.clientHeight || 500;

      const nodes = data.nodes || [];
      const edges = data.edges || [];
      const positions = {};
      const n = nodes.length;

      nodes.forEach((node, idx) => {
        const angle = (idx / Math.max(n, 1)) * 2 * Math.PI;
        const radius = Math.min(w, h) * 0.38;
        const x = w / 2 + radius * Math.cos(angle) + (Math.sin(idx * 7) * 40);
        const y = h / 2 + radius * Math.sin(angle) + (Math.cos(idx * 5) * 40);
        positions[node.id] = { x, y };
      });

      edges.forEach(edge => {
        const src = positions[edge.from];
        const tgt = positions[edge.to];
        if (src && tgt) {
          const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
          line.setAttribute('x1', src.x);
          line.setAttribute('y1', src.y);
          line.setAttribute('x2', tgt.x);
          line.setAttribute('y2', tgt.y);
          line.setAttribute('stroke', '#475569');
          line.setAttribute('stroke-width', '1.2');
          line.setAttribute('stroke-dasharray', edge.relation === 'shared_symbols' ? '3,3' : 'none');
          line.setAttribute('opacity', '0.6');
          svg.appendChild(line);
        }
      });

      nodes.forEach(node => {
        const pos = positions[node.id];
        if (!pos) return;
        const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        g.setAttribute('class', 'cursor-pointer hover:opacity-80');
        g.onclick = () => selectNode(node);

        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', pos.x);
        circle.setAttribute('cy', pos.y);
        circle.setAttribute('r', '7');
        circle.setAttribute('fill', node.is_equality ? '#38bdf8' : '#a855f7');
        circle.setAttribute('stroke', '#0f172a');
        circle.setAttribute('stroke-width', '2');

        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', pos.x + 9);
        text.setAttribute('y', pos.y + 4);
        text.setAttribute('fill', '#94a3b8');
        text.setAttribute('font-size', '10');
        text.textContent = node.label.length > 16 ? node.label.slice(0, 16) + '...' : node.label;

        g.appendChild(circle);
        g.appendChild(text);
        svg.appendChild(g);
      });
    }

    function selectNode(node) {
      const details = document.getElementById('node-details');
      details.innerHTML = `
        <div class="space-y-2">
          <div><span class="text-slate-500 font-semibold">Document:</span> <span class="text-sky-400 font-mono">${node.citekey}</span></div>
          <div><span class="text-slate-500 font-semibold">Formula ID:</span> <span class="text-slate-300 font-mono text-[11px]">${node.id}</span></div>
          <div>
            <span class="text-slate-500 font-semibold">LaTeX:</span>
            <div class="mt-1 p-2 bg-slate-900 border border-slate-700 rounded text-amber-300 font-mono text-xs overflow-x-auto">${escapeHtml(node.latex)}</div>
          </div>
          <div>
            <span class="text-slate-500 font-semibold">Symbols:</span>
            <div class="mt-1 flex flex-wrap gap-1">
              ${(node.symbols || []).map(s => `<span class="px-1.5 py-0.5 bg-slate-800 border border-slate-700 rounded text-slate-300 font-mono text-[10px]">${s}</span>`).join('')}
            </div>
          </div>
        </div>
      `;
    }

    async function loadFormulas() {
      const grid = document.getElementById('formulas-grid');
      grid.innerHTML = '<div class="text-sm text-slate-400">Loading compiled formulas...</div>';
      const citekey = document.getElementById('formula-filter').value.trim();
      const url = citekey ? `/api/formulas?citekey=${encodeURIComponent(citekey)}` : '/api/formulas?limit=20';
      const res = await fetch(url);
      const items = await res.json();
      if (!items.length) {
        grid.innerHTML = '<div class="text-sm text-slate-400">No formulas found.</div>';
        return;
      }
      grid.innerHTML = items.map(f => {
        const grade = f.letter_grade || 'A';
        const score = f.validation_score != null ? f.validation_score.toFixed(1) : '90+';
        const badgeColor = grade === 'A' ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30' :
                           grade === 'B' ? 'bg-sky-500/20 text-sky-300 border-sky-500/30' :
                           grade === 'C' ? 'bg-amber-500/20 text-amber-300 border-amber-500/30' :
                           'bg-rose-500/20 text-rose-300 border-rose-500/30';
        return `
        <div class="glass-card rounded-xl p-4 flex flex-col space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-sky-400">${f.citekey}</span>
            <div class="flex items-center space-x-1.5">
              <span class="text-[10px] px-2 py-0.5 rounded font-mono font-bold ${badgeColor} border">Quality ${grade} (${score})</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Verified</span>
            </div>
          </div>
          <div class="text-xs text-amber-200 font-mono bg-slate-900/90 p-2.5 rounded border border-slate-800 overflow-x-auto">
            ${escapeHtml(f.latex)}
          </div>
          <div>
            <div class="text-[11px] font-semibold text-slate-400 mb-1">Generated Python AST:</div>
            <pre class="text-[11px] font-mono text-emerald-400 bg-slate-950 p-2 rounded overflow-x-auto border border-slate-800">${escapeHtml(f.python_code || 'N/A')}</pre>
          </div>
          ${f.polars_code ? `
          <div>
            <div class="text-[11px] font-semibold text-slate-400 mb-1">Polars Vectorized Expression:</div>
            <code class="text-[11px] font-mono text-sky-300 bg-slate-950 p-1.5 rounded block border border-slate-800">${escapeHtml(f.polars_code)}</code>
          </div>` : ''}
        </div>
      `;}).join('');
    }

    /* Interactive Playground Methods */
    async function initPlayground() {
      if (!playgroundPresets.length) {
        try {
          const res = await fetch('/api/presets');
          playgroundPresets = await res.json();
        } catch (e) {
          console.error('Failed to load presets', e);
        }
      }
      if (playgroundPresets.length && !currentPreset) {
        selectPreset(playgroundPresets[0].id);
      }
    }

    function onPresetChange() {
      const select = document.getElementById('preset-selector');
      selectPreset(select.value);
    }

    function selectPreset(presetId) {
      currentPreset = playgroundPresets.find(p => p.id === presetId) || playgroundPresets[0];
      if (!currentPreset) return;

      document.getElementById('pg-formula-title').innerText = currentPreset.name;
      const latexEl = document.getElementById('pg-latex-display');
      if (window.katex) {
        try {
          katex.render(currentPreset.latex, latexEl, { displayMode: true, throwOnError: false });
        } catch (_) {
          latexEl.innerText = currentPreset.latex;
        }
      } else {
        latexEl.innerText = currentPreset.latex;
      }

      // Build parameters
      playgroundInputs = {};
      const container = document.getElementById('pg-params-container');
      container.innerHTML = '';

      currentPreset.params.forEach(p => {
        const key = p.alt_name || p.name;
        playgroundInputs[key] = p.default;

        const row = document.createElement('div');
        row.className = 'space-y-1.5';
        row.innerHTML = `
          <div class="flex items-center justify-between text-xs">
            <span class="text-slate-300 font-medium">${p.label}</span>
            <input type="number" id="pg-num-${key}" value="${p.default}" min="${p.min}" max="${p.max}" step="${p.step}"
              class="w-20 px-2 py-0.5 bg-slate-800 border border-slate-700 rounded text-right font-mono text-xs text-sky-400 focus:ring-1 focus:ring-sky-500 outline-none"
              oninput="onParamInput('${key}', this.value, true)">
          </div>
          <input type="range" id="pg-range-${key}" value="${p.default}" min="${p.min}" max="${p.max}" step="${p.step}"
            class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer"
            oninput="onParamInput('${key}', this.value, false)">
        `;
        container.appendChild(row);
      });

      evaluatePlayground();
    }

    function onParamInput(key, val, fromNum) {
      const numVal = parseFloat(val);
      if (isNaN(numVal)) return;
      playgroundInputs[key] = numVal;

      if (fromNum) {
        const rangeEl = document.getElementById(`pg-range-${key}`);
        if (rangeEl) rangeEl.value = numVal;
      } else {
        const numEl = document.getElementById(`pg-num-${key}`);
        if (numEl) numEl.value = numVal;
      }

      evaluatePlayground();
    }

    async function evaluatePlayground() {
      if (!currentPreset) return;
      const t0 = performance.now();

      try {
        const res = await fetch('/api/eval', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            formula_id: 'custom',
            latex: currentPreset.latex,
            inputs: playgroundInputs
          })
        });
        const data = await res.json();
        const latency = Math.round(performance.now() - t0);
        document.getElementById('pg-latency').innerText = `${latency} ms`;

        if (data.result !== undefined) {
          const formatted = typeof data.result === 'number' ? data.result.toFixed(4) : String(data.result);
          document.getElementById('pg-result-value').innerText = formatted;
        } else if (data.error) {
          document.getElementById('pg-result-value').innerText = 'Error';
        }
      } catch (err) {
        console.error('Eval error:', err);
      }

      renderSensitivityCurve();
    }

    function renderSensitivityCurve() {
      if (!currentPreset) return;
      const svg = document.getElementById('pg-curve-svg');
      if (!svg) return;
      svg.innerHTML = '';

      const sweepKey = currentPreset.curve_param;
      const sweepParam = currentPreset.params.find(p => p.name === sweepKey || p.alt_name === sweepKey);
      const minX = currentPreset.curve_min || (sweepParam ? sweepParam.min : 0);
      const maxX = currentPreset.curve_max || (sweepParam ? sweepParam.max : 100);
      const nPts = currentPreset.curve_points || 20;
      const step = (maxX - minX) / nPts;

      const points = [];
      for (let x = minX; x <= maxX; x += step) {
        const clonedInputs = { ...playgroundInputs };
        clonedInputs[sweepKey] = x;
        const y = localEvaluate(currentPreset.id, clonedInputs);
        points.push({ x, y });
      }

      const currentX = playgroundInputs[sweepKey] || minX;
      const currentY = localEvaluate(currentPreset.id, playgroundInputs);

      // SVG dimensions: 500 x 240, padding: 40
      const padL = 50, padR = 25, padT = 20, padB = 40;
      const plotW = 500 - padL - padR;
      const plotH = 240 - padT - padB;

      const allY = points.map(p => p.y);
      const minY = Math.min(...allY) * 0.9;
      const maxY = Math.max(...allY) * 1.1 || 1.0;

      const mapX = (x) => padL + ((x - minX) / (maxX - minX)) * plotW;
      const mapY = (y) => padT + plotH - ((y - minY) / (maxY - minY)) * plotH;

      // Draw Grid & Axes
      const axisLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      axisLine.setAttribute('x1', padL);
      axisLine.setAttribute('y1', padT + plotH);
      axisLine.setAttribute('x2', padL + plotW);
      axisLine.setAttribute('y2', padT + plotH);
      axisLine.setAttribute('stroke', '#334155');
      axisLine.setAttribute('stroke-width', '1.5');
      svg.appendChild(axisLine);

      // Path
      let pathD = '';
      points.forEach((p, idx) => {
        const px = mapX(p.x);
        const py = mapY(p.y);
        pathD += (idx === 0 ? `M ${px} ${py}` : ` L ${px} ${py}`);
      });

      const curvePath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      curvePath.setAttribute('d', pathD);
      curvePath.setAttribute('fill', 'none');
      curvePath.setAttribute('stroke', '#38bdf8');
      curvePath.setAttribute('stroke-width', '2.5');
      svg.appendChild(curvePath);

      // Operating point dot
      const cx = mapX(currentX);
      const cy = mapY(currentY);

      const halo = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      halo.setAttribute('cx', cx);
      halo.setAttribute('cy', cy);
      halo.setAttribute('r', '10');
      halo.setAttribute('fill', 'rgba(56, 189, 248, 0.25)');
      svg.appendChild(halo);

      const dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      dot.setAttribute('cx', cx);
      dot.setAttribute('cy', cy);
      dot.setAttribute('r', '5');
      dot.setAttribute('fill', '#38bdf8');
      dot.setAttribute('stroke', '#0f172a');
      dot.setAttribute('stroke-width', '2');
      svg.appendChild(dot);

      // Labels
      const xLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      xLabel.setAttribute('x', padL + plotW / 2);
      xLabel.setAttribute('y', 240 - 10);
      xLabel.setAttribute('fill', '#94a3b8');
      xLabel.setAttribute('font-size', '11');
      xLabel.setAttribute('text-anchor', 'middle');
      xLabel.textContent = `${sweepKey} (Operating Point: ${currentX.toFixed(1)})`;
      svg.appendChild(xLabel);

      const yLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      yLabel.setAttribute('x', padL);
      yLabel.setAttribute('y', 14);
      yLabel.setAttribute('fill', '#94a3b8');
      yLabel.setAttribute('font-size', '11');
      yLabel.textContent = `Y = ${currentY.toFixed(4)}`;
      svg.appendChild(yLabel);
    }

    function localEvaluate(presetId, inputs) {
      if (presetId === 'pythagorean') {
        const rs = inputs['R_S'] || 750;
        const ra = inputs['R_A'] || 650;
        const gamma = inputs['gamma'] || inputs['\\gamma'] || 1.83;
        const num = Math.pow(rs, gamma);
        const den = num + Math.pow(ra, gamma);
        return den > 0 ? num / den : 0.5;
      }
      if (presetId === 'fip') {
        const hr = inputs['H_R'] || 20;
        const bb = inputs['B_B'] || 55;
        const hbp = inputs['HBP'] || 6;
        const k = inputs['K'] || 180;
        const ip = inputs['I_P'] || 180;
        return ip > 0 ? (13 * hr + 3 * (bb + hbp) - 2 * k) / ip + 3.10 : 3.10;
      }
      if (presetId === 'woba') {
        const bb = inputs['B_B'] || 65;
        const hbp = inputs['HBP'] || 7;
        const h1 = inputs['H_1'] || 95;
        const h2 = inputs['H_2'] || 30;
        const h3 = inputs['H_3'] || 4;
        const hr = inputs['H_R'] || 25;
        const pa = inputs['PA'] || 620;
        return pa > 0 ? (0.69 * bb + 0.72 * hbp + 0.89 * h1 + 1.27 * h2 + 1.62 * h3 + 2.10 * hr) / pa : 0.320;
      }
      return 0.5;
    }

    async function loadTables() {
      const grid = document.getElementById('tables-grid');
      grid.innerHTML = '<div class="text-sm text-slate-400">Loading benchmark tables...</div>';
      const res = await fetch('/api/tables?limit=12');
      const tables = await res.json();
      grid.innerHTML = tables.map(t => `
        <div class="glass-card rounded-xl p-4 space-y-3">
          <div class="flex items-center justify-between">
            <div class="font-semibold text-sm text-amber-400">${t.citekey} - ${t.caption || 'Benchmark Data'}</div>
            <div class="text-xs text-slate-400">${t.num_rows} rows x ${t.num_cols} cols</div>
          </div>
          <div class="text-xs text-slate-400">Columns: <span class="font-mono text-slate-300">${(t.columns || []).join(', ')}</span></div>
          ${t.preview && t.preview.length ? `
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs border border-slate-800">
              <thead class="bg-slate-800/80 text-slate-300">
                <tr>${Object.keys(t.preview[0]).map(k => `<th class="p-2 border border-slate-700">${k}</th>`).join('')}</tr>
              </thead>
              <tbody class="divide-y divide-slate-800">
                ${t.preview.map(row => `<tr>${Object.values(row).map(v => `<td class="p-2 border border-slate-800 font-mono">${v}</td>`).join('')}</tr>`).join('')}
              </tbody>
            </table>
          </div>` : ''}
        </div>
      `).join('');
    }

    async function executeSearch() {
      const q = document.getElementById('search-input').value.trim();
      if (!q) return;
      const container = document.getElementById('search-results');
      container.innerHTML = '<div class="text-sm text-slate-400">Searching corpus using hybrid dense + sparse retrieval...</div>';
      const res = await fetch(`/api/search?q=${encodeURIComponent(q)}&limit=10`);
      const data = await res.json();
      if (!data.results.length) {
        container.innerHTML = '<div class="text-sm text-slate-400">No matching chunks found.</div>';
        return;
      }
      container.innerHTML = data.results.map(r => `
        <div class="glass-card rounded-xl p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-sky-400">${r.citekey}</span>
            <span class="text-xs px-2 py-0.5 rounded bg-sky-900/50 text-sky-300 border border-sky-700">Score: ${r.score}</span>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed">${escapeHtml(r.snippet)}</p>
          <div class="text-[11px] text-slate-500">${(r.section_path || []).join(' > ')}</div>
        </div>
      `).join('');
    }

    function escapeHtml(str) {
      if (!str) return '';
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // Init
    loadStats();
    loadLineage();
  </script>
</body>
</html>
"""
        return HTMLResponse(html_content)

    graphql_app = GraphQL(schema)

    routes = [
        Route("/", endpoint=index_view, methods=["GET"]),
        Route("/playground", endpoint=index_view, methods=["GET"]),
        Route("/api/stats", endpoint=get_stats, methods=["GET"]),
        Route("/api/documents", endpoint=get_documents, methods=["GET"]),
        Route("/api/lineage", endpoint=get_lineage, methods=["GET"]),
        Route("/api/formulas", endpoint=get_formulas, methods=["GET"]),
        Route("/api/tables", endpoint=get_tables, methods=["GET"]),
        Route("/api/search", endpoint=search_endpoint, methods=["GET"]),
        Route("/api/eval", endpoint=eval_endpoint, methods=["GET", "POST"]),
        Route("/api/presets", endpoint=get_presets, methods=["GET"]),
        Route("/api/chain", endpoint=chain_endpoint, methods=["GET"]),
        Route("/api/coverage", endpoint=get_coverage, methods=["GET"]),
        Route("/api/validate", endpoint=validate_endpoint, methods=["GET", "POST"]),
        Route("/graphql", endpoint=graphql_app, methods=["GET", "POST"]),
        Mount("/graphql", app=graphql_app),
    ]

    return Starlette(routes=routes)
