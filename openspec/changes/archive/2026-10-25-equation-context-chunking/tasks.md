# Tasks: Advanced Context-Aware Chunking & Equation Co-occurrence

## 1. Symbol & Cross-Reference Extraction Utilities

- [x] 1.1 Implement `extract_math_symbols` and `extract_equation_references` in `src/kb/math/extractor.py` to identify mathematical variables, Greek symbols, and equation cross-links. Verify with unit tests in `tests/test_formula.py`.

## 2. Derivation Clustering and Context Enrichment

- [x] 2.1 Implement derivation window clustering and symbol context enrichment in `DocumentChunker` in `src/kb/ingest/chunker.py`. Verify that adjacent derivation chunks and trailing variable definitions are merged within token limits.
- [x] 2.2 Add unit tests in `tests/test_ingest.py` validating derivation clustering, symbol header formatting, and equation cross-reference propagation. Verify with `uv run pytest tests/test_ingest.py`.

## 3. Integration and Verification

- [x] 3.1 Test re-chunking of a synthetic multi-equation derivation and verify that search retrieval for defined mathematical symbols correctly matches the parent derivation chunk. Verify with unit test execution.
- [x] 3.2 Run linters, type checks, and complete test suite: `uv run ruff check src tests`, `uv run pyright src tests`, and `uv run pytest -m "not slow"`.

## Workflow follow-up

- Archive the change after review requirements are satisfied.
- Commit changes to git tracking.
