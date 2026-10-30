# Proposal: V2 Corpus Intelligence & Multimodal Platform

## Why
While `kb` successfully operates as an evidence-to-code research engine with 311 documents, 37,006 chunks, and 6,199 formulas, four significant functional bottlenecks constrain its full intelligence loop:
1. **Manual Terminal Ingestion**: Ingesting newly discovered arXiv and OpenAlex preprints requires switching between CLI flags, manual DOI lookups, and terminal commands rather than an intuitive 1-click web interface.
2. **1,996 Unrecovered Formulas (Grade F)**: Over 32% of extracted formulas remain Grade F due to OCR delimiter mismatches, multi-character variable decomposition (e.g. $B \cdot A \cdot B \cdot I \cdot P$), and piecewise LaTeX cases that exceed Sanitizer v2 capabilities.
3. **Disconnected Empirical Benchmarks**: While `kb benchmark accuracy` supports vectorized Polars evaluation, extracted formulas lack automated schema auto-binding against real-world Statcast/Retrosheet Parquet tracking datasets, resulting in zero automated empirical validations.
4. **Ungrounded Visual Figures**: Over 490 scientific diagrams and trajectory plots extracted into homelab vault storage remain unlinked to mathematical formulas and lack VLM-based semantic comprehension for LLM agents.

## What Changes
- **Interactive UI Scholarly Explorer & 1-Click Ingest**:
  - Add a dedicated "Scholarly Explorer" tab in `kb ui serve`.
  - Provide live multi-source arXiv and OpenAlex search directly in the browser with interactive metadata cards.
  - Implement a 1-click asynchronous ingestion endpoint (`POST /api/harvest/ingest-url`) triggering the Docling GPU worker, LaTeX extraction, and vault archival in the background.
- **Advanced Formula Sanitizer v3 & AST Recovery**:
  - Implement `LaTeXSanitizerV3` with multi-character acronym preservation (`BABIP`, `wOBA`, `wRAA`), unclosed delimiter rebalancer, and `\begin{cases}` piecewise AST conversion.
  - Upgrade `CorpusFormulaRepairer` to batch-recover and elevate Grade F equations to Grade A/B in PostgreSQL with atomic rollback protection.
- **Empirical Accuracy Auto-Binding Engine & Ground-Truth Ingestion**:
  - Implement fuzzy heuristic column binding between formula mathematical symbols and Parquet/CSV dataset columns.
  - Provide curated Statcast / Retrosheet ground-truth tracking fixtures in `data/fixtures/` with automated baseline schema registration.
  - Update `kb benchmark accuracy` to auto-discover and evaluate all candidate Grade A formulas against matching golden tables.
- **Multimodal Figure & Diagram VLM Grounding & MCP Tooling**:
  - Implement `FigureVLMProcessor` to extract axes, visual curve descriptions, and trajectory insights from extracted figures.
  - Link figures directly to formulas, variables, and derivation chains in the relational schema and GraphQL knowledge graph.
  - Expose `kb_get_figure` and `kb_search_figures` in FastMCP for AI coding agents.

## Capabilities

### New Capabilities
- `scholarly-ui-explorer`: Interactive web search interface within the Starlette dashboard and background 1-click preprint ingestion.
- `formula-sanitizer-v3`: Acronym preservation, delimiter repair, piecewise case conversion, and batch AST recovery for Grade F equations.
- `figure-vlm-grounding`: Multimodal visual grounding, curve analysis, figure-to-formula relational linkages, and FastMCP figure tools.

### Modified Capabilities
- `empirical-accuracy-benchmarking`: Add heuristic column auto-binding, Statcast/Retrosheet golden fixture registration, and batch empirical evaluation without manual schema specification.

## Impact
- **APIs**: New REST endpoints (`/api/search/external`, `/api/harvest/ingest-url`, `/api/figures/{id}/analysis`), new GraphQL figure fields, and 2 new FastMCP tools.
- **Database**: Add `vlm_summary`, `detected_curves`, and `formula_ids` array to `kb_figures`.
- **Dependencies**: Adds lightweight image analysis utilities; utilizes existing `docling`, `polars`, `strawberry-graphql`, and `fastmcp`.
- **Portability**: Preserves all workstation disk floor protections ($\ge 1.5$ GB) and homelab SFTP vault invariants.
