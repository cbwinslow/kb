# Proposal: Citation Lineage, Live Formula Playground, Multi-Domain Harvesting, and Empirical Benchmarking

## Why

While the `kb` engine has amassed 311 scientific papers, 4,120 verified mathematical formulas (1,743 compiled standalone functions), 490 grounded figures, and 1,395 benchmark tables, several high-impact capabilities remain disconnected:
1. **Citation Network Sparse & Slow**: Out of 311 papers, 245 have DOIs, but only 54 have OpenAlex IDs and only 2 have `referenced_works` populated, leaving `kb_citations` with just 17 edges. Furthermore, `CitationGraphBuilder` suffers from an ORM selectin-loading bottleneck that pulls 37,006 chunks into memory during graph traversal.
2. **Formula Playground Disconnected from Compiled Library**: Although 1,743 verified formula functions are compiled in `packages/kb_formulas`, the Web UI Playground only provides static or mock examples rather than letting users search, configure parameters, and execute live calculations against the full library.
3. **Multi-Domain Harvester Presets Unharvested**: Presets for `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, and `kinematics-tracking` were defined and tested with dry-run deduplication in ADR-037, but full papers have not yet been harvested and ingested into the vault.
4. **Empirical Accuracy Untracked Across Corpus**: While `EmpiricalAccuracyRunner` supports evaluating formulas against Parquet fixtures, a global empirical accuracy evaluation across all 1,743 formulas and 1,395 fixtures has not been run, leaving empirical fidelity unverified on scorecards.

Addressing these 4 pillars transforms `kb` into a unified, rich research engine with dense citation webs, full in-browser formula execution, multi-disciplinary literature, and verified empirical accuracy leaderboards.

## What Changes

1. **Optimized Citation Graph & Bibliometric Enrichment**:
   - Optimize `CitationGraphBuilder` and `Document` queries to use column projections (`Document.id, Document.openalex_id, Document.referenced_works, Document.year`) to bypass `lazy="selectin"` eager chunk loads, reducing graph build latency from 30s+ to under 1s.
   - Run batch OpenAlex bibliometric enrichment (`kb enrich openalex --all`) across all 245 DOI papers, populating `openalex_id`, `citation_count`, `topics`, and `referenced_works`.
   - Backfill paper-to-paper citation links in `kb_citations` via `kb sync citations`, establishing hundreds of internal and external citation edges.
   - Update Web UI Lineage graph to surface real citation links, co-citation clusters, and foundational literature hubs.

2. **Live Compiled Formula Playground in Web UI**:
   - Expose REST endpoint `GET /api/formulas/compiled` returning metadata, signatures, docstrings, and parameter types for the 1,743 compiled formulas in `packages/kb_formulas`.
   - Implement `POST /api/formulas/compiled/{func_name}/eval` executing validated formula functions with user-supplied arguments.
   - Enhance the Web UI `[🧮 Playground]` tab with formula search/filter dropdown, reactive parameter sliders/inputs, real-time result calculation, sensitivity curve visualization, and 1-click code export (Python, Polars, SymPy, curl).

3. **Multi-Domain Literature Harvester Execution**:
   - Execute targeted harvesting sweeps across multi-domain presets (`biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, `kinematics-tracking`).
   - Ingest harvested PDFs through GPU-accelerated Docling layout analysis and OCR, extracting formulas, tables, and figures.
   - Ground newly extracted figures via `FigureBatchIndexer` and persist artifacts to the homelab SFTP vault.

4. **Corpus Empirical Accuracy Benchmarking Leaderboard**:
   - Execute automated empirical evaluation (`kb benchmark accuracy --all`) across Grade A formulas matching tabular Parquet fixtures.
   - Compute MAE, RMSE, max relative error, and $R^2$ metrics.
   - Generate a markdown and JSON empirical accuracy leaderboard artifact.
   - Surface empirical accuracy badges in the Web UI Formulas and Figures tables.

## Capabilities

### Modified Capabilities
- `openalex-citation-graph`: Add column projection optimizations to avoid ORM eager loading, and batch OpenAlex reference enrichment to codify dense citation linkages across all DOI-bearing documents.
- `ui-playground`: Connect the playground to the real 1,743 compiled formula functions in `packages/kb_formulas`, supporting dynamic signature inspection, reactive input generation, live execution, and code snippet export.
- `harvester-daemon`: Execute multi-domain harvesting sweeps across `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, and `kinematics-tracking` with layout analysis and vault synchronization.
- `empirical-accuracy-benchmarking`: Run global empirical accuracy benchmarking across Grade A formulas and Parquet fixtures, generating leaderboard reports and surfacing empirical accuracy metrics in the UI.

## Impact

- **Database**: Populates `referenced_works`, `topics`, and `openalex_id` on `kb_documents`, expands `kb_citations` from 17 to hundreds of edges, and adds new multi-domain documents, formulas, and figures.
- **Backend APIs (`src/kb/ui/app.py`)**: Adds `/api/formulas/compiled` and `/api/formulas/compiled/{func_name}/eval`, and enriches `/api/lineage` with dense citation edges.
- **Performance**: Eliminates 37,000-chunk ORM selectin loading during citation graph traversals.
- **CLI Commands**: Enhances `kb enrich openalex`, `kb sync citations`, `kb sync harvest`, and `kb benchmark accuracy`.
- **Quality Gates**: All changes will strictly adhere to `ruff check`, `pyright` strict typing, and `pytest` regression suites.
