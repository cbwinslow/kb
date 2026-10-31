"""Empirical accuracy benchmark runner evaluating vectorized formulas against datasets."""

from __future__ import annotations

import logging
import math
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, ClassVar

import numpy as np
import polars as pl
from pydantic import BaseModel, Field
from sqlalchemy import select

from kb.codegen.compiler import FormulaCompiler
from kb.math.ontology import SymbolOntology, get_symbol_ontology
from kb.storage.database import DatabaseManager
from kb.storage.models import BenchmarkTable, Formula

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class AccuracyMetrics:
    """Statistical accuracy metrics comparing vectorized formula predictions to ground truth."""

    mae: float
    rmse: float
    r_squared: float
    max_relative_error: float
    num_samples: int
    throughput_rows_per_sec: float
    passed: bool

    def to_dict(self) -> dict[str, Any]:
        """Convert metrics to a serializable dictionary."""
        return {
            "mae": round(self.mae, 6),
            "rmse": round(self.rmse, 6),
            "r_squared": round(self.r_squared, 6),
            "max_relative_error": round(self.max_relative_error, 6),
            "num_samples": self.num_samples,
            "throughput_rows_per_sec": round(self.throughput_rows_per_sec, 1),
            "passed": self.passed,
        }


class TableBindingResult(BaseModel):
    """Result of mapping a formula's argument symbols to table columns."""

    matched_columns: dict[str, str] = Field(
        default_factory=dict, description="Map from formula parameter -> table column"
    )
    missing_symbols: list[str] = Field(
        default_factory=list, description="Formula parameters not found in table columns"
    )
    constants: dict[str, float] = Field(
        default_factory=dict, description="Injected default numerical constants"
    )
    target_column: str | None = Field(
        default=None, description="Identified ground-truth output column"
    )
    is_bound: bool = Field(default=False, description="Whether all required parameters are bound")


class HeuristicColumnMatcher:
    """Fuzzy column matcher combining domain synonym mappings, ontology aliases, and token similarity."""

    # Domain synonyms bridging mathematical symbols, abbreviations, and empirical tracking column names
    SYNONYM_GROUPS: ClassVar[list[set[str]]] = [
        # Velocity / speed
        {"v_0", "v0", "v", "v_launch", "exit_velocity", "launch_speed", "pitch_speed", "velocity", "speed", "ev"},
        # Launch angle / pitch angle
        {"theta", "launch_angle", "angle", "pitch_angle", "vertical_angle", "la"},
        # Spin rate
        {"omega", "spin_rate", "spin", "release_spin_rate", "rotational_speed"},
        # Spin axis / direction
        {"phi", "spin_axis", "spin_direction", "axis"},
        # Distance
        {"d", "x", "dist", "distance", "hit_distance_sc", "total_distance", "carry"},
        # Aerodynamic coefficients
        {"cd", "drag_coef", "drag_coefficient", "c_d"},
        {"cl", "lift_coef", "lift_coefficient", "c_l"},
        # Baseball run values
        {"r_s", "rs", "runs_scored", "runs", "r"},
        {"r_a", "ra", "runs_allowed"},
        {"w_oba", "woba", "woba_value"},
        {"b_abip", "babip"},
        {"f_ip", "fip"},
        {"e_ra", "era"},
        {"w_ar", "war"},
        {"h_r", "hr", "home_runs"},
        {"b_b", "bb", "walks"},
        {"s_o", "so", "strikeouts", "k"},
        {"i_p", "ip", "innings_pitched", "outs"},
        {"a_b", "ab", "at_bats"},
    ]

    def __init__(self, ontology: SymbolOntology | None = None) -> None:
        """Initialize heuristic matcher with ontology and indexed synonym groups."""
        self.ontology = ontology or get_symbol_ontology()
        self._lookup: dict[str, set[str]] = {}
        for group in self.SYNONYM_GROUPS:
            for item in group:
                self._lookup[item.lower()] = group

    def _normalize(self, s: str) -> str:
        clean = re.sub(r"[{}\\^]", "", s)
        clean = re.sub(r"[\s\-+*/(),]+", "_", clean)
        return clean.strip("_").lower()

    def _levenshtein_similarity(self, s1: str, s2: str) -> float:
        """Compute normalized similarity ratio between two strings [0.0, 1.0]."""
        if s1 == s2:
            return 1.0
        if not s1 or not s2:
            return 0.0
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + cost,
                )
        dist = dp[len1][len2]
        max_len = max(len1, len2)
        return 1.0 - (dist / max_len)

    def match_column(
        self, symbol: str, available_columns: list[str], threshold: float = 0.75
    ) -> str | None:
        """Find the best matching column for a formula parameter symbol.

        Resolution stages:
        1. Exact match (case sensitive or insensitive)
        2. Ontology canonical resolution
        3. Synonym group dictionary matching
        4. Normalized substring / prefix matching
        5. Fuzzy Levenshtein token similarity (>= threshold)
        """
        if not symbol:
            return None

        # 1. Exact match
        if symbol in available_columns:
            return symbol
        norm_sym = self._normalize(symbol)
        for col in available_columns:
            if self._normalize(col) == norm_sym:
                return col

        # 2. Ontology match
        sym_canon = self.ontology.resolve_canonical(symbol)
        if sym_canon:
            for col in available_columns:
                col_canon = self.ontology.resolve_canonical(col)
                if col_canon == sym_canon:
                    return col

        # 3. Synonym dictionary match
        if norm_sym in self._lookup:
            synonyms = self._lookup[norm_sym]
            for col in available_columns:
                if self._normalize(col) in synonyms:
                    return col

        # 4. Normalized substring / prefix match
        for col in available_columns:
            norm_col = self._normalize(col)
            if norm_sym and len(norm_sym) >= 3 and (norm_sym in norm_col or norm_col in norm_sym):
                return col

        # 5. Fuzzy Levenshtein similarity
        best_col: str | None = None
        best_score = 0.0
        for col in available_columns:
            score = self._levenshtein_similarity(norm_sym, self._normalize(col))
            if score > best_score and score >= threshold:
                best_score = score
                best_col = col

        return best_col


