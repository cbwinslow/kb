# Design: Performance & Quality Benchmarking Suite

## Architecture

```
                                  ┌────────────────────────┐
                                  │      CLI Command       │
                                  │      kb benchmark      │
                                  └───────────┬────────────┘
                                              │
                                  ┌───────────▼────────────┐
                                  │ PerformanceBenchmarker │
                                  │ src/kb/benchmark/      │
                                  │      runner.py         │
                                  └───────────┬────────────┘
                                              │
        ┌───────────────────┬─────────────────┼───────────────────┐
        │                   │                 │                   │
┌───────▼────────┐  ┌───────▼────────┐ ┌──────▼─────────┐ ┌───────▼────────┐
│ Formula Speed  │  │ Embedding Speed│ │ Search Latency │ │ Corpus Quality │
│ Scalar vs      │  │ ms/chunk       │ │ P50 / P95 / Max│ │ AST Parse Rate │
│ Polars Speedup │  │ chunks/sec     │ │ RRF Ranking    │ │ Valid Formulas │
└────────────────┘  └────────────────┘ └────────────────┘ └────────────────┘
```

## Data Models & Result Metrics

```python
@dataclass(slots=True)
class FormulaBenchmarkResult:
    function_name: str
    n_rows: int
    scalar_time_ms: float
    polars_time_ms: float
    scalar_throughput_rows_per_sec: float
    polars_throughput_rows_per_sec: float
    speedup_factor: float

@dataclass(slots=True)
class EmbeddingBenchmarkResult:
    n_chunks: int
    device: str
    total_time_ms: float
    latency_per_chunk_ms: float
    throughput_chunks_per_sec: float

@dataclass(slots=True)
class SearchBenchmarkResult:
    n_queries: int
    p50_latency_ms: float
    p95_latency_ms: float
    max_latency_ms: float
    mean_latency_ms: float

@dataclass(slots=True)
class QualityBenchmarkResult:
    total_formulas: int
    verified_valid: int
    valid_ratio: float
    equalities_count: int
    equality_ratio: float
    compilable_count: int
    compilation_ratio: float

@dataclass(slots=True)
class BenchmarkSuiteResult:
    timestamp: str
    formula_benchmarks: list[FormulaBenchmarkResult]
    embedding_benchmark: EmbeddingBenchmarkResult | None
    search_benchmark: SearchBenchmarkResult | None
    quality_benchmark: QualityBenchmarkResult | None
```

## Reporting Formats
- Terminal Markdown Table rendering.
- Machine-readable JSON output for CI pipelines and regression tracking.
