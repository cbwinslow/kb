"""Empirical verifier for compiled mathematical formulas against benchmark tables and test cases."""

from __future__ import annotations

import logging
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any, cast

import polars as pl

from kb.codegen.compiler import FormulaCompiler
from kb.codegen.models import CodeGenerationResult, VerificationResult

logger = logging.getLogger(__name__)


class FormulaVerifier:
    """Validates compiled Python functions against empirical tables and test vectors."""

    def __init__(self, compiler: FormulaCompiler | None = None) -> None:
        self.compiler = compiler or FormulaCompiler()

    def _execute_code(self, python_source: str, function_name: str) -> Callable[..., float]:
        """Dynamically execute python code and extract the compiled function."""
        namespace: dict[str, Any] = {}
        exec(python_source, namespace)
        fn = namespace.get(function_name)
        if not callable(fn):
            raise ValueError(f"Compiled code does not define callable function '{function_name}'")
        return cast(Callable[..., float], fn)

    def verify_with_inputs(
        self,
        codegen: CodeGenerationResult,
        input_data: Mapping[str, Sequence[float] | float],
        expected_outputs: Sequence[float] | None = None,
        tolerance: float = 1e-4,
    ) -> VerificationResult:
        """Verify compiled formula on explicit test vector inputs.

        Args:
            codegen: Code generation result containing source code.
            input_data: Dictionary mapping parameter names to float values or lists of floats.
            expected_outputs: Optional ground-truth outputs to compare against.
            tolerance: Maximum allowable absolute error.

        Returns:
            VerificationResult detailing numerical accuracy.
        """
        if not codegen.is_valid or not codegen.python_source:
            return VerificationResult(
                formula_id=codegen.formula_id,
                citekey=codegen.citekey,
                passed=False,
                num_samples=0,
                details=f"Invalid formula code: {codegen.error}",
            )

        try:
            fn = self._execute_code(codegen.python_source, codegen.function_name)
        except Exception as exc:
            return VerificationResult(
                formula_id=codegen.formula_id,
                citekey=codegen.citekey,
                passed=False,
                num_samples=0,
                details=f"Code execution error: {exc}",
            )

        # Normalize inputs to lists with flexible parameter name matching
        param_lists: dict[str, list[float]] = {}
        sample_count = 1
        for p in codegen.parameters:
            matched_key: str | None = None
            norm_p = p.replace("_", "").lower()
            for k in input_data:
                if k == p or k.replace("_", "").lower() == norm_p:
                    matched_key = k
                    break

            if matched_key is None:
                return VerificationResult(
                    formula_id=codegen.formula_id,
                    citekey=codegen.citekey,
                    passed=False,
                    num_samples=0,
                    details=f"Missing input parameter '{p}' (available: {list(input_data.keys())})",
                )
            val = input_data[matched_key]
            if isinstance(val, (int, float)):
                param_lists[p] = [float(val)]
            else:
                param_lists[p] = [float(x) for x in val]
                sample_count = max(sample_count, len(param_lists[p]))

        # Broadcast scalar parameters if needed
        for p, vals in param_lists.items():
            if len(vals) < sample_count:
                param_lists[p] = vals * sample_count

        predicted: list[float] = []
        for i in range(sample_count):
            row_args = {p: param_lists[p][i] for p in codegen.parameters}
            try:
                out = float(fn(**row_args))
                predicted.append(out)
            except Exception as e:
                return VerificationResult(
                    formula_id=codegen.formula_id,
                    citekey=codegen.citekey,
                    passed=False,
                    num_samples=len(predicted),
                    details=f"Evaluation failed at sample {i}: {e}",
                )

        if expected_outputs is not None:
            if len(expected_outputs) != sample_count:
                return VerificationResult(
                    formula_id=codegen.formula_id,
                    citekey=codegen.citekey,
                    passed=False,
                    num_samples=sample_count,
                    details=f"Length mismatch: {sample_count} predicted vs {len(expected_outputs)} expected",
                )
            abs_errors = [abs(p - e) for p, e in zip(predicted, expected_outputs, strict=True)]
            mae = sum(abs_errors) / len(abs_errors)
            max_rel = max(
                (err / (abs(e) + 1e-9) for err, e in zip(abs_errors, expected_outputs, strict=True)),
                default=0.0,
            )
            passed = mae <= tolerance
            msg = (
                f"Evaluation passed with MAE={mae:.6f} (tolerance={tolerance})"
                if passed
                else f"Evaluation exceeded tolerance: MAE={mae:.6f} > {tolerance}"
            )
            return VerificationResult(
                formula_id=codegen.formula_id,
                citekey=codegen.citekey,
                passed=passed,
                num_samples=sample_count,
                mean_absolute_error=mae,
                max_relative_error=max_rel,
                tested_columns=list(param_lists.keys()),
                details=msg,
                predicted_samples=predicted,
                actual_samples=list(expected_outputs),
            )

        # If no expected outputs, verify outputs are finite
        all_finite = all(not (x != x or abs(x) == float("inf")) for x in predicted)
        return VerificationResult(
            formula_id=codegen.formula_id,
            citekey=codegen.citekey,
            passed=all_finite,
            num_samples=sample_count,
            tested_columns=list(param_lists.keys()),
            details="All outputs evaluated to finite numeric values"
            if all_finite
            else "NaN or infinite values encountered",
            predicted_samples=predicted,
        )

    def verify_against_parquet(
        self,
        codegen: CodeGenerationResult,
        parquet_path: str | Path,
        column_mapping: dict[str, str] | None = None,
        target_column: str | None = None,
        max_rows: int = 100,
    ) -> VerificationResult:
        """Verify compiled formula on an extracted Parquet benchmark fixture.

        Args:
            codegen: Code generation result.
            parquet_path: Path to parquet table file.
            column_mapping: Optional map from formula param name -> parquet column name.
            target_column: Optional column name for expected output comparison.
            max_rows: Maximum rows to read and test.

        Returns:
            VerificationResult.
        """
        path = Path(parquet_path)
        if not path.exists():
            return VerificationResult(
                formula_id=codegen.formula_id,
                citekey=codegen.citekey,
                passed=False,
                num_samples=0,
                fixture_path=str(path),
                details=f"Parquet fixture not found: {path}",
            )

        try:
            df = pl.read_parquet(path)
            if df.height > max_rows:
                df = df.head(max_rows)
        except Exception as exc:
            return VerificationResult(
                formula_id=codegen.formula_id,
                citekey=codegen.citekey,
                passed=False,
                num_samples=0,
                fixture_path=str(path),
                details=f"Failed to read parquet: {exc}",
            )

        # Build column map
        mapping = column_mapping or {}
        input_data: dict[str, list[float]] = {}
        for param in codegen.parameters:
            col_name = mapping.get(param, param)
            norm_param = param.replace("_", "").lower()
            # Fuzzy match if exact name not in columns
            if col_name not in df.columns:
                matches = [
                    c
                    for c in df.columns
                    if param.lower() in c.lower()
                    or norm_param in c.replace("_", "").lower()
                ]
                if matches:
                    col_name = matches[0]
                else:
                    return VerificationResult(
                        formula_id=codegen.formula_id,
                        citekey=codegen.citekey,
                        passed=False,
                        num_samples=0,
                        fixture_path=str(path),
                        details=f"Could not map parameter '{param}' to any table column (available: {df.columns})",
                    )

            try:
                # Convert column to float, dropping nulls/strings
                vals = df[col_name].cast(pl.Float64, strict=False).fill_null(0.0).to_list()
                input_data[param] = [float(v) for v in vals]
            except Exception as e:
                return VerificationResult(
                    formula_id=codegen.formula_id,
                    citekey=codegen.citekey,
                    passed=False,
                    num_samples=0,
                    fixture_path=str(path),
                    details=f"Failed to cast column '{col_name}' to float: {e}",
                )

        expected: list[float] | None = None
        if target_column and target_column in df.columns:
            try:
                raw_exp = df[target_column].cast(pl.Float64, strict=False).fill_null(0.0).to_list()
                expected = [float(v) for v in raw_exp]
            except Exception:
                expected = None

        res = self.verify_with_inputs(codegen, input_data, expected_outputs=expected)
        res.fixture_path = str(path)
        return res
