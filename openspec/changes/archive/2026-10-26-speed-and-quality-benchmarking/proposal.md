# Proposal: Performance & Quality Benchmarking Suite

## 1. Problem Statement
The scientific knowledge base contains over 260 research papers, 32,000 vector embeddings, and 5,800+ extracted formulas. While the pipeline operates robustly, developers and downstream quantitative applications currently lack:
1. **Empirical Execution Speed Benchmarks**: No standardized benchmark exists comparing the throughput (rows/second) and execution time of compiled Python scalar functions versus vectorized Polars column expressions.
2. **Embedding & Ingestion Throughput Telemetry**: No tool measures dense BGE-M3 embedding latency (ms/chunk) and throughput across CPU and CUDA backends.
3. **Retrieval Latency Profiling**: No profiling suite measures P50, P95, and P99 latency for Hybrid Search (combining dense vector distance, full-text `tsvector` matching, and Reciprocal Rank Fusion).
4. **Corpus Quality Auditing**: No automated audit reports the mathematical verification yield, compilation rate, and structural integrity across all corpus formulas in the database.

## 2. Proposed Solution
Build a comprehensive **Performance & Quality Benchmarking Suite**:
1. **Benchmarking Engine (`src/kb/benchmark/runner.py`)**:
   - `benchmark_formula_execution`: Measures scalar Python vs. vectorized Polars throughput across $N$ rows (e.g. 100,000 rows) and calculates the speedup ratio.
   - `benchmark_embedding_throughput`: Generates embeddings for sample text chunks and profiles latency per chunk and total throughput.
   - `benchmark_search_latency`: Runs sample queries against the database, profiling P50, P95, and max response times for Hybrid RRF search.
   - `benchmark_corpus_quality`: Traverses database formulas to measure AST parse success rates, equality detection yield, and symbol distribution.
2. **CLI Integration (`kb benchmark`)**:
   - Add a command-line interface with flags (`--all`, `--formulas`, `--search`, `--embeddings`, `--quality`, `--rows`, `--json`, `--output`).
3. **Automated Testing & Documentation**:
   - Unit and integration tests in `tests/test_benchmark_runner.py`.
   - Record ADR-018 in `docs/DECISIONS.md`.
   - Delta specification in `specs/performance-benchmarking/spec.md`.

## 3. Impact & Portability
- Lightweight execution with mocked/isolated fallbacks for CI environments.
- Fully portable across Windows, Linux, and macOS with zero hardcoded credentials or paths.
