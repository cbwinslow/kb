"""Data structures for compiled code and empirical verification."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class CodeGenerationResult:
    """Represents compiled, type-safe Python and Polars code for an extracted formula."""

    formula_id: str
    citekey: str
    function_name: str
    python_source: str
    polars_expression: str | None = None
    parameters: list[str] = field(default_factory=list)
    raw_latex: str = ""
    sympy_repr: str | None = None
    is_valid: bool = True
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert result to dictionary representation."""
        return {
            "formula_id": self.formula_id,
            "citekey": self.citekey,
            "function_name": self.function_name,
            "python_source": self.python_source,
            "polars_expression": self.polars_expression,
            "parameters": self.parameters,
            "raw_latex": self.raw_latex,
            "sympy_repr": self.sympy_repr,
            "is_valid": self.is_valid,
            "error": self.error,
        }


@dataclass(slots=True)
class VerificationResult:
    """Represents empirical test results of a compiled formula against benchmark data."""

    formula_id: str
    citekey: str
    passed: bool
    num_samples: int
    mean_absolute_error: float | None = None
    max_relative_error: float | None = None
    tested_columns: list[str] = field(default_factory=list)
    fixture_path: str | None = None
    details: str = ""
    predicted_samples: list[float] = field(default_factory=list)
    actual_samples: list[float] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert verification result to dictionary representation."""
        return {
            "formula_id": self.formula_id,
            "citekey": self.citekey,
            "passed": self.passed,
            "num_samples": self.num_samples,
            "mean_absolute_error": self.mean_absolute_error,
            "max_relative_error": self.max_relative_error,
            "tested_columns": self.tested_columns,
            "fixture_path": self.fixture_path,
            "details": self.details,
            "predicted_samples": self.predicted_samples[:5],
            "actual_samples": self.actual_samples[:5],
        }
