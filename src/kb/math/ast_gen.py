"""Code generation and executable Python AST emission from validated SymPy expressions."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import Any

from sympy import Equality, Expr, lambdify
from sympy.core.basic import Basic
from sympy.printing.pycode import pycode

from kb.math.extractor import ExtractedFormula


class FormulaCodeGenerator:
    """Emits executable Python functions, lambdas, and source code from SymPy formulas."""

    def __init__(self, default_module: str = "math") -> None:
        """Initialize code generator.

        Args:
            default_module: Default module for lambdify ('math', 'numpy', etc.).
        """
        self.default_module = default_module

    def _resolve_expr_and_symbols(
        self, target: ExtractedFormula | Expr | Equality
    ) -> tuple[Expr, Sequence[Basic]]:
        """Extract evaluation expression and ordered argument symbols."""
        if isinstance(target, ExtractedFormula):
            if not target.is_valid or target.sympy_expr is None:
                err = target.error_message or "Unknown parsing error"
                raise ValueError(
                    f"Cannot generate code for invalid formula {target.formula_id}: {err}"
                )
            expr_obj = target.sympy_expr
        else:
            expr_obj = target

        if isinstance(expr_obj, Equality):
            rhs = expr_obj.rhs
            if not isinstance(rhs, Expr):
                raise TypeError(f"Expected RHS to be SymPy Expr, got {type(rhs)}")
            expr = rhs
        elif isinstance(expr_obj, Expr):
            expr = expr_obj
        else:
            raise TypeError(f"Unsupported expression type: {type(expr_obj)}")

        # Clean symbol names (e.g. R_{S} -> R_S for valid Python identifiers)
        symbols: list[Basic] = sorted(expr.free_symbols, key=lambda s: str(s))
        return expr, symbols

    def generate_callable(
        self,
        target: ExtractedFormula | Expr | Equality,
        modules: str | list[str] | None = None,
    ) -> Callable[..., float]:
        """Compile a SymPy expression into an executable Python callable.

        Args:
            target: ExtractedFormula or SymPy expression.
            modules: Numeric backend ('math', 'numpy', etc.).

        Returns:
            Callable executing the formula with float inputs.
        """
        expr, symbols = self._resolve_expr_and_symbols(target)
        mod = modules or self.default_module
        fn: Callable[..., float] = lambdify(symbols, expr, modules=mod)
        return fn

    def generate_python_source(
        self,
        target: ExtractedFormula | Expr | Equality,
        function_name: str = "calculate_metric",
    ) -> str:
        """Emit clean, PEP 8 type-hinted Python source code for the formula.

        Args:
            target: ExtractedFormula or SymPy expression.
            function_name: Name for the generated Python function.

        Returns:
            Python source code string.
        """
        expr, symbols = self._resolve_expr_and_symbols(target)
        python_expr = str(pycode(expr))

        # Build clean parameter list
        param_names: list[str] = []
        for s in symbols:
            clean_name = str(s).replace("{", "").replace("}", "")
            param_names.append(clean_name)
            # Replace subscripted symbol formatting in expression if needed
            if str(s) != clean_name:
                python_expr = python_expr.replace(str(s), clean_name)

        params_signature = ", ".join(f"{p}: float" for p in param_names)
        docstring_expr = str(expr)

        lines = [
            f"def {function_name}({params_signature}) -> float:",
            f'    """Evaluate formula: {docstring_expr}"""',
            f"    return float({python_expr})",
            "",
        ]
        return "\n".join(lines)

    def evaluate(
        self,
        target: ExtractedFormula | Expr | Equality,
        **kwargs: float,
    ) -> float:
        """Directly evaluate a formula with keyword arguments.

        Args:
            target: ExtractedFormula or SymPy expression.
            **kwargs: Numerical argument values keyed by symbol name.

        Returns:
            Computed numerical float value.
        """
        _expr, symbols = self._resolve_expr_and_symbols(target)
        fn = self.generate_callable(target)

        # Map kwargs to positional arguments matching symbol order
        args: list[float] = []
        for sym in symbols:
            name = str(sym)
            clean_name = name.replace("{", "").replace("}", "")
            if name in kwargs:
                args.append(float(kwargs[name]))
            elif clean_name in kwargs:
                args.append(float(kwargs[clean_name]))
            else:
                available = list(kwargs.keys())
                raise ValueError(
                    f"Missing required parameter '{clean_name}'. Available kwargs: {available}"
                )

        result: Any = fn(*args)
        return float(result)
