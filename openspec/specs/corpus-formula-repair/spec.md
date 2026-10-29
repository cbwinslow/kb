# Specification: In-Place Corpus Formula Repair

## Scope & Purpose
Enables progressive, transaction-safe in-place repair and re-parsing of previously ingested formulas in PostgreSQL to recover valid symbolic ASTs following sanitizer upgrades.

## Requirements
1. **Batch Repair Process**:
   - `CorpusFormulaRepairer.repair_corpus(batch_size, dry_run)` in `kb.math.repair`:
     - Reads formulas from database (targeting invalid or all formulas).
     - Applies updated `EquationSanitizer.sanitize(raw_latex)`.
     - Re-parses sanitized LaTeX with `FormulaExtractor`.
     - In non-dry-run mode, updates `sanitized_latex`, `sympy_repr`, `symbols`, `is_valid`, `is_equality`, `lhs`, and `rhs` columns in-place.
     - Commits transactions progressively per batch to protect database memory and connection state.
2. **Progress & Outcome Accounting**:
   - MUST return a `RepairResult` reporting total processed, previously valid, newly recovered, and persistently failing counts.
3. **CLI Interface**:
   - Exposed as `kb formulas repair [--batch-size 250] [--dry-run]` in `src/kb/cli.py`.
