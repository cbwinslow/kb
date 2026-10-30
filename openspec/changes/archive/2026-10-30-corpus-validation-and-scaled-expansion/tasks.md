# Tasks

## 1. Corpus Auditing & Invariant Verification

- [x] 1.1 Implement `CorpusAuditor` in `src/kb/qa/corpus_auditor.py` checking relational integrity, orphaned records, and vault paths, with unit tests in `tests/test_corpus_auditor.py`
- [x] 1.2 Integrate `kb corpus audit` command into `src/kb/cli.py` and verify execution

## 2. Batch Formula Repair & Quality Gate Scoring

- [x] 2.1 Implement `repair_and_grade_corpus()` in `src/kb/math/repair.py` integrating `CorpusFormulaRepairer` and `FormulaQualityGate`, with unit tests in `tests/test_formula_repair.py`
- [x] 2.2 Add `kb corpus repair-all` command in `src/kb/cli.py` and execute live repair on the PostgreSQL database on `cbwdellr720` to score unvalidated formulas

## 3. Scaled Multi-Domain Preset Harvesting

- [x] 3.1 Execute scaled harvesting across targeted presets (`popular`, `mlb-modeling`, `statcast`, `retrosheet`, `baseball-python`) with pre-download deduplication
- [x] 3.2 Vault newly harvested PDFs and figure assets to homelab storage (`cbwdellr720`), unlinking local temporary files and verifying $\ge 1.5$ GB free disk space

## 4. Vectorized Code Generation & Benchmark Verification

- [x] 4.1 Update standalone `packages/kb_formulas` library export with newly verified Grade A equations using `FormulaLibraryGenerator`
- [x] 4.2 Execute empirical accuracy verification against `kb_benchmark_tables` via `kb benchmark accuracy`
- [x] 4.3 Execute the full tripartite quality gate (`ruff check`, `pyright`, `pytest`) ensuring 100% passing tests and zero warnings
- [x] 4.4 Record ADR-034 in `docs/DECISIONS.md` documenting the corpus audit and batch quality scoring architecture

## Workflow follow-up

- Sync delta specs to main specs with `npx openspec archive corpus-validation-and-scaled-expansion --yes`.
