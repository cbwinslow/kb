# Specification: In-Place Corpus Formula Repair

## Purpose
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

### Requirement: Batch Formula Repair with Quality Gate Integration
The system SHALL support batch-level repair and automated quality gate score elevation across all formulas in `kb_formulas`.

#### Scenario: Progressive repair and scorecard elevation
- **WHEN** user executes `kb corpus repair-all` or `kb formulas repair --evaluate-grades`
- **THEN** system processes invalid or unvalidated formulas, sanitizes LaTeX representations, parses SymPy ASTs, assigns Tier 1–4 diagnostic scores, and writes letter grades in progressive transaction batches.

#### Scenario: Updating diagnostic validation details in-place
- **WHEN** an unvalidated formula is processed by the batch repair pipeline
- **THEN** formula record is updated with `validation_status` ('verified', 'provisional', 'degraded', or 'failed'), `validation_score` (0.0 to 100.0), and a structured `validation_details` JSON payload.
