"""Standalone formula library generator compiling scientific literature equations to typed Python and Polars."""

from __future__ import annotations

import ast
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

from sqlalchemy import select

from kb.codegen.compiler import FormulaCompiler
from kb.storage.database import DatabaseManager
from kb.storage.models import Document, Formula

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class GeneratedFormulaFunction:
    """Metadata and source code for an exported formula function."""

    formula_id: str
    citekey: str
    function_name: str
    expr_function_name: str
    parameters: list[str]
    scalar_code: str
    polars_code: str
    raw_latex: str
    katex_docstring: str
    paper_title: str | None = None
    paper_year: int | None = None
    paper_authors: list[str] = field(default_factory=list)


class FormulaLibraryGenerator:
    """Extracts verified equations from the corpus database and generates an executable library."""

    def __init__(self, db_manager: DatabaseManager | None = None) -> None:
        self.db_manager = db_manager or DatabaseManager()
        self.compiler = FormulaCompiler()

    def _sanitize_name(self, text: str) -> str:
        """Sanitize an arbitrary symbol or LaTeX fragment to a valid Python identifier."""
        # Strip LaTeX math tags and formatting
        cleaned = re.sub(r"\\[a-zA-Z]+", "", text)
        cleaned = re.sub(r"[{}\\^_{}()\[\]*+\-/,.:;=]", " ", cleaned)
        cleaned = re.sub(r"\s+", "_", cleaned).strip("_").lower()
        if not cleaned:
            return "metric"
        if cleaned[0].isdigit():
            cleaned = f"val_{cleaned}"
        return cleaned

    def _derive_function_names(self, formula: Formula) -> tuple[str, str]:
        """Derive readable scalar and Polars function names from formula metadata."""
        prefix = ""
        if formula.lhs:
            lhs_clean = self._sanitize_name(formula.lhs)
            if lhs_clean and lhs_clean != "metric" and len(lhs_clean) < 30:
                prefix = lhs_clean

        if not prefix:
            cite_clean = self._sanitize_name(formula.citekey.replace("arxiv_", ""))
            prefix = f"{cite_clean}"

        # Suffix with short hash for uniqueness
        short_id = formula.id.replace("-", "")[:6]
        scalar_name = f"calc_{prefix}_{short_id}"
        expr_name = f"expr_{prefix}_{short_id}"
        return scalar_name, expr_name

    def _generate_docstring(
        self,
        formula: Formula,
        parameters: list[str],
        doc: Document | None = None,
    ) -> str:
        """Generate KaTeX-compliant markdown documentation for the function."""
        latex_str = (formula.sanitized_latex or formula.raw_latex or "").strip()
        doc_title = doc.title if doc else "Corpus Document"
        year_str = f" ({doc.year})" if doc and doc.year else ""
        authors_str = ", ".join(doc.authors[:3]) if doc and doc.authors else "Scientific Literature"
        if doc and len(doc.authors) > 3:
            authors_str += " et al."

        param_lines = "\n".join(f"        {p} (float): Input parameter `{p}`." for p in parameters)

        docstring = (
            f'    r"""Compute mathematical metric extracted from {formula.citekey}.\n\n'
            f"    **Source**:\n"
            f"    - Title: {doc_title}{year_str}\n"
            f"    - Authors: {authors_str}\n"
            f"    - Citation Key: `{formula.citekey}`\n\n"
            f"    **KaTeX Formula**:\n"
            f"    $$\n"
            f"    {latex_str}\n"
            f"    $$\n\n"
            f"    Args:\n"
            f"{param_lines}\n\n"
            f"    Returns:\n"
            f"        float: Calculated metric value.\n"
            f'    """'
        )
        return docstring

    def compile_formula(
        self,
        formula: Formula,
        doc: Document | None = None,
    ) -> GeneratedFormulaFunction | None:
        """Compile a single database formula into scalar and Polars executable functions."""
        if not formula.is_valid:
            return None

        scalar_name, expr_name = self._derive_function_names(formula)
        comp_res = self.compiler.compile(
            formula_id=formula.id,
            citekey=formula.citekey,
            raw_latex=formula.sanitized_latex or formula.raw_latex,
            sympy_repr=formula.sympy_repr,
            function_name=scalar_name,
        )

        if not comp_res.is_valid or not comp_res.parameters:
            return None

        # Filter out extreme parameter count (e.g. OCR noise)
        if len(comp_res.parameters) > 12:
            return None

        # Filter out complex/imaginary expressions
        if "1j" in comp_res.python_source or "I" in comp_res.parameters or "complex" in comp_res.python_source:
            return None

        # Filter out reserved keywords or namespace collisions
        reserved = {"pl", "math", "float", "int", "str", "expr", "return", "def", "class", "import"}
        if any(p in reserved for p in comp_res.parameters):
            return None

        docstring = self._generate_docstring(formula, comp_res.parameters, doc)

        # Build clean scalar function
        sig_params = ", ".join(f"{p}: float" for p in comp_res.parameters)
        # Extract the return expression from compiler.python_source
        return_match = re.search(r"return float\((.*?)\)\s*$", comp_res.python_source, re.MULTILINE | re.DOTALL)
        if not return_match:
            return None
        core_expr = return_match.group(1).strip()

        scalar_func = (
            f"def {scalar_name}({sig_params}) -> float:\n"
            f"{docstring}\n"
            f"    return float({core_expr})\n"
        )

        # Build Polars expression function
        polars_expr = comp_res.polars_expression or core_expr
        polars_func = (
            f"def {expr_name}() -> pl.Expr:\n"
            f'    r"""Return vectorized Polars expression for `{scalar_name}`."""\n'
            f"    return ({polars_expr})\n"
        )

        return GeneratedFormulaFunction(
            formula_id=formula.id,
            citekey=formula.citekey,
            function_name=scalar_name,
            expr_function_name=expr_name,
            parameters=comp_res.parameters,
            scalar_code=scalar_func,
            polars_code=polars_func,
            raw_latex=formula.sanitized_latex or formula.raw_latex,
            katex_docstring=docstring,
            paper_title=doc.title if doc else None,
            paper_year=doc.year if doc else None,
            paper_authors=doc.authors if doc else [],
        )

    def generate_module_source(self, functions: list[GeneratedFormulaFunction]) -> str:
        """Compose complete standalone Python module with all compiled functions."""
        all_exports: list[str] = []
        for fn in functions:
            all_exports.append(f'    "{fn.function_name}",')
            all_exports.append(f'    "{fn.expr_function_name}",')

        header = (
            "# ruff: noqa\n"
            '"""Auto-generated standalone scientific formula library.\n\n'
            "Compiled directly from peer-reviewed research preprints in the Knowledge Base.\n"
            "Each formula provides typed Python scalar execution and vectorized Polars expressions.\n"
            '"""\n\n'
            "from __future__ import annotations\n\n"
            "import math\n\n"
            "import polars as pl\n\n"
            "__all__ = [\n"
            + "\n".join(all_exports)
            + "\n]\n\n"
        )

        body_blocks: list[str] = []
        for fn in functions:
            body_blocks.append(f"{fn.scalar_code}\n\n{fn.polars_code}")

        module_source = header + "\n\n".join(body_blocks) + "\n"
        return module_source

    async def export_to_file(
        self,
        output_path: Path | str,
        limit: int | None = None,
        require_equality: bool = False,
    ) -> int:
        """Read formulas from the database, compile them, and write module to disk."""
        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)

        await self.db_manager.init_db()
        async with self.db_manager.get_session() as session:
            # Query formulas and related documents
            stmt = select(Formula).where(Formula.is_valid.is_(True))
            if require_equality:
                stmt = stmt.where(Formula.is_equality.is_(True))
            if limit:
                stmt = stmt.limit(limit * 2)  # Allow buffer for compile filtering

            res = await session.execute(stmt)
            formulas = list(res.scalars().all())

            # Load document metadata map
            doc_stmt = select(Document)
            doc_res = await session.execute(doc_stmt)
            docs = {d.citekey: d for d in doc_res.scalars().all()}

        compiled_funcs: list[GeneratedFormulaFunction] = []
        seen_names: set[str] = set()

        for formula in formulas:
            doc = docs.get(formula.citekey)
            compiled = self.compile_formula(formula, doc=doc)
            if compiled is not None and compiled.function_name not in seen_names:
                seen_names.add(compiled.function_name)
                seen_names.add(compiled.expr_function_name)
                compiled_funcs.append(compiled)
                if limit and len(compiled_funcs) >= limit:
                    break

        if not compiled_funcs:
            logger.warning("No formulas were successfully compiled for export.")
            return 0

        source = self.generate_module_source(compiled_funcs)

        # Validate syntax of generated source code with ast.parse
        ast.parse(source)

        target.write_text(source, encoding="utf-8")
        logger.info("Successfully exported %d formulas to %s", len(compiled_funcs), target)
        return len(compiled_funcs)
