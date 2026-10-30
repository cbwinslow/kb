"""Empirical accuracy benchmark runner evaluating vectorized formulas against datasets."""

from __future__ import annotations

import logging
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

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
    ) -> None:
        """Initialize runner with database manager, ontology, and code compiler."""
        self.db_manager = db_manager or DatabaseManager()
        self.ontology = ontology or get_symbol_ontology()
        self.compiler = compiler or FormulaCompiler()

    def bind_formula_to_table(
        self,
        formula: Formula,
        columns: list[str],
        target_candidate: str | None = None,
        default_constants: dict[str, float] | None = None,
    ) -> TableBindingResult:
        """Map table column headers to formula symbols using SymbolOntology.

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

        # Determine target column
        target_col: str | None = target_candidate
        if not target_col and formula.lhs:
            lhs_clean = formula.lhs.replace("{", "").replace("}", "").replace("\\", "").strip("_")
            lhs_mapping = self.ontology.resolve_column_mapping([lhs_clean], columns)
            if lhs_mapping:
                target_col = lhs_mapping.get(lhs_clean)

        # Resolve parameter columns via ontology
        mapping = self.ontology.resolve_column_mapping(params, columns)

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

        # Case 2: Evaluate against matching benchmark tables in database
        for formula in formulas:
            # Find candidate tables with matching citekey or columns
            candidate_tables = [t for t in tables if t.citekey == formula.citekey]
            if not candidate_tables:
                candidate_tables = tables[:5]  # Try common benchmark tables

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
                    break

        return results
