# Design: Corpus Validation, Invariant Auditing & Scaled Sabermetric Expansion

## Context
The `kb` knowledge base on `cbwdellr720` has expanded rapidly to over 280 documents and nearly 6,000 formulas. However:
1. Over 1,600 equations remain in `validation_status IS NULL` without formal Tier 1–4 quality scores.
2. An automated audit mechanism is needed to guarantee 0 orphaned records (chunks without documents, formulas without chunks/documents, missing figures on the homelab vault).
3. The newly implemented multi-attribute deduplication engine enables large-scale harvesting sweeps across all 5 sabermetric presets (`popular`, `mlb-modeling`, `statcast`, `retrosheet`, and `baseball-python`) without duplicate downloads.

See `proposal.md` for background and user goals.

## Goals / Non-Goals

**Goals:**
- Implement `CorpusAuditor` in `src/kb/qa/corpus_auditor.py` to audit document, chunk, formula, figure, and table counts and invariant consistency.
- Implement `repair_and_grade_corpus()` to batch-process all unvalidated formulas using `CorpusFormulaRepairer` and `FormulaQualityGate`, assigning Tier 1–4 diagnostics and letter grades.
- Execute a scaled multi-preset harvest sweep across targeted sabermetric disciplines.
- Vault newly acquired papers and figures to `cbwdellr720` via `SSHStorageSync` and maintain $\ge 1.5$ GB workstation disk space.
- Re-compile verified Grade A formulas into `packages/kb_formulas` with vectorized Polars expressions and run accuracy benchmarks.

**Non-Goals:**
- No edits to external `baseballpy`.
- No dropping or mutating core database schemas.

## Decisions

### 1. Dedicated Corpus Auditor Engine (`src/kb/qa/corpus_auditor.py`)
Provides an asynchronous `CorpusAuditor` that queries PostgreSQL to calculate:
- Total counts across `kb_documents`, `kb_chunks`, `kb_formulas`, `kb_figures`, and `kb_benchmark_tables`.
- Relational integrity: checks for orphaned chunks (`WHERE document_id NOT IN (SELECT id FROM kb_documents)`), orphaned formulas, and unlinked figures.
- Quality status distribution: tallies formulas by `validation_status` ('verified', 'provisional', 'degraded', 'failed', 'unvalidated').
- Remote vault file presence: samples figure remote paths on `cbwdellr720` to verify remote persistence.

### 2. Batch Quality Gate Scorer (`src/kb/math/repair.py`)
Enhances `CorpusFormulaRepairer` with `repair_and_grade_corpus(batch_size=100)`:
- Queries formulas where `validation_status IS NULL` or `is_valid = false`.
- Cleans and re-parses LaTeX with `EquationSanitizer` and `FormulaExtractor`.
- Evaluates Tier 1–4 quality rules using `FormulaQualityGate.validate_formula()`.
- Updates `sanitized_latex`, `sympy_repr`, `symbols`, `is_valid`, `is_equality`, `validation_status`, `validation_score`, and `validation_details` in progressive transaction batches.

### 3. Scaled Multi-Preset Harvester Sweeps
Utilizes `kb sync harvest` across `popular`, `mlb-modeling`, `statcast`, `retrosheet`, and `baseball-python` presets:
- Leverages `DuplicateResolver` to filter candidate works before downloading.
- Harvests candidate open-access research papers, parses layout with Docling on CUDA RTX 3060, generates BGE-M3 embeddings, and vaults to homelab PostgreSQL 16.

## Risks / Trade-offs

- **[Risk: Large batch database update transaction locks]**
  → *Mitigation*: Process formulas in chunks of 50–100, committing each batch independently to keep transactions short and avoid table locks.
- **[Risk: GPU memory exhaustion during multi-paper layout conversion]**
  → *Mitigation*: Process papers sequentially, releasing PyTorch CUDA memory cache (`torch.cuda.empty_cache()`) between papers.
- **[Risk: Workstation disk space exhaustion]**
  → *Mitigation*: Unlink temporary local PDFs and image crops immediately after vaulting, ensuring free disk space remains $\ge 1.5$ GB.
