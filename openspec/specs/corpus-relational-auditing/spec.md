# Corpus Relational & Health Auditing Specification

## Purpose
Ensure corpus-wide relational integrity across documents, text chunks, LaTeX formulas, benchmark fixtures, and figures, while providing automated in-place repair and quality grade elevation.

## Requirements

### Requirement 1: Invariant & Orphan Verification
The `CorpusAuditor` MUST verify that:
1. Zero chunks exist without a valid parent document foreign key.
2. Zero formulas exist without a valid parent chunk foreign key.
3. Every document has associated text chunks and metadata.
4. All database records link cleanly to permanent vault fixtures.

### Requirement 2: Formula Health Breakdown
The audit report MUST track:
- Total formulas and validation status counts (Verified, Provisional, Degraded, Failed, Unvalidated).
- Grade distributions (A, B, C, D, F).
- Relational violations and diagnostic messages.

### Requirement 3: Automated In-Place Corpus Repair
`CorpusFormulaRepairer` MUST provide batch in-place re-sanitization, SymPy AST compilation, and Tier 1–4 quality grading in atomic transactions with configurable limits and batch sizes.