def discover_fixtures(fixtures_dir: Path | str = "data/fixtures") -> list[dict[str, Any]]:
    """Scan fixture directory for Parquet and CSV datasets and extract column schemas lazily."""
    p_dir = Path(fixtures_dir)
    if not p_dir.exists():
        return []

    discovered: list[dict[str, Any]] = []
    for pq_path in p_dir.rglob("*.parquet"):
        try:
            schema = pl.read_parquet_schema(pq_path)
            cols = list(schema.keys())
            discovered.append(
                {
                    "path": str(pq_path),
                    "name": pq_path.stem,
                    "format": "parquet",
                    "columns": cols,
                    "citekey": pq_path.parent.name if pq_path.parent != p_dir else pq_path.stem,
                }
            )
        except Exception as exc:  # noqa: BLE001
            logger.debug("Failed to read parquet schema for %s: %s", pq_path, exc)

    return discovered


class EmpiricalAccuracyRunner:
    """Executes vectorized formulas against tabular benchmark datasets and records telemetry."""

    DEFAULT_CONSTANTS: dict[str, float] = {
        "c": 3.10,
        "gamma": 1.83,
        "g": 9.80665,
        "pi": math.pi,
        "rho": 1.225,
    }

    def __init__(
        self,
        db_manager: DatabaseManager | None = None,
        ontology: SymbolOntology | None = None,
        compiler: FormulaCompiler | None = None,
        matcher: HeuristicColumnMatcher | None = None,
    ) -> None:
        """Initialize runner with database manager, ontology, code compiler, and heuristic matcher."""
        self.db_manager = db_manager or DatabaseManager()
        self.ontology = ontology or get_symbol_ontology()
        self.compiler = compiler or FormulaCompiler()
        self.matcher = matcher or HeuristicColumnMatcher(ontology=self.ontology)

    def bind_formula_to_table(
        self,
        formula: Formula,
        columns: list[str],
        target_candidate: str | None = None,
        default_constants: dict[str, float] | None = None,
    ) -> TableBindingResult:
        """Map table column headers to formula symbols using HeuristicColumnMatcher and SymbolOntology.

        Args:
            formula: Formula database entity with symbols and LHS/RHS.
            columns: Available column names in the dataset table.
            target_candidate: Optional explicit target ground-truth column name.
            default_constants: Optional override dictionary of constant symbols.

        Returns:
            TableBindingResult detailing resolved parameters, constants, and target column.
        """
        all_constants = {**self.DEFAULT_CONSTANTS, **(default_constants or {})}
        symbols = [s for s in (formula.symbols or []) if s]
        comp = self.compiler.compile(
            formula_id=formula.id,
            citekey=formula.citekey,
            raw_latex=formula.sanitized_latex or formula.raw_latex,
            sympy_repr=formula.sympy_repr,
        )
        params = comp.parameters if comp.is_valid and comp.parameters else symbols

        # Determine target column via heuristic matcher
        target_col: str | None = target_candidate
        if not target_col and formula.lhs:
            target_col = self.matcher.match_column(formula.lhs, columns)

        # Resolve parameter columns via heuristic matcher
        mapping: dict[str, str] = {}
        for p in params:
            m_col = self.matcher.match_column(p, columns)
            if m_col:
                mapping[p] = m_col

        missing: list[str] = []
        injected_constants: dict[str, float] = {}

        for p in params:
            if p in mapping:
                continue
            # Check if parameter is a known constant
            norm_p = p.lower()
            if norm_p in all_constants:
                injected_constants[p] = all_constants[norm_p]
            else:
                missing.append(p)

        is_bound = len(missing) == 0 and (target_col is not None or target_candidate is not None)

        return TableBindingResult(
            matched_columns=mapping,
            missing_symbols=missing,
            constants=injected_constants,
            target_column=target_col,
            is_bound=is_bound,
        )

    def evaluate_vectorized(
        self,
        df: pl.DataFrame,
        formula: Formula,
        target_column: str,
        param_mapping: dict[str, str] | None = None,
        constants: dict[str, float] | None = None,
        tolerance_r2: float = 0.95,
        tolerance_mae: float = 1.0,
    ) -> AccuracyMetrics:
        """Evaluate vectorized Polars expression across all rows of the dataset.

        Args:
            df: Input Polars DataFrame.
            formula: Formula to evaluate.
            target_column: Name of ground-truth column to compare against.
            param_mapping: Mapping of formula parameter name -> column name in df.
            constants: Numerical constants to inject.
            tolerance_r2: Minimum acceptable R^2 score.
            tolerance_mae: Maximum acceptable MAE score.

        Returns:
            AccuracyMetrics detailing MAE, RMSE, R^2, and execution throughput.
        """
        comp = self.compiler.compile(
            formula_id=formula.id,
            citekey=formula.citekey,
            raw_latex=formula.sanitized_latex or formula.raw_latex,
            sympy_repr=formula.sympy_repr,
        )
        if not comp.is_valid or not comp.polars_expression:
            raise ValueError(f"Formula '{formula.id}' could not be compiled to a Polars expression.")

        # Alias columns in DataFrame to match formula parameter names
        mapping = param_mapping or {}
        alias_exprs: list[pl.Expr] = []
        for param, col_name in mapping.items():
            if col_name in df.columns and param != col_name:
                alias_exprs.append(pl.col(col_name).cast(pl.Float64, strict=False).alias(param))

        # Inject constants as literal columns
        const_dict = {**self.DEFAULT_CONSTANTS, **(constants or {})}
        for k, v in const_dict.items():
            if k not in df.columns:
                alias_exprs.append(pl.lit(float(v)).alias(k))

        working_df = df.with_columns(alias_exprs) if alias_exprs else df

        # Evaluate the compiled Polars expression in the polars namespace
        polars_expr_str = comp.polars_expression
        eval_scope: dict[str, Any] = {"pl": pl, "math": math}
        try:
            expr: pl.Expr = eval(polars_expr_str, eval_scope)
        except Exception as exc:
            raise RuntimeError(
                f"Failed to parse Polars expression '{polars_expr_str}': {exc}"
            ) from exc

        start_time = time.perf_counter()
        pred_df = working_df.select(
            [
                expr.cast(pl.Float64, strict=False).alias("__pred__"),
                pl.col(target_column).cast(pl.Float64, strict=False).alias("__target__"),
            ]
        ).drop_nulls()

        elapsed = time.perf_counter() - start_time
        num_samples = len(pred_df)
        if num_samples == 0:
            raise ValueError("Evaluation produced 0 valid non-null samples.")

        y_pred = pred_df["__pred__"].to_numpy()
        y_true = pred_df["__target__"].to_numpy()

        diff = y_pred - y_true
        mae = float(np.mean(np.abs(diff)))
        rmse = float(np.sqrt(np.mean(diff**2)))

        ss_res = float(np.sum(diff**2))
        ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
        r2 = float(1.0 - (ss_res / ss_tot)) if ss_tot > 1e-9 else 1.0

        denom = np.abs(y_true) + 1e-9
        max_rel_err = float(np.max(np.abs(diff) / denom))
        throughput = num_samples / max(elapsed, 1e-6)

        passed = bool(r2 >= tolerance_r2 and mae <= tolerance_mae)

        return AccuracyMetrics(
            mae=mae,
            rmse=rmse,
            r_squared=r2,
            max_relative_error=max_rel_err,
            num_samples=num_samples,
            throughput_rows_per_sec=throughput,
            passed=passed,
        )

    async def benchmark_formula_against_table(
        self,
        formula: Formula,
        table: BenchmarkTable,
        persist_telemetry: bool = True,
    ) -> AccuracyMetrics | None:
        """Benchmark a single formula against a database BenchmarkTable Parquet fixture."""
        if not table.parquet_path or not Path(table.parquet_path).exists():
            return None

        try:
            df = pl.read_parquet(table.parquet_path)
        except Exception as exc:
            logger.warning("Failed to read parquet table %s: %exc", table.parquet_path, exc)
            return None

        binding = self.bind_formula_to_table(formula, df.columns)
        if not binding.is_bound or not binding.target_column:
            return None

        try:
            metrics = self.evaluate_vectorized(
                df=df,
                formula=formula,
                target_column=binding.target_column,
                param_mapping=binding.matched_columns,
                constants=binding.constants,
            )
        except Exception as exc:
            logger.debug("Vectorized eval failed for formula %s on table %s: %s", formula.id, table.id, exc)
            return None

        if persist_telemetry:
            async with self.db_manager.session_factory() as session:
                f_record = (
                    await session.execute(select(Formula).where(Formula.id == formula.id))
                ).scalar_one_or_none()
                if f_record:
                    details = dict(f_record.validation_details or {})
                    tier_scores = dict(details.get("tier_scores") or {})
                    tier_scores["empirical_benchmark"] = 25.0 if metrics.passed else 15.0
                    details["tier_scores"] = tier_scores
                    details["accuracy_metrics"] = metrics.to_dict()
                    f_record.validation_details = details
                    await session.commit()

        return metrics

    async def benchmark_corpus(
        self,
        min_grade: str = "A",
        min_score: float = 88.0,
        dataset_path: Path | str | None = None,
        target_column: str | None = None,
        limit: int | None = None,
        persist_telemetry: bool = True,
        run_all: bool = False,
        fixtures_dir: Path | str = "data/fixtures",
    ) -> list[dict[str, Any]]:
        """Run vectorized empirical accuracy benchmarks across verified formulas in the corpus."""
        await self.db_manager.init_db()

        async with self.db_manager.session_factory() as session:
            stmt = select(Formula).where(Formula.is_valid.is_(True))
            if min_grade.upper() == "A":
                stmt = stmt.where(Formula.validation_score >= min_score)
            if limit:
                stmt = stmt.limit(limit)

            formulas = list((await session.execute(stmt)).scalars().all())

            # Load benchmark tables if no standalone dataset is provided
            tables: list[BenchmarkTable] = []
            if not dataset_path:
                tbl_stmt = select(BenchmarkTable).where(BenchmarkTable.parquet_path.is_not(None))
                tables = list((await session.execute(tbl_stmt)).scalars().all())

        results: list[dict[str, Any]] = []

        # Case 1: Standalone dataset path provided
        if dataset_path and Path(dataset_path).exists():
            df = pl.read_parquet(dataset_path)
            for formula in formulas:
                binding = self.bind_formula_to_table(
                    formula, df.columns, target_candidate=target_column
                )
                if not binding.is_bound or not binding.target_column:
                    continue
                try:
                    metrics = self.evaluate_vectorized(
                        df=df,
                        formula=formula,
                        target_column=binding.target_column,
                        param_mapping=binding.matched_columns,
                        constants=binding.constants,
                    )
                    results.append(
                        {
                            "formula_id": formula.id,
                            "citekey": formula.citekey,
                            "target_column": binding.target_column,
                            "metrics": metrics.to_dict(),
                        }
                    )
                except Exception:
                    continue
            return results

        # Case 2: Discover and evaluate across local fixtures if run_all or tables empty
        discovered = discover_fixtures(fixtures_dir) if (run_all or not tables) else []
        for formula in formulas:
            evaluated = False

            # First, check database BenchmarkTable entries if available
            candidate_tables = [t for t in tables if t.citekey == formula.citekey]
            if not candidate_tables and not run_all:
                candidate_tables = tables[:5]

            for table in candidate_tables:
                metrics = await self.benchmark_formula_against_table(
                    formula=formula,
                    table=table,
                    persist_telemetry=persist_telemetry,
                )
                if metrics is not None:
                    results.append(
                        {
                            "formula_id": formula.id,
                            "citekey": formula.citekey,
                            "table_id": table.id,
                            "metrics": metrics.to_dict(),
                        }
                    )
                    evaluated = True
                    break

            if evaluated:
                continue

            # Second, check discovered parquet fixtures
            candidate_fixtures = [
                f for f in discovered if formula.citekey and formula.citekey in f["name"]
            ]
            if not candidate_fixtures and run_all:
                candidate_fixtures = discovered[:20]

            for fixture in candidate_fixtures:
                binding = self.bind_formula_to_table(formula, fixture["columns"])
                if not binding.is_bound or not binding.target_column:
                    continue
                try:
                    df = pl.read_parquet(fixture["path"])
                    metrics = self.evaluate_vectorized(
                        df=df,
                        formula=formula,
                        target_column=binding.target_column,
                        param_mapping=binding.matched_columns,
                        constants=binding.constants,
                    )
                    results.append(
                        {
                            "formula_id": formula.id,
                            "citekey": formula.citekey,
                            "fixture_name": fixture["name"],
                            "metrics": metrics.to_dict(),
                        }
                    )
                    break
                except Exception:
                    continue

        return results
