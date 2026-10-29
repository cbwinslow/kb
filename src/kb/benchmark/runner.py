"""Performance and quality benchmarking engine for scientific formulas, embeddings, and retrieval."""

from __future__ import annotations

import datetime
import json
import logging
import statistics
import time
from dataclasses import asdict, dataclass
from typing import Any

import polars as pl
from sqlalchemy import func, select

from kb.codegen.compiler import FormulaCompiler
from kb.logging import timed_stage
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import LocalEmbeddingGenerator
from kb.storage.models import Formula
from kb.storage.search import HybridSearchEngine

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class FormulaBenchmarkResult:
    """Benchmark metrics comparing scalar Python loop vs vectorized Polars expression."""

    function_name: str
    n_rows: int
    scalar_time_ms: float
    polars_time_ms: float
    scalar_throughput_rows_per_sec: float
    polars_throughput_rows_per_sec: float
    speedup_factor: float


@dataclass(slots=True)
class EmbeddingBenchmarkResult:
    """Benchmark metrics for dense vector embedding generation throughput."""

    n_chunks: int
    device: str
    total_time_ms: float
    latency_per_chunk_ms: float
    throughput_chunks_per_sec: float


@dataclass(slots=True)
class SearchBenchmarkResult:
    """Latency metrics for Hybrid RRF Search across the corpus."""

    n_queries: int
    p50_latency_ms: float
    p95_latency_ms: float
    max_latency_ms: float
    mean_latency_ms: float


@dataclass(slots=True)
class QualityBenchmarkResult:
    """Corpus mathematical formula verification and compilation yield scorecard."""

    total_formulas: int
    verified_valid: int
    valid_ratio: float
    equalities_count: int
    equality_ratio: float
    compilable_count: int
    compilation_ratio: float


@dataclass(slots=True)
class BenchmarkSuiteResult:
    """Aggregated results across all performance and quality benchmark suites."""

    timestamp: str
    formula_benchmarks: list[FormulaBenchmarkResult]
    embedding_benchmark: EmbeddingBenchmarkResult | None
    search_benchmark: SearchBenchmarkResult | None
    quality_benchmark: QualityBenchmarkResult | None

    def to_dict(self) -> dict[str, Any]:
        """Convert results to serializable dictionary."""
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        """Convert results to formatted JSON string."""
        return json.dumps(self.to_dict(), indent=indent)

    def to_markdown(self) -> str:
        """Render results as a formatted GitHub Flavored Markdown report."""
        lines = [
            f"# KB Performance & Quality Benchmark Report ({self.timestamp})",
            "",
        ]

        if self.formula_benchmarks:
            lines.extend(
                [
                    "## 1. Formula Execution Speed (Scalar Python vs. Vectorized Polars)",
                    "| Formula | Rows | Scalar (ms) | Polars (ms) | Scalar Throughput | Polars Throughput | Speedup |",
                    "|---|---|---|---|---|---|---|",
                ]
            )
            for f in self.formula_benchmarks:
                lines.append(
                    f"| `{f.function_name}` | {f.n_rows:,} | {f.scalar_time_ms:.2f} ms | "
                    f"{f.polars_time_ms:.2f} ms | {f.scalar_throughput_rows_per_sec:,.0f} rows/s | "
                    f"{f.polars_throughput_rows_per_sec:,.0f} rows/s | **{f.speedup_factor:.1f}x** |"
                )
            lines.append("")

        if self.embedding_benchmark:
            e = self.embedding_benchmark
            lines.extend(
                [
                    "## 2. Dense Vector Embedding Generation (BGE-M3)",
                    f"- **Device**: `{e.device}`",
                    f"- **Chunks Processed**: {e.n_chunks}",
                    f"- **Latency per Chunk**: {e.latency_per_chunk_ms:.2f} ms",
                    f"- **Throughput**: {e.throughput_chunks_per_sec:.2f} chunks/sec",
                    f"- **Total Time**: {e.total_time_ms:.2f} ms",
                    "",
                ]
            )

        if self.search_benchmark:
            s = self.search_benchmark
            lines.extend(
                [
                    "## 3. Hybrid Search Latency (RRF Fusion)",
                    f"- **Queries Evaluated**: {s.n_queries}",
                    f"- **Mean Latency**: {s.mean_latency_ms:.2f} ms",
                    f"- **P50 (Median)**: {s.p50_latency_ms:.2f} ms",
                    f"- **P95 Latency**: {s.p95_latency_ms:.2f} ms",
                    f"- **Max Latency**: {s.max_latency_ms:.2f} ms",
                    "",
                ]
            )

        if self.quality_benchmark:
            q = self.quality_benchmark
            lines.extend(
                [
                    "## 4. Corpus Formula Quality Scorecard",
                    f"- **Total Formulas**: {q.total_formulas:,}",
                    f"- **Verified Valid**: {q.verified_valid:,} ({q.valid_ratio * 100:.1f}%)",
                    f"- **Explicit Equalities**: {q.equalities_count:,} ({q.equality_ratio * 100:.1f}%)",
                    f"- **Compilable Functions**: {q.compilable_count:,} ({q.compilation_ratio * 100:.1f}%)",
                    "",
                ]
            )

        return "\n".join(lines)


