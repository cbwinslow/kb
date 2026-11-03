# Design: Corpus Formula Elevation, Batch Figure VLM Grounding, and Multi-Domain Preset Harvesting

## Context

Following ADR-036, the platform contains a robust LaTeX Sanitizer V3, heuristic auto-binding for empirical accuracy, FastMCP multimodal tools (`kb_get_figure`, `kb_search_figures`), and an interactive Scholarly UI Explorer. However:
- 1,996 of 6,199 formulas in PostgreSQL remain at Grade F due to legacy parser failures.
- 490 figures in the homelab vault lack pre-computed VLM summaries and formula linkages.
- Harvester presets in `src/kb/enrich/openalex.py` are limited to baseball sabermetrics.

## Goals / Non-Goals

**Goals:**
- Implement targeted recovery heuristics in `CorpusFormulaRepairer` and `EquationSanitizer` to convert recoverable Grade-F formulas into valid SymPy ASTs and evaluate Tier 1–4 quality scores.
- Create an async batch figure indexing engine (`FigureBatchIndexer`) and CLI command (`kb figures index-all`) to ground ungrounded figures against proximal chunks and formula entities.
- Add curated multi-domain research presets (`biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, `kinematics-tracking`) to `OpenAlexClient.get_preset_queries()` and `kb sync harvest`.
- Re-export verified Grade A equations to `packages/kb_formulas`.

**Non-Goals:**
- Replacing existing OCR / Docling document parsing pipelines.
- Modifying underlying PostgreSQL schema tables (existing `figures.vlm_summary`, `figures.detected_curves`, and `figures.formula_ids` columns are already present).
- Overhauling FastMCP server tools (tools are already declared; this populates the underlying data).

## Decisions

### 1. Progressive Batch In-Place Formula Repair (`src/kb/math/repair.py`)
- **Decision**: Extend `CorpusFormulaRepairer.repair_and_grade_corpus()` with targeting for Grade F formulas, applying:
  - Sanitizer V3 acronym protection (`BABIP`, `wOBA`, `ERA`, `FIP`, `wRAA`).
  - Stack-based delimiter rebalancing for missing braces, parentheses, and brackets.
  - Multi-line equation array unwrapping (`\begin{align*}`, `\begin{array}`).
  - Bounded transaction batches (default 100) with rollback on individual equation parse failures to prevent aborted transactions.
- **Alternatives Considered**: Full corpus re-extraction from raw PDFs. Rejected because re-extracting 311 PDFs would take hours of GPU OCR time, whereas sanitizer AST re-parsing operates directly on database LaTeX strings in seconds.

### 2. Batch Figure VLM Indexer (`src/kb/enrich/vlm.py`, `src/kb/cli.py`)
- **Decision**: Implement `FigureBatchIndexer` in `src/kb/enrich/vlm.py`:
  - Queries `figures` table for rows where `vlm_summary IS NULL` (or all rows if `--force`).
  - Calls `FigureVLMProcessor.analyze_figure()` with caption and surrounding text context.
  - Resolves proximal formula IDs by scanning parent document chunks within the same section.
  - Exposes `kb figures index-all [--batch-size 50] [--limit N] [--force] [--dry-run]` in CLI.
- **Alternatives Considered**: On-demand lazy VLM grounding during FastMCP calls. Rejected because VLM inference adds 500ms–2s latency to real-time agent queries; pre-indexing guarantees sub-50ms tool response times.

### 3. Multi-Domain Harvester Taxonomy (`src/kb/enrich/openalex.py`)
- **Decision**: Expand `get_preset_queries()` with structured dictionary definitions containing search keywords, concept filters, and sort orders:
  - `biomechanics`: `"biomechanics" OR "joint kinetics" OR "ground reaction force" OR "motion capture"`
  - `aerodynamics-pinn`: `"physics-informed neural network" OR "aerodynamics" OR "Magnus effect" OR "wake flow"`
  - `sports-econometrics`: `"sports economics" OR "salary arbitration" OR "win-maximizing"`
  - `kinematics-tracking`: `"trajectory tracking" OR "Kalman filter" OR "optical tracking"`
- **Alternatives Considered**: Free-form user text queries only. Presets provide standardized, high-yield, reproducible query configurations for continuous harvesters.

## Risks / Trade-offs

- **[Risk] Heavy database lock contention during batch updates** → **Mitigation**: Batches are processed in small chunks (50-100 items) with explicit transaction boundaries and session release.
- **[Risk] VLM timeout or high latency on complex charts** → **Mitigation**: Batch processor supports `--limit` and graceful fallbacks preserving caption-only grounding when visual inference fails.
- **[Risk] Over-sanitizing valid LaTeX into invalid SymPy** → **Mitigation**: All transformations are validated by `FormulaExtractor.extract_ast()`; if SymPy parsing fails, the original raw LaTeX is preserved and the formula remains unchanged.
