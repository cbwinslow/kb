# Proposal: Corpus Validation, Invariant Auditing & Scaled Sabermetric Expansion

## Why
The `kb` repository on `cbwdellr720` houses over 280 scientific documents, 33,000 chunks, 5,900 formulas, and 1,200 benchmark tables. However, over 1,600 equations lack formal Tier 1–4 quality validation, and dozens have degraded AST syntax or OCR glitches. To ensure data integrity across the knowledge graph, symbolic chaining engines, and vectorized code generation pipelines, `kb` requires an automated corpus audit, repair, and grading harness. Concurrently, high-yield scaled harvesting across 5 targeted sabermetric disciplines must be executed to expand the corpus with foundational research while enforcing multi-attribute deduplication and local disk preservation.

## What Changes
- **Automated Corpus Auditing & Invariant Verification**: Adds `kb corpus audit` command to detect orphaned chunks, unlinked formulas, missing figure vault paths, and unvalidated equations.
- **Corpus-Wide Batch Formula Repair & Grading**: Adds `kb corpus repair-all` command combining `CorpusFormulaRepairer` and `FormulaQualityGate` to automatically sanitize LaTeX ASTs, split acronyms, repair OCR token errors, compute Tier 1–4 scorecards, and assign letter grades (A–F) across all unvalidated equations.
- **Multi-Domain Scaled Harvester Execution**: Drives large-scale batch harvesting across `popular`, `mlb-modeling`, `statcast`, `retrosheet`, and `baseball-python` presets, leveraging smart deduplication to acquire and vault 50+ new high-impact research papers.
- **Automated Accuracy & Code Generation Sync**: Compiles Grade A verified equations into vectorized Polars expressions within `packages/kb_formulas` and verifies empirical benchmark accuracy against Parquet dataset tables.

## Capabilities

### Modified Capabilities
- `corpus-qa`: Extends corpus quality auditing to verify relational integrity, detect orphaned records, and validate remote figure vault paths on `cbwdellr720`.
- `corpus-formula-repair`: Adds batch-level repair and quality scoring for all database equations, updating validation status and Tier 1–4 diagnostic details.
- `harvester-daemon`: Expands daemon and CLI harvesting workflows to support coordinated multi-preset batch sweeps with automated vault transfer and local unlinking.

## Impact
- `src/kb/qa/corpus_auditor.py`: New module providing comprehensive relational integrity and quality auditing for PostgreSQL documents, chunks, formulas, and figures.
- `src/kb/cli.py`: Exposes `kb corpus audit` and `kb corpus repair-all` CLI commands.
- `src/kb/math/repair.py` & `src/kb/qa/quality_gate.py`: Connected for batch corpus repair pass.
- `packages/kb_formulas`: Standalone vectorized wheel updated with newly verified equations.
- 100% backward compatible with existing database schemas and REST/GraphQL APIs.
