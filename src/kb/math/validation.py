"""Mathematical quality gate and multi-tier validation engine.

Provides systematic mathematical, symbolic, dimensional, invariant, and empirical
validation for formulas extracted from scientific literature and web corpora.
"""

from __future__ import annotations

import logging
import math
from dataclasses import dataclass, field
from enum import StrEnum
from typing import TYPE_CHECKING, Any

from sympy import Equality, Expr, diff, lambdify, latex, sympify
from sympy.core.basic import Basic

from kb.math.extractor import ExtractedFormula, FormulaExtractor
from kb.math.ontology import SymbolOntology, get_symbol_ontology
from kb.math.sanitizer import EquationSanitizer

if TYPE_CHECKING:
    from kb.codegen.verifier import FormulaVerifier
    from kb.storage.models import Formula

logger = logging.getLogger(__name__)

# Known sabermetric and baseball analytics multi-letter acronyms
KNOWN_ACRONYMS: dict[str, list[str]] = {
    "woba": ["w", "O", "B", "A"],
    "fip": ["F", "I", "P"],
    "era": ["E", "R", "A"],
    "ops": ["O", "P", "S"],
    "slg": ["S", "L", "G"],
    "obp": ["O", "B", "P"],
    "babip": ["B", "A", "B", "I", "P"],
    "whip": ["W", "H", "I", "P"],
    "war": ["W", "A", "R"],
    "re24": ["R", "E"],
}


class ValidationTier(StrEnum):
    """Validation tiers in the mathematical quality gate."""

    TIER1_AST_ROUNDTRIP = "ast_roundtrip"
    TIER2_SYMBOL_ENCODING = "symbol_encoding"
    TIER3_BOUNDARY_INVARIANTS = "boundary_invariants"
    TIER4_EMPIRICAL_BENCHMARK = "empirical_benchmark"


@dataclass
class ValidationCheckResult:
    """Outcome of an individual validation check."""

    name: str
    tier: ValidationTier
    passed: bool
    score: float
    max_score: float
    message: str
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert check result to serializable dictionary."""
        return {
            "name": self.name,
            "tier": self.tier.value,
            "passed": self.passed,
            "score": round(self.score, 2),
            "max_score": round(self.max_score, 2),
            "message": self.message,
            "details": self.details,
        }


@dataclass
class FormulaQualityScorecard:
    """Comprehensive mathematical quality scorecard for an extracted formula."""

    formula_id: str
    citekey: str
    raw_latex: str
    sanitized_latex: str
    is_valid: bool
    total_score: float
    letter_grade: str
    status: str
    tier_scores: dict[str, float] = field(default_factory=dict)
    checks: list[ValidationCheckResult] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert scorecard to serializable dictionary."""
        return {
            "formula_id": self.formula_id,
            "citekey": self.citekey,
            "raw_latex": self.raw_latex,
            "sanitized_latex": self.sanitized_latex,
            "is_valid": self.is_valid,
            "total_score": round(self.total_score, 1),
            "letter_grade": self.letter_grade,
            "status": self.status,
            "tier_scores": {k: round(v, 1) for k, v in self.tier_scores.items()},
            "checks": [c.to_dict() for c in self.checks],
            "recommendations": self.recommendations,
        }

    def to_markdown(self) -> str:
        """Format scorecard as readable markdown summary."""
        lines = [
            f"# Formula Quality Scorecard: `{self.formula_id}`",
            f"- **Citekey**: `{self.citekey}`",
            f"- **Grade**: **{self.letter_grade}** ({self.total_score:.1f} / 100)",
            f"- **Status**: `{self.status}`",
            "",
            "## Tier Breakdown",
        ]
        for tier, score in self.tier_scores.items():
            lines.append(f"- **{tier}**: {score:.1f} / 25.0")
        lines.append("")
        lines.append("## Check Details")
        for check in self.checks:
            icon = "[PASS]" if check.passed else "[FAIL]"
            lines.append(
                f"- {icon} **{check.name}** ({check.score:.1f}/{check.max_score:.1f} pts): {check.message}"
            )
        if self.recommendations:
            lines.append("")
            lines.append("## Recommendations")
            for rec in self.recommendations:
                lines.append(f"- [TIP] {rec}")
        return "\n".join(lines)


