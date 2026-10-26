"""Formula compiler that translates SymPy/LaTeX expressions into typed Python and Polars expressions."""

from __future__ import annotations

import ast
import re

from sympy import Equality, Expr, sympify
from sympy.printing.pycode import pycode

from kb.codegen.models import CodeGenerationResult
from kb.math.ast_gen import FormulaCodeGenerator
from kb.math.extractor import FormulaExtractor


class FormulaCompiler:
    """Translates mathematical equations into verified Python functions and Polars expressions."""

    def __init__(self) -> None:
        self.extractor = FormulaExtractor()
        self.generator = FormulaCodeGenerator(default_module="math")

    def _clean_identifier(self, name: str) -> str:
        """Sanitize LaTeX symbol string to valid Python variable identifier."""
        clean = re.sub(r"[{}\\^]", "", name)
        clean = re.sub(r"[\s\-+*/(),]+", "_", clean)
        clean = clean.strip("_")
        if not clean or clean[0].isdigit():
            clean = f"var_{clean}"
        return clean

    def compile(
        self,
        formula_id: str,
        citekey: str,
        raw_latex: str,
        sympy_repr: str | None = None,
        function_name: str | None = None,
    ) -> CodeGenerationResult:
        """Compile a formula into Python source and Polars expression.

        Args:
            formula_id: Unique identifier for the formula.
            citekey: Citation key of the source document.
            raw_latex: LaTeX string of the equation.
            sympy_repr: Optional pre-parsed SymPy string representation.
            function_name: Optional override for generated function name.

        Returns:
            CodeGenerationResult containing runnable source code.
        """
        fn_name = function_name or f"calc_{self._clean_identifier(formula_id)}"

        try:
            # 1. Resolve SymPy expression
            expr_obj: Expr | Equality | None = None
            if sympy_repr:
                try:
                    expr_obj = sympify(sympy_repr)
                except Exception:
                    expr_obj = None

            if expr_obj is None:
                extracted = self.extractor.parse_latex_string(raw_latex, formula_id=formula_id)
                if not extracted.is_valid or extracted.sympy_expr is None:
                    return CodeGenerationResult(
                        formula_id=formula_id,
                        citekey=citekey,
                        function_name=fn_name,
                        python_source="",
                        raw_latex=raw_latex,
                        sympy_repr=sympy_repr,
                        is_valid=False,
                        error=extracted.error_message or "Failed to parse formula into SymPy",
                    )
                expr_obj = extracted.sympy_expr

            # 2. Extract RHS if equation
            eval_expr: Expr
            if isinstance(expr_obj, Equality):
                rhs = expr_obj.rhs
                if not isinstance(rhs, Expr):
                    raise TypeError(f"Expected RHS to be SymPy Expr, got {type(rhs)}")
                eval_expr = rhs
            elif isinstance(expr_obj, Expr):
                eval_expr = expr_obj
            else:
                eval_expr = sympify(str(expr_obj))

            # 3. Extract parameter symbols
            symbols = sorted(eval_expr.free_symbols, key=lambda s: str(s))
            param_map = {str(s): self._clean_identifier(str(s)) for s in symbols}
            param_list = [param_map[str(s)] for s in symbols]

            # 4. Generate Python source code
            raw_py_expr = str(pycode(eval_expr))
            # Replace variable names in python expression
            for original_sym, clean_sym in param_map.items():
                if original_sym != clean_sym:
                    raw_py_expr = re.sub(
                        rf"\b{re.escape(original_sym)}\b", clean_sym, raw_py_expr
                    )

            docstring = f"Calculates metric from {citekey}.\n    Equation: {raw_latex.strip()}"
            sig_params = ", ".join(f"{p}: float" for p in param_list)
            python_source = (
                f"def {fn_name}({sig_params}) -> float:\n"
                f'    """{docstring}"""\n'
                f"    import math\n"
                f"    return float({raw_py_expr})\n"
            )

            # Validate syntax of generated python code
            ast.parse(python_source)

            # 5. Generate Polars vectorized expression
            polars_expr_str = self._generate_polars_expression(raw_py_expr, param_list)

            return CodeGenerationResult(
                formula_id=formula_id,
                citekey=citekey,
                function_name=fn_name,
                python_source=python_source,
                polars_expression=polars_expr_str,
                parameters=param_list,
                raw_latex=raw_latex,
                sympy_repr=str(eval_expr),
                is_valid=True,
            )

        except Exception as exc:
            return CodeGenerationResult(
                formula_id=formula_id,
                citekey=citekey,
                function_name=fn_name,
                python_source="",
                raw_latex=raw_latex,
                sympy_repr=sympy_repr,
                is_valid=False,
                error=f"{type(exc).__name__}: {exc}",
            )

    def _generate_polars_expression(self, py_expr: str, parameters: list[str]) -> str:
        """Translate a scalar python expression into a Polars expression string."""
        polars_expr = py_expr

        # Replace parameters first with pl.col("...") (avoiding math. constants like math.e, math.pi)
        for param in sorted(parameters, key=len, reverse=True):
            polars_expr = re.sub(rf"(?<!math\.)\b{re.escape(param)}\b", f'pl.col("{param}")', polars_expr)

        # Replace math functions with polars column/expression functions
        # If the argument contains pl.col, convert to method call; otherwise leave as math.<fn>
        def _replace_math(match: re.Match[str], method: str) -> str:
            inner = match.group(1).strip()
            if "pl.col" in inner:
                return f"({inner}).{method}()"
            return f"math.{method}({inner})"

        polars_expr = re.sub(r"\bmath\.sqrt\((.*?)\)", lambda m: _replace_math(m, "sqrt"), polars_expr)
        polars_expr = re.sub(r"\bmath\.exp\((.*?)\)", lambda m: _replace_math(m, "exp"), polars_expr)
        polars_expr = re.sub(r"\bmath\.log\((.*?)\)", lambda m: _replace_math(m, "log"), polars_expr)

        return polars_expr
