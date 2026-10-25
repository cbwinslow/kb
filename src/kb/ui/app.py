"""Interactive Web Application and REST API for the Scientific Knowledge Base."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import polars as pl
from sqlalchemy import func, select
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route

from kb.codegen.compiler import FormulaCompiler
from kb.math.lineage import DerivationNode, FormulaLineageGraph
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import LocalEmbeddingGenerator
from kb.storage.models import BenchmarkTable, Chunk, Document, Formula
from kb.storage.search import HybridSearchEngine


def create_app(db_manager: DatabaseManager | None = None) -> Starlette:
    """Creates the Starlette application for kb visual dashboard."""
    manager = db_manager or DatabaseManager()
    compiler = FormulaCompiler()

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

            return JSONResponse({
                "documents": doc_cnt,
                "chunks": chk_cnt,
                "formulas": frm_cnt,
                "tables": tbl_cnt,
                "embedded_chunks": emb_cnt,
            })

    async def get_documents(_request: Request) -> JSONResponse:
        """Return list of ingested documents."""
        async with manager.session_factory() as session:
            stmt = select(Document).order_by(Document.year.desc().nullslast()).limit(100)
            res = await session.execute(stmt)
            docs = res.scalars().all()
            return JSONResponse([
                {
                    "citekey": d.citekey,
                    "title": d.title,
                    "authors": d.authors,
                    "year": d.year,
                    "doi": d.doi,
                    "arxiv_id": d.arxiv_id,
                    "num_formulas": len(d.formulas),
                    "num_tables": len(d.benchmark_tables),
                }
                for d in docs
            ])

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
                    "label": f"{n.citekey}:{n.formula_id[:8]}",
                    "citekey": n.citekey,
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
                    "relation": str(e.relation),
                    "confidence": e.confidence,
                    "reason": e.reason,
                    "shared_symbols": e.shared_symbols,
                }
                for e in graph.edges
            ]

            return JSONResponse({
                "num_nodes": len(nodes_data),
                "num_edges": len(edges_data),
                "nodes": nodes_data,
                "edges": edges_data,
            })

    async def get_formulas(request: Request) -> JSONResponse:
        """Return formulas with compiled code."""
        citekey = request.query_params.get("citekey")
        limit = int(request.query_params.get("limit", 25))

        async with manager.session_factory() as session:
            stmt = select(Formula).where(Formula.is_valid == True)  # noqa: E712
            if citekey:
                stmt = stmt.where(Formula.citekey == citekey)
            stmt = stmt.limit(limit)
            formulas = list((await session.execute(stmt)).scalars().all())

            results: list[dict[str, Any]] = []
            for f in formulas:
                compiled = compiler.compile(
                    formula_id=f.id,
                    citekey=f.citekey,
                    raw_latex=f.raw_latex,
                    sympy_repr=f.sympy_repr,
                )
                results.append({
                    "formula_id": f.id,
                    "citekey": f.citekey,
                    "latex": f.raw_latex,
                    "symbols": f.symbols,
                    "python_code": compiled.python_source,
                    "polars_code": compiled.polars_expression,
                    "parameters": compiled.parameters,
                    "is_valid": compiled.is_valid,
                })
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
                results.append({
                    "table_id": t.id,
                    "citekey": t.citekey,
                    "caption": t.caption,
                    "num_rows": t.num_rows,
                    "num_cols": t.num_cols,
                    "columns": t.column_names,
                    "parquet_path": t.parquet_path,
                    "preview": preview_rows,
                })
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
            results = await searcher.search(session, query_text=query, embedder=embedder, limit=limit)
            return JSONResponse({
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
            })

    async def index_view(_request: Request) -> HTMLResponse:
        """Serve the interactive single-page dashboard."""
        html_content = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KB Scientific Knowledge Base Explorer</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
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
    <div id="stats-container" class="flex items-center space-x-4 text-xs">
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-docs" class="font-semibold text-sky-400">...</span> docs</div>
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-chunks" class="font-semibold text-emerald-400">...</span> chunks</div>
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-formulas" class="font-semibold text-indigo-400">...</span> formulas</div>
      <div class="px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700"><span id="stat-tables" class="font-semibold text-amber-400">...</span> tables</div>
    </div>
  </header>

  <!-- Navigation Tabs -->
  <div class="bg-slate-900 border-b border-slate-800 px-6 py-2 flex space-x-4">
    <button onclick="switchTab('lineage')" id="tab-btn-lineage" class="px-4 py-1.5 text-sm font-medium rounded-lg bg-sky-500 text-white">Lineage Graph (DAG)</button>
    <button onclick="switchTab('formulas')" id="tab-btn-formulas" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Knowledge-to-Code</button>
    <button onclick="switchTab('tables')" id="tab-btn-tables" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Benchmark Tables</button>
    <button onclick="switchTab('search')" id="tab-btn-search" class="px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white">Hybrid Retrieval</button>
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

    <!-- View 3: Benchmark Tables -->
    <section id="view-tables" class="flex-1 hidden flex flex-col space-y-4 overflow-y-auto custom-scroll">
      <div>
        <h2 class="text-base font-semibold text-slate-200">Benchmark Tables & Parquet Fixtures</h2>
        <p class="text-xs text-slate-400">524 golden tables extracted from literature, backed by typed Parquet files.</p>
      </div>
      <div id="tables-grid" class="space-y-4">
        <div class="text-sm text-slate-400">Loading tables...</div>
      </div>
    </section>

    <!-- View 4: Hybrid Search -->
    <section id="view-search" class="flex-1 hidden flex flex-col space-y-4">
      <div class="flex space-x-3">
        <input id="search-input" type="text" placeholder="Ask or search research corpus (e.g. 'Pythagorean expectation derivation')..." class="flex-1 px-4 py-2.5 bg-slate-800 border border-slate-700 rounded-xl text-slate-200 text-sm focus:ring-2 focus:ring-sky-500 outline-none" onkeydown="if(event.key==='Enter') executeSearch()">
        <button onclick="executeSearch()" class="px-5 py-2.5 bg-sky-600 hover:bg-sky-500 text-white rounded-xl text-sm font-medium">Search</button>
      </div>
      <div id="search-results" class="flex-1 overflow-y-auto custom-scroll space-y-3">
        <p class="text-xs text-slate-400">Enter a query above to execute hybrid dense + sparse retrieval across the corpus.</p>
      </div>
    </section>
  </main>

  <script>
    // State
    let currentTab = 'lineage';
    let graphData = { nodes: [], edges: [] };

    function switchTab(tabId) {
      ['lineage', 'formulas', 'tables', 'search'].forEach(t => {
        document.getElementById(`view-${t}`).classList.add('hidden');
        document.getElementById(`tab-btn-${t}`).className = 'px-4 py-1.5 text-sm font-medium rounded-lg text-slate-400 hover:text-white';
      });
      document.getElementById(`view-${tabId}`).classList.remove('hidden');
      document.getElementById(`tab-btn-${tabId}`).className = 'px-4 py-1.5 text-sm font-medium rounded-lg bg-sky-500 text-white';
      currentTab = tabId;

      if (tabId === 'formulas') loadFormulas();
      if (tabId === 'tables') loadTables();
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

      // Position nodes in radial or grid layout
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

      // Render edges
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

      // Render node circles
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
      grid.innerHTML = items.map(f => `
        <div class="glass-card rounded-xl p-4 flex flex-col space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono font-bold text-sky-400">${f.citekey}</span>
            <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Verified</span>
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
      `).join('');
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

    routes = [
        Route("/", endpoint=index_view, methods=["GET"]),
        Route("/api/stats", endpoint=get_stats, methods=["GET"]),
        Route("/api/documents", endpoint=get_documents, methods=["GET"]),
        Route("/api/lineage", endpoint=get_lineage, methods=["GET"]),
        Route("/api/formulas", endpoint=get_formulas, methods=["GET"]),
        Route("/api/tables", endpoint=get_tables, methods=["GET"]),
        Route("/api/search", endpoint=search_endpoint, methods=["GET"]),
    ]

    return Starlette(routes=routes)
