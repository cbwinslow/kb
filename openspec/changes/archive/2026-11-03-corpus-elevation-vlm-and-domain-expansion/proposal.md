# Proposal: Corpus Formula Elevation, Batch Figure VLM Grounding, and Multi-Domain Preset Harvesting

## Why

Following the delivery of the V2 platform (Sanitizer V3, heuristic auto-binding, VLM visual grounding, and Scholarly UI Explorer in ADR-036), three high-leverage opportunities remain to maximize the scientific knowledge base's value:
1. **Formula Quality Elevation**: 1,996 of 6,199 formulas in `kb_formulas` remain at Grade F due to legacy extraction artifacts, unclosed delimiter formatting, and piecewise cases that can now be recovered by Sanitizer V3 into verified Grade A/B ASTs.
2. **Corpus-Wide VLM Grounding**: 490 scientific diagrams and trajectory plots extracted into homelab vault storage have not yet had their VLM summaries, curve detections, and formula entity links pre-computed for real-time agent retrieval via FastMCP (`kb_get_figure`, `kb_search_figures`).
3. **Multi-Domain Taxonomy Expansion**: While `kb` is designed to be domain-agnostic, its curated harvest presets are currently concentrated in baseball sabermetrics. Expanding presets into adjacent quantitative domains (biomechanics, aerodynamics & PINNs, sports econometrics, kinematics) enables broader cross-disciplinary evidence-to-code pipelines.

## What Changes

- **Corpus Formula Elevation & Grade-F Recovery**:
  - Run enhanced Sanitizer V3 and stack-based delimiter repair across all 1,996 Grade F formulas using `kb corpus repair-all --batch-size 100`.
  - Add domain heuristics for common mathematical notation recovery (piecewise arrays, multi-line equation arrays `\begin{aligned}`, split fraction bars, subscript cleanup).
  - Automatically re-score recovered formulas through `FormulaQualityGate` (Tiers 1–4) and export verified Grade A additions into `packages/kb_formulas`.
- **Batch Figure VLM Grounding Indexer**:
  - Implement `kb figures index-all` CLI command and async batch processing service with `--batch-size`, `--limit`, `--force`, and `--dry-run` flags.
  - Automatically scan ungrounded `Figure` records in PostgreSQL, query `FigureVLMProcessor` to extract diagram classifications, axes, units, and curve descriptions, and link related formula IDs from proximal chunks.
  - Expose grounded figure counts and status in `kb corpus audit` and the Starlette UI (`/api/stats`).
- **Multi-Domain Preset Taxonomy & Harvesting**:
  - Extend `get_preset_queries()` in `src/kb/enrich/openalex.py` with multi-domain curated presets:
    - `biomechanics`: joint angles, inverse dynamics, ground reaction force, markerless motion capture.
    - `aerodynamics-pinn`: physics-informed neural networks, wake vortex aerodynamics, drag crisis, Magnus effect.
    - `sports-econometrics`: salary arbitration models, win-per-dollar efficiency, attendance regression.
    - `kinematics-tracking`: high-frame-rate computer vision, 3D ball trajectory filtering, Kalman/Extended Kalman tracking.
  - Extend `kb sync harvest --preset <name>` to accept and validate the new domain presets with multi-attribute deduplication.

## Capabilities

### Modified Capabilities
- `corpus-formula-repair`: Add Requirement 2 for targeted Grade-F AST recovery with Sanitizer V3 piecewise and delimiter repair heuristics.
- `figure-vlm-grounding`: Add Requirement 4 for corpus-wide batch VLM indexing and CLI orchestration (`kb figures index-all`).
- `openalex-enrichment`: Add Requirement 4 for multi-domain taxonomy presets and quantitative research harvest queries.

## Impact

- **Database**: Updates `kb_formulas` (elevating Grade F to A/B/C), updates `figures` (`vlm_summary`, `detected_curves`, `formula_ids`).
- **Standalone Package**: Recompiles `packages/kb_formulas` with newly recovered Grade A formulas.
- **CLI Commands**:
  - `kb corpus repair-all` (enhanced repair rate).
  - `kb figures index-all` (new command).
  - `kb sync harvest --preset [biomechanics|aerodynamics-pinn|sports-econometrics|kinematics-tracking]` (expanded choices).
- **FastMCP Agent Tools**: `kb_get_figure`, `kb_search_figures`, `kb_get_formula` immediately benefit from enriched figure metadata and expanded formula library.
- **Portability & Disk Guard**: Preserves homelab SFTP vaulting and minimum local workstation disk threshold ($\ge 1.5$ GB free).