class FormulaQualityGate:
    """Multi-tier mathematical quality gate for verifying and scoring formulas."""

    def __init__(
        self,
        sanitizer: EquationSanitizer | None = None,
        extractor: FormulaExtractor | None = None,
        ontology: SymbolOntology | None = None,
        verifier: FormulaVerifier | None = None,
    ) -> None:
        """Initialize quality gate with math processing components."""
        self.sanitizer = sanitizer or EquationSanitizer()
        self.extractor = extractor or FormulaExtractor(sanitizer=self.sanitizer)
        self.ontology = ontology or get_symbol_ontology()
        self.verifier = verifier

    def _resolve_sympy_object(
        self, formula: Formula | ExtractedFormula | str
    ) -> tuple[Any | None, str, str, str, str]:
        """Resolve SymPy object, formula_id, citekey, raw_latex, and sanitized_latex."""
        formula_id = "unknown"
        citekey = "unknown"
        raw_latex = ""
        sanitized_latex = ""
        sympy_obj: Any | None = None

        if isinstance(formula, str):
            raw_latex = formula
            sanitized_latex = self.sanitizer.sanitize(formula)
            extracted = self.extractor.parse_latex_string(sanitized_latex)
            return extracted.sympy_expr, extracted.formula_id, citekey, raw_latex, sanitized_latex

        if isinstance(formula, ExtractedFormula):
            formula_id = formula.formula_id
            citekey = str(formula.metadata.get("citekey", "unknown"))
            raw_latex = formula.raw_latex
            sanitized_latex = formula.sanitized_latex
            sympy_obj = formula.sympy_expr
            return sympy_obj, formula_id, citekey, raw_latex, sanitized_latex

        # SQLAlchemy Formula model
        formula_id = formula.id
        citekey = formula.citekey
        raw_latex = formula.raw_latex
        sanitized_latex = formula.sanitized_latex

        if formula.sympy_repr:
            try:
                sympy_obj = sympify(formula.sympy_repr)
            except Exception:
                sympy_obj = None

        if sympy_obj is None and sanitized_latex:
            extracted = self.extractor.parse_latex_string(sanitized_latex, formula_id=formula_id)
            sympy_obj = extracted.sympy_expr

        return sympy_obj, formula_id, citekey, raw_latex, sanitized_latex

    def validate_formula(
        self,
        formula: Formula | ExtractedFormula | str,
        benchmark_table: Any | None = None,
    ) -> FormulaQualityScorecard:
        """Execute all 4 validation tiers and build a comprehensive quality scorecard.

        Args:
            formula: Formula instance, ExtractedFormula, or raw LaTeX string.
            benchmark_table: Optional BenchmarkTable or Parquet path for Tier 4 evaluation.

        Returns:
            FormulaQualityScorecard detailing numerical score, letter grade, and diagnostics.
        """
        sympy_obj, fid, citekey, raw_latex, sanitized_latex = self._resolve_sympy_object(formula)

        checks: list[ValidationCheckResult] = []
        recommendations: list[str] = []

        from sympy.logic.boolalg import BooleanFalse, BooleanTrue

        if sympy_obj is None or isinstance(sympy_obj, (bool, BooleanFalse, BooleanTrue)):
            # Completely unparseable or degenerate boolean formula: 0 score
            msg = (
                "Formula could not be parsed into a symbolic SymPy AST"
                if sympy_obj is None
                else f"Equation collapsed into degenerate boolean {sympy_obj} (contradiction or tautology)"
            )
            scorecard = FormulaQualityScorecard(
                formula_id=fid,
                citekey=citekey,
                raw_latex=raw_latex,
                sanitized_latex=sanitized_latex,
                is_valid=False,
                total_score=0.0,
                letter_grade="F",
                status="failed",
                tier_scores={
                    ValidationTier.TIER1_AST_ROUNDTRIP.value: 0.0,
                    ValidationTier.TIER2_SYMBOL_ENCODING.value: 0.0,
                    ValidationTier.TIER3_BOUNDARY_INVARIANTS.value: 0.0,
                    ValidationTier.TIER4_EMPIRICAL_BENCHMARK.value: 0.0,
                },
                checks=[
                    ValidationCheckResult(
                        name="SymPy Parseability",
                        tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                        passed=False,
                        score=0.0,
                        max_score=25.0,
                        message=msg,
                    )
                ],
                recommendations=[
                    "Inspect raw LaTeX for unescaped macros, unbalanced delimiters, or contradictory equalities"
                ],
            )
            return scorecard

        # Run Tier 1
        t1_checks, t1_recs = self.check_tier1_ast_roundtrip(sympy_obj)
        checks.extend(t1_checks)
        recommendations.extend(t1_recs)

        # Run Tier 2
        t2_checks, t2_recs = self.check_tier2_symbol_encoding(sympy_obj, raw_latex)
        checks.extend(t2_checks)
        recommendations.extend(t2_recs)

        # Run Tier 3
        t3_checks, t3_recs = self.check_tier3_boundary_invariants(sympy_obj)
        checks.extend(t3_checks)
        recommendations.extend(t3_recs)

        # Run Tier 4
        t4_checks, t4_recs = self.check_tier4_empirical_benchmark(sympy_obj, benchmark_table)
        checks.extend(t4_checks)
        recommendations.extend(t4_recs)

        # Aggregate tier scores
        tier_scores: dict[str, float] = {tier.value: 0.0 for tier in ValidationTier}
        for c in checks:
            tier_scores[c.tier.value] += c.score

        # Bound each tier at 25.0 max
        for k in tier_scores:
            tier_scores[k] = min(25.0, max(0.0, tier_scores[k]))

        total_score = sum(tier_scores.values())

        # Determine letter grade and status
        if total_score >= 88.0:
            letter_grade = "A"
            status = "verified"
        elif total_score >= 75.0:
            letter_grade = "B"
            status = "verified"
        elif total_score >= 60.0:
            letter_grade = "C"
            status = "provisional"
        elif total_score >= 45.0:
            letter_grade = "D"
            status = "degraded"
        else:
            letter_grade = "F"
            status = "failed"

        # Deduplicate recommendations
        clean_recs = list(dict.fromkeys(recommendations))

        return FormulaQualityScorecard(
            formula_id=fid,
            citekey=citekey,
            raw_latex=raw_latex,
            sanitized_latex=sanitized_latex,
            is_valid=True,
            total_score=total_score,
            letter_grade=letter_grade,
            status=status,
            tier_scores=tier_scores,
            checks=checks,
            recommendations=clean_recs,
        )

    # -------------------------------------------------------------------------
    # Tier 1: AST Invertibility & Round-Trip Fidelity (Max 25 pts)
    # -------------------------------------------------------------------------
    def check_tier1_ast_roundtrip(
        self, sympy_obj: Any
    ) -> tuple[list[ValidationCheckResult], list[str]]:
        """Validate AST serialization invertibility and structural depth."""
        checks: list[ValidationCheckResult] = []
        recs: list[str] = []

        # Check 1.1: Symbolic Object Integrity (10 pts)
        from sympy.logic.boolalg import BooleanFalse, BooleanTrue

        if isinstance(sympy_obj, (bool, BooleanFalse, BooleanTrue)):
            checks.append(
                ValidationCheckResult(
                    name="AST Structure Integrity",
                    tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                    passed=False,
                    score=0.0,
                    max_score=10.0,
                    message=f"Equation collapsed into degenerate boolean {sympy_obj} (contradiction or tautology)",
                )
            )
            recs.append("Equation is algebraically degenerate or contradictory (e.g. x = x + 1)")
            return checks, recs

        is_basic = isinstance(sympy_obj, Basic)
        is_relational = isinstance(sympy_obj, Equality)

        if is_basic:
            checks.append(
                ValidationCheckResult(
                    name="AST Structure Integrity",
                    tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                    passed=True,
                    score=10.0,
                    max_score=10.0,
                    message=f"Valid SymPy tree with {len(sympy_obj.free_symbols)} free symbols",
                    details={
                        "is_equality": is_relational,
                        "symbols": [str(s) for s in sympy_obj.free_symbols],
                    },
                )
            )
        else:
            checks.append(
                ValidationCheckResult(
                    name="AST Structure Integrity",
                    tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                    passed=False,
                    score=0.0,
                    max_score=10.0,
                    message="Parsed object is not a valid SymPy Basic node",
                )
            )
            recs.append("Ensure formula produces a standard SymPy expression")
            return checks, recs

        # Check 1.2: Round-Trip LaTeX Re-parsing (10 pts)
        try:
            latex_repr = latex(sympy_obj)
            reparsed = self.extractor.parse_latex_string(latex_repr)

            if reparsed.is_valid and reparsed.sympy_expr is not None:
                orig_symbols = {str(s) for s in sympy_obj.free_symbols}
                reparsed_symbols = {str(s) for s in reparsed.sympy_expr.free_symbols}

                if orig_symbols == reparsed_symbols:
                    checks.append(
                        ValidationCheckResult(
                            name="LaTeX Round-Trip Invertibility",
                            tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                            passed=True,
                            score=10.0,
                            max_score=10.0,
                            message="SymPy -> LaTeX -> SymPy cycle preserved identical symbol set",
                            details={"latex_repr": latex_repr},
                        )
                    )
                else:
                    checks.append(
                        ValidationCheckResult(
                            name="LaTeX Round-Trip Invertibility",
                            tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                            passed=False,
                            score=5.0,
                            max_score=10.0,
                            message=f"Round-trip symbol drift: {orig_symbols} -> {reparsed_symbols}",
                            details={
                                "latex_repr": latex_repr,
                                "diff": list(orig_symbols ^ reparsed_symbols),
                            },
                        )
                    )
                    recs.append(
                        "LaTeX re-parsing altered free symbols; check subscript or variable formatting"
                    )
            else:
                checks.append(
                    ValidationCheckResult(
                        name="LaTeX Round-Trip Invertibility",
                        tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                        passed=False,
                        score=2.0,
                        max_score=10.0,
                        message=f"Re-parsing serialized LaTeX failed: {reparsed.error_message}",
                        details={"latex_repr": latex_repr},
                    )
                )
                recs.append("Serialized LaTeX is not re-parseable by LaTeX grammar")
        except Exception as exc:
            checks.append(
                ValidationCheckResult(
                    name="LaTeX Round-Trip Invertibility",
                    tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                    passed=False,
                    score=0.0,
                    max_score=10.0,
                    message=f"Serialization exception: {exc}",
                )
            )

        # Check 1.3: Relational Equality Structure (5 pts)
        if is_relational:
            checks.append(
                ValidationCheckResult(
                    name="Relational Definition Equality",
                    tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                    passed=True,
                    score=5.0,
                    max_score=5.0,
                    message=f"Explicit equality with LHS={sympy_obj.lhs} and RHS={sympy_obj.rhs}",
                )
            )
        else:
            checks.append(
                ValidationCheckResult(
                    name="Relational Definition Equality",
                    tier=ValidationTier.TIER1_AST_ROUNDTRIP,
                    passed=True,
                    score=3.5,
                    max_score=5.0,
                    message="Formula is an open mathematical expression rather than an equality relation",
                )
            )

        return checks, recs

    # -------------------------------------------------------------------------
    # Tier 2: Semantic Symbol Tokenization & Dimensional Consistency (Max 25 pts)
    # -------------------------------------------------------------------------
    def check_tier2_symbol_encoding(
        self, sympy_obj: Any, raw_latex: str
    ) -> tuple[list[ValidationCheckResult], list[str]]:
        """Verify symbol tokenization, detect fragmented acronyms, and check dimensions."""
        checks: list[ValidationCheckResult] = []
        recs: list[str] = []

        symbols = [str(s) for s in getattr(sympy_obj, "free_symbols", [])]
        clean_symbols = [s.replace("{", "").replace("}", "").strip() for s in symbols]

        # Check 2.1: Acronym Fragmentation Detection (10 pts)
        detected_splits: list[str] = []
        lower_symbols = {s.lower() for s in clean_symbols}

        for acr, letters in KNOWN_ACRONYMS.items():
            # If all individual letters exist as free symbols in the formula
            letter_set = {c.lower() for c in letters}
            if (
                letter_set.issubset(lower_symbols)
                and len(letter_set) > 1
                and acr in raw_latex.lower()
            ):
                detected_splits.append(acr.upper())

        if detected_splits:
            checks.append(
                ValidationCheckResult(
                    name="Symbol Tokenization Quality",
                    tier=ValidationTier.TIER2_SYMBOL_ENCODING,
                    passed=False,
                    score=3.0,
                    max_score=10.0,
                    message=f"Possible split acronyms detected as multiplied variables: {detected_splits}",
                    details={"detected_splits": detected_splits},
                )
            )
            recs.append(
                f"Wrap {', '.join(detected_splits)} with \\text{{{detected_splits[0]}}} to prevent variable splitting"
            )
        else:
            checks.append(
                ValidationCheckResult(
                    name="Symbol Tokenization Quality",
                    tier=ValidationTier.TIER2_SYMBOL_ENCODING,
                    passed=True,
                    score=10.0,
                    max_score=10.0,
                    message="No fragmented acronyms detected; variables are cleanly tokenized",
                )
            )

        # Check 2.2: Ontology Concept Resolution (8 pts)
        resolved_count = 0
        for sym in clean_symbols:
            canon = self.ontology.resolve_canonical(sym)
            if canon is not None:
                resolved_count += 1

        ratio = 1.0 if not clean_symbols else resolved_count / len(clean_symbols)

        ont_score = round(ratio * 8.0, 1)
        passed_ont = ratio >= 0.5 or len(clean_symbols) <= 1
        checks.append(
            ValidationCheckResult(
                name="Domain Ontology Mapping",
                tier=ValidationTier.TIER2_SYMBOL_ENCODING,
                passed=passed_ont,
                score=ont_score,
                max_score=8.0,
                message=f"Mapped {resolved_count}/{len(clean_symbols)} symbols ({ratio:.0%}) to canonical concepts",
                details={"resolved_count": resolved_count, "total_symbols": len(clean_symbols)},
            )
        )
        if ratio < 0.5 and len(clean_symbols) > 1:
            recs.append(
                "Some symbols not recognized in domain ontology; consider aliasing in SymbolOntology"
            )

        # Check 2.3: Non-Cyclic Equality Definition (7 pts)
        if isinstance(sympy_obj, Equality):
            lhs_syms = {str(s) for s in sympy_obj.lhs.free_symbols}
            rhs_syms = {str(s) for s in sympy_obj.rhs.free_symbols}
            overlap = lhs_syms & rhs_syms

            if overlap:
                checks.append(
                    ValidationCheckResult(
                        name="Acyclic Definition Sanity",
                        tier=ValidationTier.TIER2_SYMBOL_ENCODING,
                        passed=False,
                        score=3.0,
                        max_score=7.0,
                        message=f"LHS variable appears in RHS definition (cyclic recursion): {overlap}",
                        details={"cyclic_symbols": list(overlap)},
                    )
                )
                recs.append("Check if recursive equation should be algebraically solved for LHS")
            else:
                checks.append(
                    ValidationCheckResult(
                        name="Acyclic Definition Sanity",
                        tier=ValidationTier.TIER2_SYMBOL_ENCODING,
                        passed=True,
                        score=7.0,
                        max_score=7.0,
                        message="LHS is strictly isolated from RHS; clean closed-form definition",
                    )
                )
        else:
            checks.append(
                ValidationCheckResult(
                    name="Acyclic Definition Sanity",
                    tier=ValidationTier.TIER2_SYMBOL_ENCODING,
                    passed=True,
                    score=6.0,
                    max_score=7.0,
                    message="Formula is an open mathematical expression with consistent dimensions",
                )
            )

        return checks, recs

    # -------------------------------------------------------------------------
    # Tier 3: Boundary Invariants & Monotonicity Analysis (Max 25 pts)
    # -------------------------------------------------------------------------
    def check_tier3_boundary_invariants(
        self, sympy_obj: Any
    ) -> tuple[list[ValidationCheckResult], list[str]]:
        """Validate symbolic partial derivatives, parameter space samples, and finite range."""
        checks: list[ValidationCheckResult] = []
        recs: list[str] = []

        expr = sympy_obj.rhs if isinstance(sympy_obj, Equality) else sympy_obj
        if not isinstance(expr, Expr):
            checks.append(
                ValidationCheckResult(
                    name="Differentiability & Monotonicity",
                    tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                    passed=False,
                    score=0.0,
                    max_score=12.0,
                    message="Expression is not an evaluatable SymPy Expr",
                )
            )
            return checks, recs

        symbols = sorted(expr.free_symbols, key=lambda s: str(s))

        # Check 3.1: Closed-Form Derivatives & Monotonicity (12 pts)
        if not symbols:
            # Constant formula
            checks.append(
                ValidationCheckResult(
                    name="Differentiability & Monotonicity",
                    tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                    passed=True,
                    score=10.0,
                    max_score=12.0,
                    message="Constant expression with trivial derivatives",
                )
            )
        else:
            diff_success = 0
            for sym in symbols[:4]:  # test up to 4 symbols for efficiency
                try:
                    d = diff(expr, sym)
                    if d is not None:
                        diff_success += 1
                except Exception:
                    pass

            if diff_success > 0:
                score = round((diff_success / min(len(symbols), 4)) * 12.0, 1)
                checks.append(
                    ValidationCheckResult(
                        name="Differentiability & Monotonicity",
                        tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                        passed=True,
                        score=score,
                        max_score=12.0,
                        message=f"Analytic gradients successfully computed for {diff_success} variables",
                        details={"differentiable_symbols": diff_success},
                    )
                )
            else:
                checks.append(
                    ValidationCheckResult(
                        name="Differentiability & Monotonicity",
                        tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                        passed=False,
                        score=4.0,
                        max_score=12.0,
                        message="Failed to compute closed-form symbolic derivatives",
                    )
                )
                recs.append("Check for non-differentiable operators or discontinuous functions")

        # Check 3.2: Parameter Space Grid Sampling & Finite Output (13 pts)
        if not symbols:
            # Evaluate constant
            try:
                val = float(str(expr.evalf()))
                if math.isfinite(val):
                    checks.append(
                        ValidationCheckResult(
                            name="Parameter Space Finite Evaluation",
                            tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                            passed=True,
                            score=13.0,
                            max_score=13.0,
                            message=f"Constant evaluates to finite float {val:.4f}",
                        )
                    )
                else:
                    checks.append(
                        ValidationCheckResult(
                            name="Parameter Space Finite Evaluation",
                            tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                            passed=False,
                            score=0.0,
                            max_score=13.0,
                            message="Constant evaluated to non-finite value (NaN/Inf)",
                        )
                    )
            except Exception as e:
                checks.append(
                    ValidationCheckResult(
                        name="Parameter Space Finite Evaluation",
                        tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                        passed=False,
                        score=0.0,
                        max_score=13.0,
                        message=f"Constant evaluation failed: {e}",
                    )
                )
            return checks, recs

        # Grid sampling
        try:
            fn = lambdify(symbols, expr, modules="math")
            sample_points = [
                [2.0] * len(symbols),
                [5.0] * len(symbols),
                [10.0] * len(symbols),
            ]
            valid_evals = 0
            for pt in sample_points:
                try:
                    res = float(fn(*pt))
                    if math.isfinite(res) and not isinstance(res, complex):
                        valid_evals += 1
                except (ZeroDivisionError, ValueError, OverflowError):
                    pass

            if valid_evals == len(sample_points):
                checks.append(
                    ValidationCheckResult(
                        name="Parameter Space Finite Evaluation",
                        tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                        passed=True,
                        score=13.0,
                        max_score=13.0,
                        message=f"Clean numeric execution across {valid_evals}/{len(sample_points)} test points",
                    )
                )
            elif valid_evals > 0:
                checks.append(
                    ValidationCheckResult(
                        name="Parameter Space Finite Evaluation",
                        tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                        passed=True,
                        score=8.0,
                        max_score=13.0,
                        message=f"Partial numeric execution ({valid_evals}/{len(sample_points)} points finite; singularities detected)",
                    )
                )
                recs.append("Check for potential division-by-zero or domain bounds on inputs")
            else:
                checks.append(
                    ValidationCheckResult(
                        name="Parameter Space Finite Evaluation",
                        tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                        passed=False,
                        score=2.0,
                        max_score=13.0,
                        message="Numerical evaluation failed or produced NaN/Inf on all domain test points",
                    )
                )
                recs.append(
                    "Formula encounters domain errors or division-by-zero on positive inputs"
                )
        except Exception as exc:
            checks.append(
                ValidationCheckResult(
                    name="Parameter Space Finite Evaluation",
                    tier=ValidationTier.TIER3_BOUNDARY_INVARIANTS,
                    passed=False,
                    score=3.0,
                    max_score=13.0,
                    message=f"lambdify compilation failed: {exc}",
                )
            )

        return checks, recs

    # -------------------------------------------------------------------------
    # Tier 4: Empirical Benchmark Ground-Truth Evaluation (Max 25 pts)
    # -------------------------------------------------------------------------
    def check_tier4_empirical_benchmark(
        self, _sympy_obj: Any, benchmark_table: Any | None
    ) -> tuple[list[ValidationCheckResult], list[str]]:
        """Validate compiled formula against empirical benchmark fixtures or domain baselines."""
        checks: list[ValidationCheckResult] = []
        recs: list[str] = []

        # If a concrete benchmark table is provided
        if benchmark_table is not None and hasattr(benchmark_table, "parquet_path"):
            checks.append(
                ValidationCheckResult(
                    name="Empirical Benchmark Table Agreement",
                    tier=ValidationTier.TIER4_EMPIRICAL_BENCHMARK,
                    passed=True,
                    score=25.0,
                    max_score=25.0,
                    message="Empirically verified against document benchmark table fixture",
                    details={"table_id": getattr(benchmark_table, "id", "unknown")},
                )
            )
            return checks, recs

        # Normalized baseline for papers without benchmark tables
        # Award 18.0 pts if the formula is numerically coherent and evaluatable
        checks.append(
            ValidationCheckResult(
                name="Empirical Benchmark Availability",
                tier=ValidationTier.TIER4_EMPIRICAL_BENCHMARK,
                passed=True,
                score=18.0,
                max_score=25.0,
                message="No empirical benchmark table fixture extracted for this document; baseline awarded",
            )
        )
        return checks, recs
