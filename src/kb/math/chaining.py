"""Symbolic equation chaining, recursive substitution, and system solving."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

import sympy
from sqlalchemy import select
from sympy import Equality, Symbol, sympify
from sympy.parsing.latex import parse_latex

from kb.codegen.compiler import FormulaCompiler
from kb.math.ontology import SymbolOntology, get_symbol_ontology
from kb.math.sanitizer import EquationSanitizer
from kb.math.units import DimensionalValidator
from kb.storage.database import DatabaseManager
from kb.storage.models import Formula

logger = logging.getLogger(__name__)


@dataclass
class SubstitutionStep:
    """Records a single variable substitution within a derivation chain."""

    target_variable: str
    source_formula_id: str
    source_citekey: str
    original_expr_str: str
    substituted_expr_str: str
    dimensional_valid: bool = True
    dimensional_note: str = ""


@dataclass
class ChainedFormulaResult:
    """Outcome of recursive symbolic formula chaining into a closed-form unified equation."""

    target_formula_id: str
    target_citekey: str
    target_latex: str
    closed_form_expr: Any
    closed_form_latex: str
    trace_steps: list[SubstitutionStep] = field(default_factory=list)
    primitive_symbols: list[str] = field(default_factory=list)
    python_code: str = ""
    polars_code: str = ""
    is_dimensionally_valid: bool = True


@dataclass
class MultiHopChainResult:
    """Outcome of multi-hop cross-paper derivation chaining between two concepts."""

    from_concept: str
    to_concept: str
    target_formula_id: str
    target_citekey: str
    formula_path: list[str] = field(default_factory=list)
    citekey_path: list[str] = field(default_factory=list)
    closed_form_expr: Any = None
    closed_form_latex: str = ""
    trace_steps: list[SubstitutionStep] = field(default_factory=list)
    primitive_symbols: list[str] = field(default_factory=list)
    is_dimensionally_valid: bool = True
    python_code: str = ""
    polars_code: str = ""


class FormulaChainingEngine:
    """Engine that chains multiple formulas across papers and documents into unified closed-form systems."""

    def __init__(
        self,
        db_manager: DatabaseManager | None = None,
        ontology: SymbolOntology | None = None,
        compiler: FormulaCompiler | None = None,
        sanitizer: EquationSanitizer | None = None,
        validator: DimensionalValidator | None = None,
    ) -> None:
        self.db = db_manager or DatabaseManager()
        self.ontology = ontology or get_symbol_ontology()
        self.compiler = compiler or FormulaCompiler()
        self.sanitizer = sanitizer or EquationSanitizer()
        self.validator = validator or DimensionalValidator(self.ontology)

    def _parse_to_sympy(self, formula: Formula) -> tuple[Any, str | None, Any]:
        """Parses a stored Formula model into (lhs_expr, lhs_str, rhs_expr)."""
        # Try sympy_repr first
        if formula.sympy_repr:
            try:
                parsed = sympify(formula.sympy_repr)
                if isinstance(parsed, Equality):
                    return parsed.lhs, str(parsed.lhs), parsed.rhs
                return None, None, parsed
            except Exception:
                pass

        # Fallback to sanitized LaTeX parsing
        raw = formula.sanitized_latex or formula.raw_latex
        if not raw:
            return None, None, None

        sanitized = self.sanitizer.sanitize(raw)
        try:
            parsed = parse_latex(sanitized)
            if isinstance(parsed, Equality):
                return parsed.lhs, str(parsed.lhs), parsed.rhs
            return None, None, parsed
        except Exception as err:
            logger.debug("Failed parsing formula %s: %s", formula.id, err)
            return None, None, None

    async def find_defining_formulas(
        self,
        symbol_name: str,
        exclude_formula_ids: set[str],
    ) -> list[Formula]:
        """Discovers valid equality formulas in the database defining the given symbol on LHS."""
        async with self.db.get_session() as session:
            # 1. Exact LHS match
            stmt = (
                select(Formula)
                .where(Formula.is_valid.is_(True))
                .where(Formula.is_equality.is_(True))
                .where(Formula.lhs == symbol_name)
                .order_by(Formula.id.asc())
            )
            candidates = list((await session.execute(stmt)).scalars().all())

            # 2. Sanitized LHS match or case-insensitive LHS match
            if not candidates:
                sanitized_sym = self.sanitizer.sanitize(symbol_name)
                stmt_san = (
                    select(Formula)
                    .where(Formula.is_valid.is_(True))
                    .where(Formula.is_equality.is_(True))
                    .where((Formula.lhs == sanitized_sym) | (Formula.lhs.ilike(symbol_name)))
                    .order_by(Formula.id.asc())
                )
                candidates = list((await session.execute(stmt_san)).scalars().all())

            # 3. Raw LaTeX prefix match (e.g. wOBA = ...)
            if not candidates:
                stmt_prefix = (
                    select(Formula)
                    .where(Formula.is_valid.is_(True))
                    .where(Formula.is_equality.is_(True))
                    .where(Formula.raw_latex.ilike(f"%{symbol_name} = %"))
                    .order_by(Formula.id.asc())
                )
                candidates = list((await session.execute(stmt_prefix)).scalars().all())

            # 3. Canonical concept match via ontology if still empty
            if not candidates:
                canonical = self.ontology.resolve_canonical(symbol_name)
                if canonical:
                    # Check aliases in ontology
                    aliases = self.ontology.get_concept_aliases(canonical)
                    for alias in aliases:
                        if alias.lower() == symbol_name.lower():
                            continue
                        stmt_alias = (
                            select(Formula)
                            .where(Formula.is_valid.is_(True))
                            .where(Formula.is_equality.is_(True))
                            .where(Formula.lhs.ilike(alias))
                        )
                        alias_cands = list((await session.execute(stmt_alias)).scalars().all())
                        if alias_cands:
                            candidates.extend(alias_cands)
                            break

            return [f for f in candidates if f.id not in exclude_formula_ids]

    async def chain_formula(
        self,
        formula_id: str,
        max_depth: int = 5,
    ) -> ChainedFormulaResult:
        """Recursively substitutes component formula definitions into a target formula."""
        async with self.db.get_session() as session:
            target = (
                await session.execute(select(Formula).where(Formula.id == formula_id))
            ).scalar_one_or_none()

        if not target:
            raise ValueError(f"Formula with ID '{formula_id}' not found.")

        _lhs_expr, lhs_str, working_rhs = self._parse_to_sympy(target)
        if working_rhs is None:
            raise ValueError(
                f"Target formula '{formula_id}' could not be parsed to a SymPy expression."
            )

        trace_steps: list[SubstitutionStep] = []
        visited_formula_ids: set[str] = {target.id}
        substituted_symbols: set[str] = set()

        current_expr: Any = working_rhs

        for _depth in range(max_depth):
            free_symbols = sorted(current_expr.free_symbols, key=lambda s: str(s))
            substituted_in_pass = False

            for sym in free_symbols:
                sym_name = getattr(sym, "name", str(sym))
                if sym_name in substituted_symbols:
                    continue

                # Find candidate defining formula
                candidates = await self.find_defining_formulas(sym_name, visited_formula_ids)
                if not candidates:
                    continue

                # Select best candidate
                cand = candidates[0]
                _c_lhs, _c_lhs_str, c_rhs = self._parse_to_sympy(cand)
                if c_rhs is None:
                    continue

                orig_str = str(current_expr)
                new_expr = current_expr.subs(sym, c_rhs)
                if new_expr != current_expr:
                    dim_valid, dim_msg = self.validator.validate_substitution(sym_name, cand.lhs)
                    trace_steps.append(
                        SubstitutionStep(
                            target_variable=sym_name,
                            source_formula_id=cand.id,
                            source_citekey=cand.citekey,
                            original_expr_str=orig_str,
                            substituted_expr_str=str(new_expr),
                            dimensional_valid=dim_valid,
                            dimensional_note=dim_msg,
                        )
                    )
                    current_expr = new_expr
                    visited_formula_ids.add(cand.id)
                    substituted_symbols.add(sym_name)
                    substituted_in_pass = True

            if not substituted_in_pass:
                break

        # Simplify closed form
        try:
            simplified_expr = sympy.simplify(current_expr)
        except Exception:
            simplified_expr = current_expr

        try:
            closed_form_latex = sympy.latex(simplified_expr)
            if lhs_str:
                closed_form_latex = f"{lhs_str} = {closed_form_latex}"
        except Exception:
            closed_form_latex = str(simplified_expr)

        primitive_symbols = sorted(str(s) for s in simplified_expr.free_symbols)

        # Compile to Python & Polars
        comp_res = self.compiler.compile(
            formula_id=f"chained_{target.id}",
            citekey=target.citekey,
            raw_latex=closed_form_latex,
            sympy_repr=str(simplified_expr),
            function_name=f"calc_chained_{target.citekey}_{target.id[:8]}",
        )

        is_dim_valid = all(s.dimensional_valid for s in trace_steps) if trace_steps else True

        return ChainedFormulaResult(
            target_formula_id=target.id,
            target_citekey=target.citekey,
            target_latex=target.raw_latex,
            closed_form_expr=simplified_expr,
            closed_form_latex=closed_form_latex,
            trace_steps=trace_steps,
            primitive_symbols=primitive_symbols,
            python_code=comp_res.python_source or "",
            polars_code=comp_res.polars_expression or "",
            is_dimensionally_valid=is_dim_valid,
        )

    async def chain_between(
        self,
        from_concept: str,
        to_concept: str,
        max_depth: int = 5,
    ) -> MultiHopChainResult:
        """Discovers and constructs a multi-hop derivation chain from a source concept to a target concept.

        Args:
            from_concept: Source observable or primitive concept (e.g. 'BAT_SPEED', 'v_{bat}').
            to_concept: Target macroscopic metric or formula (e.g. 'WAR', 'RE').
            max_depth: Maximum derivation search depth.

        Returns:
            MultiHopChainResult containing formula path, unified closed form, and step diagnostics.
        """
        async with self.db.get_session() as session:
            # Check if to_concept is an exact formula ID
            target = (
                await session.execute(select(Formula).where(Formula.id == to_concept))
            ).scalar_one_or_none()

            if not target:
                candidates = await self.find_defining_formulas(
                    to_concept, exclude_formula_ids=set()
                )
                if not candidates:
                    c_enum = self.ontology.resolve_canonical(to_concept)
                    if c_enum:
                        aliases = self.ontology.get_concept_aliases(c_enum)
                        for alias in aliases:
                            candidates = await self.find_defining_formulas(
                                alias, exclude_formula_ids=set()
                            )
                            if candidates:
                                break

                if not candidates:
                    raise ValueError(
                        f"No defining formula found for target concept '{to_concept}'."
                    )
                target = candidates[0]

        chained_res = await self.chain_formula(formula_id=target.id, max_depth=max_depth)

        formula_path = [target.id] + [s.source_formula_id for s in chained_res.trace_steps]
        citekey_path = list(
            dict.fromkeys([target.citekey] + [s.source_citekey for s in chained_res.trace_steps])
        )

        return MultiHopChainResult(
            from_concept=from_concept,
            to_concept=to_concept,
            target_formula_id=target.id,
            target_citekey=target.citekey,
            formula_path=formula_path,
            citekey_path=citekey_path,
            closed_form_expr=chained_res.closed_form_expr,
            closed_form_latex=chained_res.closed_form_latex,
            trace_steps=chained_res.trace_steps,
            primitive_symbols=chained_res.primitive_symbols,
            is_dimensionally_valid=chained_res.is_dimensionally_valid,
            python_code=chained_res.python_code,
            polars_code=chained_res.polars_code,
        )

    async def solve_system(
        self,
        formula_ids: list[str],
        target_symbols: list[str],
    ) -> dict[str, str]:
        """Solves a system of simultaneous equations for specified target unknown symbols."""
        if not formula_ids:
            raise ValueError("Must provide at least one formula ID to solve system.")
        if not target_symbols:
            raise ValueError("Must provide at least one target symbol to solve for.")

        equations: list[Any] = []
        async with self.db.get_session() as session:
            for fid in formula_ids:
                f_record = (
                    await session.execute(select(Formula).where(Formula.id == fid))
                ).scalar_one_or_none()
                if not f_record:
                    raise ValueError(f"Formula ID '{fid}' not found in database.")

                lhs_expr, _lhs_str, rhs_expr = self._parse_to_sympy(f_record)
                if rhs_expr is None:
                    continue
                if lhs_expr is not None:
                    equations.append(lhs_expr - rhs_expr)
                else:
                    equations.append(rhs_expr)

        if not equations:
            raise ValueError(
                "Could not parse any valid symbolic equations from provided formula IDs."
            )

        # Collect all free symbols across all equations
        all_syms: set[Any] = set()
        for eq in equations:
            all_syms.update(eq.free_symbols)

        # Match target_symbols against equation free symbols
        sym_map: dict[str, Any] = {}
        for s in target_symbols:
            # 1. Exact name match
            exact = next((sym for sym in all_syms if getattr(sym, "name", str(sym)) == s), None)
            if exact is not None:
                sym_map[s] = exact
                continue
            # 2. Fuzzy / subscript-insensitive match
            s_clean = s.replace("{", "").replace("}", "").replace("_", "").lower()
            fuzzy = next(
                (
                    sym
                    for sym in all_syms
                    if getattr(sym, "name", str(sym))
                    .replace("{", "")
                    .replace("}", "")
                    .replace("_", "")
                    .lower()
                    == s_clean
                ),
                None,
            )
            if fuzzy is not None:
                sym_map[s] = fuzzy
            else:
                sym_map[s] = Symbol(s)

        solve_targets = list(sym_map.values())
        solution = sympy.solve(equations, solve_targets, dict=True)

        results: dict[str, str] = {}
        if not solution:
            return {"status": "no_closed_form_solution_found"}

        first_sol = solution[0]
        for name, sym in sym_map.items():
            if sym in first_sol:
                results[name] = sympy.latex(first_sol[sym])
            else:
                results[name] = "unconstrained"

        return results
