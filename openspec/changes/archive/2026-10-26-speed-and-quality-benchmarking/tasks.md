# Tasks: Performance & Quality Benchmarking Suite

## Phase 1: Benchmarking Engine Implementation
- [x] Create `src/kb/benchmark/__init__.py` and `src/kb/benchmark/runner.py` with `PerformanceBenchmarker` <!-- id: 201 -->
- [x] Implement `benchmark_formula_execution` (Scalar vs. Vectorized Polars) <!-- id: 202 -->
- [x] Implement `benchmark_embedding_throughput` (Dense BGE-M3 latency) <!-- id: 203 -->
- [x] Implement `benchmark_search_latency` (Hybrid RRF latency profiling) <!-- id: 204 -->
- [x] Implement `benchmark_corpus_quality` (Formula AST validation yield) <!-- id: 205 -->

## Phase 2: CLI Integration
- [x] Add `kb benchmark` CLI parser and async handler in `src/kb/cli.py` <!-- id: 206 -->
- [x] Support `--all`, `--formulas`, `--embeddings`, `--search`, `--quality`, `--rows`, `--json`, and `--output` flags <!-- id: 207 -->

## Phase 3: Testing & Verification
- [x] Create `tests/test_benchmark_runner.py` with mock and real execution tests <!-- id: 208 -->
- [x] Verify execution with `uv run pytest tests/test_benchmark_runner.py` <!-- id: 209 -->
- [x] Run full test suite, `ruff check`, and `pyright` <!-- id: 210 -->

## Phase 4: OpenSpec Sync, ADR, & Documentation
- [x] Create `openspec/specs/performance-benchmarking/spec.md` <!-- id: 211 -->
- [x] Record ADR-018 in `docs/DECISIONS.md` <!-- id: 212 -->
- [x] Archive change under `openspec/changes/archive/` <!-- id: 213 -->
- [x] Update `README.md` and `openspec/project.md` <!-- id: 214 -->
- [x] Git commit and push to remote <!-- id: 215 -->