class PerformanceBenchmarker:
    """Profiles system execution speed, latency, throughput, and mathematical formula quality."""

    def __init__(self, db_manager: DatabaseManager | None = None) -> None:
        self.manager = db_manager or DatabaseManager()
        self.compiler = FormulaCompiler()

    def benchmark_formula_execution(self, n_rows: int = 100_000) -> list[FormulaBenchmarkResult]:
        """Benchmarks pure Python loop vs. vectorized Polars expression across standard formulas."""
        logger.info("Benchmarking formula execution across %d rows...", n_rows)
        results: list[FormulaBenchmarkResult] = []

        # Benchmark 1: Pythagorean Expectation: W = R^g / (R^g + RA^g)
        df_pyth = pl.DataFrame(
            {
                "R": [700.0 + (i % 100) for i in range(n_rows)],
                "RA": [650.0 + (i % 80) for i in range(n_rows)],
                "gamma": [1.83] * n_rows,
            }
        )

        # Scalar timing
        r_list = df_pyth["R"].to_list()
        ra_list = df_pyth["RA"].to_list()
        gamma_list = df_pyth["gamma"].to_list()

        start = time.perf_counter()
        _scalar_out = [
            (r**g) / (r**g + ra**g) for r, ra, g in zip(r_list, ra_list, gamma_list, strict=True)
        ]
        scalar_ms = (time.perf_counter() - start) * 1000.0

        # Polars timing
        pyth_expr = pl.col("R") ** pl.col("gamma") / (
            pl.col("R") ** pl.col("gamma") + pl.col("RA") ** pl.col("gamma")
        )
        start = time.perf_counter()
        _df_out = df_pyth.with_columns(pyth_expr.alias("W_pct"))
        polars_ms = (time.perf_counter() - start) * 1000.0

        scalar_throughput = (n_rows / scalar_ms) * 1000.0
        polars_throughput = (n_rows / polars_ms) * 1000.0
        speedup = scalar_ms / polars_ms if polars_ms > 0 else 1.0

        results.append(
            FormulaBenchmarkResult(
                function_name="pythagorean_expectation",
                n_rows=n_rows,
                scalar_time_ms=scalar_ms,
                polars_time_ms=polars_ms,
                scalar_throughput_rows_per_sec=scalar_throughput,
                polars_throughput_rows_per_sec=polars_throughput,
                speedup_factor=speedup,
            )
        )

        # Benchmark 2: FIP = (13*HR + 3*(BB + HBP) - 2*K) / IP + C
        df_fip = pl.DataFrame(
            {
                "HR": [20.0 + (i % 15) for i in range(n_rows)],
                "BB": [50.0 + (i % 25) for i in range(n_rows)],
                "HBP": [5.0 + (i % 5) for i in range(n_rows)],
                "K": [180.0 + (i % 40) for i in range(n_rows)],
                "IP": [200.0 + (i % 30) for i in range(n_rows)],
                "C": [3.10] * n_rows,
            }
        )

        hr_l = df_fip["HR"].to_list()
        bb_l = df_fip["BB"].to_list()
        hbp_l = df_fip["HBP"].to_list()
        k_l = df_fip["K"].to_list()
        ip_l = df_fip["IP"].to_list()
        c_l = df_fip["C"].to_list()

        start = time.perf_counter()
        _scalar_fip = [
            ((13.0 * hr + 3.0 * (bb + hbp) - 2.0 * k) / ip) + c
            for hr, bb, hbp, k, ip, c in zip(hr_l, bb_l, hbp_l, k_l, ip_l, c_l, strict=True)
        ]
        scalar_fip_ms = (time.perf_counter() - start) * 1000.0

        fip_expr = (
            13.0 * pl.col("HR") + 3.0 * (pl.col("BB") + pl.col("HBP")) - 2.0 * pl.col("K")
        ) / pl.col("IP") + pl.col("C")
        start = time.perf_counter()
        _df_fip_out = df_fip.with_columns(fip_expr.alias("FIP"))
        polars_fip_ms = (time.perf_counter() - start) * 1000.0

        scalar_fip_throughput = (n_rows / scalar_fip_ms) * 1000.0
        polars_fip_throughput = (n_rows / polars_fip_ms) * 1000.0
        speedup_fip = scalar_fip_ms / polars_fip_ms if polars_fip_ms > 0 else 1.0

        results.append(
            FormulaBenchmarkResult(
                function_name="fielding_independent_pitching",
                n_rows=n_rows,
                scalar_time_ms=scalar_fip_ms,
                polars_time_ms=polars_fip_ms,
                scalar_throughput_rows_per_sec=scalar_fip_throughput,
                polars_throughput_rows_per_sec=polars_fip_throughput,
                speedup_factor=speedup_fip,
            )
        )

        return results

    @timed_stage("benchmark_embeddings")
    def benchmark_embedding_throughput(self, n_chunks: int = 20) -> EmbeddingBenchmarkResult:
        """Benchmarks dense BGE-M3 vector embedding generation latency and throughput."""
        generator = LocalEmbeddingGenerator()
        sample_texts = [
            f"Mathematical analysis of baseball trajectory and spin physics in section {i}."
            for i in range(n_chunks)
        ]

        start = time.perf_counter()
        _embeddings = generator.embed_texts(sample_texts)
        total_ms = (time.perf_counter() - start) * 1000.0

        latency_per_chunk = total_ms / n_chunks if n_chunks > 0 else 0.0
        throughput = (n_chunks / total_ms) * 1000.0 if total_ms > 0 else 0.0

        return EmbeddingBenchmarkResult(
            n_chunks=n_chunks,
            device=generator.device,
            total_time_ms=total_ms,
            latency_per_chunk_ms=latency_per_chunk,
            throughput_chunks_per_sec=throughput,
        )

    @timed_stage("benchmark_search")
    async def benchmark_search_latency(
        self, queries: list[str] | None = None
    ) -> SearchBenchmarkResult:
        """Profiles Hybrid Search response times across multiple test queries."""
        test_queries = queries or [
            "pythagorean expectation win percentage formula",
            "aerodynamics of baseball drag coefficient spin",
            "fielding independent pitching sabermetrics",
            "statcast launch angle exit velocity run value",
            "openWAR replacement level player performance",
        ]

        searcher = HybridSearchEngine(db_manager=self.manager)
        embedder = LocalEmbeddingGenerator()
        latencies_ms: list[float] = []

        async with self.manager.session_factory() as session:
            for q in test_queries:
                start = time.perf_counter()
                _results = await searcher.search(
                    session=session,
                    query_text=q,
                    embedder=embedder,
                    limit=5,
                )
                elapsed_ms = (time.perf_counter() - start) * 1000.0
                latencies_ms.append(elapsed_ms)

        latencies_ms.sort()
        n = len(latencies_ms)
        p50 = latencies_ms[n // 2] if n > 0 else 0.0
        p95_idx = min(int(n * 0.95), n - 1) if n > 0 else 0
        p95 = latencies_ms[p95_idx] if n > 0 else 0.0
        max_lat = latencies_ms[-1] if n > 0 else 0.0
        mean_lat = statistics.mean(latencies_ms) if n > 0 else 0.0

        return SearchBenchmarkResult(
            n_queries=n,
            p50_latency_ms=p50,
            p95_latency_ms=p95,
            max_latency_ms=max_lat,
            mean_latency_ms=mean_lat,
        )

    @timed_stage("benchmark_quality")
    async def benchmark_corpus_quality(self) -> QualityBenchmarkResult:
        """Audits mathematical quality, verification rates, and compilation yield across the corpus."""
        async with self.manager.session_factory() as session:
            total_cnt = (await session.execute(select(func.count(Formula.id)))).scalar_one()
            valid_cnt = (
                await session.execute(
                    select(func.count(Formula.id)).where(Formula.is_valid == True)  # noqa: E712
                )
            ).scalar_one()
            equality_cnt = (
                await session.execute(
                    select(func.count(Formula.id)).where(Formula.is_equality == True)  # noqa: E712
                )
            ).scalar_one()

            # Measure sample compilation yield (first 100 valid formulas)
            sample_stmt = (
                select(Formula)
                .where(Formula.is_valid == True)  # noqa: E712
                .limit(100)
            )
            sample_formulas = list((await session.execute(sample_stmt)).scalars().all())
            compilable = 0
            for f in sample_formulas:
                res = self.compiler.compile(
                    formula_id=f.id,
                    citekey=f.citekey,
                    raw_latex=f.raw_latex,
                    sympy_repr=f.sympy_repr,
                )
                if res.is_valid:
                    compilable += 1

            sample_size = len(sample_formulas)
            compilation_ratio = (compilable / sample_size) if sample_size > 0 else 0.0
            estimated_compilable = int(valid_cnt * compilation_ratio)

            return QualityBenchmarkResult(
                total_formulas=total_cnt,
                verified_valid=valid_cnt,
                valid_ratio=(valid_cnt / total_cnt) if total_cnt > 0 else 0.0,
                equalities_count=equality_cnt,
                equality_ratio=(equality_cnt / total_cnt) if total_cnt > 0 else 0.0,
                compilable_count=estimated_compilable,
                compilation_ratio=compilation_ratio,
            )

    async def run_all(
        self,
        n_rows: int = 100_000,
        n_chunks: int = 20,
        queries: list[str] | None = None,
    ) -> BenchmarkSuiteResult:
        """Runs the entire performance and quality benchmarking suite."""
        logger.info("Executing full benchmark suite...")
        now_str = datetime.datetime.now(datetime.UTC).isoformat()

        formula_res = self.benchmark_formula_execution(n_rows=n_rows)
        embedding_res = self.benchmark_embedding_throughput(n_chunks=n_chunks)
        search_res = await self.benchmark_search_latency(queries=queries)
        quality_res = await self.benchmark_corpus_quality()

        return BenchmarkSuiteResult(
            timestamp=now_str,
            formula_benchmarks=formula_res,
            embedding_benchmark=embedding_res,
            search_benchmark=search_res,
            quality_benchmark=quality_res,
        )
