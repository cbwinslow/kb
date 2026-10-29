"""LaTeX formula extractor and SymPy symbolic parser."""

from __future__ import annotations

import hashlib
import logging
import re
import warnings
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict, Field
from sympy.core.relational import Equality
from sympy.parsing.latex import parse_latex

if TYPE_CHECKING:
    from kb.ingest.chunker import EnrichedChunk

from kb.math.sanitizer import EquationSanitizer

logger = logging.getLogger(__name__)

# Patterns to locate display and inline equations in markdown text
MATH_DISPLAY_RE = re.compile(r"\$\$([\s\S]*?)\$\$")
MATH_INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)([^\n$]+?)(?<!\$)\$(?!\$)")
MATH_ENV_RE = re.compile(
    r"(\\begin\{(?:equation|align|aligned|gather|displaymath)\*?\}"
    r"[\s\S]*?"
    r"\\end\{(?:equation|align|aligned|gather|displaymath)\*?\})"
)


class ExtractedFormula(BaseModel):
    """Container for validated mathematical expressions and their SymPy representations."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    formula_id: str = Field(description="Deterministic hash of the formula")
    raw_latex: str = Field(description="Original uncleaned LaTeX expression")
    sanitized_latex: str = Field(description="Sanitized LaTeX suitable for SymPy")
    sympy_expr: Any | None = Field(
        default=None, description="Underlying SymPy Expression or Equality object"
    )
    symbols: list[str] = Field(default_factory=list, description="Free symbols in the expression")
    is_valid: bool = Field(default=False, description="Whether SymPy parsed successfully")
    is_equality: bool = Field(default=False, description="Whether formula is Equality (LHS=RHS)")
    lhs: str | None = Field(default=None, description="Left-hand side string if equality")
    rhs: str | None = Field(default=None, description="Right-hand side string if equality")
    error_message: str | None = Field(default=None, description="Parser error message if invalid")
    chunk_id: str | None = Field(default=None, description="Associated chunk ID")
    metadata: dict[str, Any] = Field(default_factory=dict, description="Metadata")


class FormulaExtractor:
    """Extracts, sanitizes, and parses LaTeX formulas into SymPy symbolic expressions."""

    def __init__(self, sanitizer: EquationSanitizer | None = None) -> None:
        """Initialize FormulaExtractor with equation sanitizer.

        Args:
            sanitizer: EquationSanitizer instance. If None, default is used.
        """
        self.sanitizer = sanitizer or EquationSanitizer()

    def parse_latex_string(
        self,
        raw_latex: str,
        formula_id: str = "",
        chunk_id: str | None = None,
    ) -> ExtractedFormula:
        """Sanitize and parse a raw LaTeX equation into SymPy.

        Args:
            raw_latex: Raw LaTeX string.
            formula_id: Optional ID; auto-generated if empty.
            chunk_id: Optional parent chunk ID.

        Returns:
            ExtractedFormula with symbolic validation status.
        """
        clean_raw = raw_latex.strip()
        if not formula_id:
            raw_hash = hashlib.sha256(clean_raw.encode("utf-8")).hexdigest()[:12]
            formula_id = f"formula_{raw_hash}"

        sanitized = self.sanitizer.sanitize(clean_raw)

        if not sanitized:
            return ExtractedFormula(
                formula_id=formula_id,
                raw_latex=clean_raw,
                sanitized_latex="",
                is_valid=False,
                error_message="Empty formula after sanitization",
                chunk_id=chunk_id,
            )

        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=SyntaxWarning)
                parsed = parse_latex(sanitized)
            if parsed is None:
                raise ValueError("SymPy parse_latex returned None")

            is_eq = isinstance(parsed, Equality)
            free_symbols = sorted(str(s) for s in parsed.free_symbols)

            lhs_str = str(parsed.lhs) if is_eq else None
            rhs_str = str(parsed.rhs) if is_eq else str(parsed)

            return ExtractedFormula(
                formula_id=formula_id,
                raw_latex=clean_raw,
                sanitized_latex=sanitized,
                sympy_expr=parsed,
                symbols=free_symbols,
                is_valid=True,
                is_equality=is_eq,
                lhs=lhs_str,
                rhs=rhs_str,
                chunk_id=chunk_id,
            )
        except Exception as exc:  # noqa: BLE001
            logger.debug("Failed to parse formula '%s': %s", sanitized, exc)
            return ExtractedFormula(
                formula_id=formula_id,
                raw_latex=clean_raw,
                sanitized_latex=sanitized,
                sympy_expr=None,
                symbols=[],
                is_valid=False,
                error_message=str(exc),
                chunk_id=chunk_id,
            )

    def extract_from_text(
        self,
        text: str,
        chunk_id: str | None = None,
    ) -> list[ExtractedFormula]:
        """Scan a block of markdown text for LaTeX equations and parse each.

        Args:
            text: Markdown text containing LaTeX formulas.
            chunk_id: Optional parent chunk ID.

        Returns:
            List of ExtractedFormula objects.
        """
        formulas: list[ExtractedFormula] = []
        found_raws: set[str] = set()

        # 1. Environment equations (\begin{equation}...\end{equation})
        for match in MATH_ENV_RE.finditer(text):
            raw = match.group(0).strip()
            if raw and raw not in found_raws:
                found_raws.add(raw)
                formulas.append(self.parse_latex_string(raw, chunk_id=chunk_id))

        # 2. Display equations ($$...$$)
        for match in MATH_DISPLAY_RE.finditer(text):
            raw = match.group(0).strip()
            if raw and raw not in found_raws:
                found_raws.add(raw)
                formulas.append(self.parse_latex_string(raw, chunk_id=chunk_id))

        # 3. Inline equations ($...$)
        for match in MATH_INLINE_RE.finditer(text):
            raw = match.group(0).strip()
            # Ignore trivial single punctuation/letters or already found
            if raw and len(raw) > 2 and raw not in found_raws:
                found_raws.add(raw)
                formulas.append(self.parse_latex_string(raw, chunk_id=chunk_id))

        return formulas

    def extract_from_chunk(self, chunk: EnrichedChunk) -> list[ExtractedFormula]:
        """Extract and parse all equations from an EnrichedChunk.

        Args:
            chunk: EnrichedChunk instance.

        Returns:
            List of ExtractedFormula objects linked to chunk.chunk_id.
        """
        formulas: list[ExtractedFormula] = []
        seen_raws: set[str] = set()

        # Use pre-extracted math expressions on the chunk if available
        if chunk.math_expressions:
            for raw in chunk.math_expressions:
                if raw and raw not in seen_raws:
                    seen_raws.add(raw)
                    formulas.append(self.parse_latex_string(raw, chunk_id=chunk.chunk_id))

        # Also scan raw text for any missed formulas
        text_formulas = self.extract_from_text(chunk.raw_text, chunk_id=chunk.chunk_id)
        for tf in text_formulas:
            if tf.raw_latex not in seen_raws:
                seen_raws.add(tf.raw_latex)
                formulas.append(tf)

        return formulas


# Standard LaTeX Greek alphabet macros
GREEK_SYMBOLS: set[str] = {
    r"\alpha",
    r"\beta",
    r"\gamma",
    r"\delta",
    r"\epsilon",
    r"\varepsilon",
    r"\zeta",
    r"\eta",
    r"\theta",
    r"\vartheta",
    r"\iota",
    r"\kappa",
    r"\lambda",
    r"\mu",
    r"\nu",
    r"\xi",
    r"\pi",
    r"\rho",
    r"\sigma",
    r"\tau",
    r"\upsilon",
    r"\phi",
    r"\varphi",
    r"\chi",
    r"\psi",
    r"\omega",
    r"\Gamma",
    r"\Delta",
    r"\Theta",
    r"\Lambda",
    r"\Xi",
    r"\Pi",
    r"\Sigma",
    r"\Upsilon",
    r"\Phi",
    r"\Psi",
    r"\Omega",
}

# Common domain variables in sports analytics and statistical modeling
COMMON_DOMAIN_VARIABLES: set[str] = {
    "RS",
    "RA",
    "HR",
    "BB",
    "SO",
    "IP",
    "AB",
    "TB",
    "OBP",
    "SLG",
    "OPS",
    "FIP",
    "wOBA",
    "wRC",
    "WAR",
    "BABIP",
    "tERA",
    "SIERA",
    "UZR",
    "DRS",
}

EQUATION_REF_RE = re.compile(
    r"\b(?:Equation|Eq\.?|Eqs\.?|formula)\s*\(?([0-9]+(?:\.[0-9]+)*[a-z]?)\)?",
    re.IGNORECASE,
)

VARIABLE_DEF_RE = re.compile(
    r"(?:\b(?:where|in which|let|with)|,\s*and|;\s*and|,)\s+"
    r"(\$?[a-zA-Z_\\{}^]+\$?)\s+(?:denotes|represents|is the|is a|being)\s+([^,\n\.]+)",
    re.IGNORECASE,
)


def extract_math_symbols(text: str) -> list[str]:
    """Extract distinct mathematical symbols, Greek letters, and domain parameters from text.

    Args:
        text: Text containing mathematical equations, variables, or definitions.

    Returns:
        Sorted unique list of symbol strings (e.g. ['RS', 'RA', 'gamma', 'mu', 'sigma^2']).
    """
    symbols: set[str] = set()

    # 1. Greek letters
    for greek in GREEK_SYMBOLS:
        if greek in text:
            symbols.add(greek.lstrip("\\"))

    # 2. Domain variables
    for var in COMMON_DOMAIN_VARIABLES:
        if re.search(rf"\b{var}\b", text):
            symbols.add(var)

    # 3. Subscripted parameters like \mu_{i}, \sigma^2, Y_{ij}, \beta_1, X_i
    subscript_matches = re.finditer(
        r"(?:\$|\\|\b)([a-zA-Z])(?:_\{([a-zA-Z0-9_,]+)\}|_([a-zA-Z0-9]))", text
    )
    for m in subscript_matches:
        base = m.group(1)
        sub = m.group(2) or m.group(3)
        symbols.add(f"{base}_{{{sub}}}")

    # 4. Powers/variances like \sigma^2 or s^2
    power_matches = re.finditer(r"(?:\$|\\|\b)([a-zA-Z]+)\^\{?([0-9]+)\}?", text)
    for m in power_matches:
        base = m.group(1).lstrip("\\")
        pwr = m.group(2)
        symbols.add(f"{base}^{pwr}")

    return sorted(symbols)


def extract_equation_references(text: str) -> list[str]:
    """Extract equation label numbers or IDs referenced in the text.

    Examples:
        'as shown in Equation (1)' -> ['1']
        'substituting Eq. (2.3) into (4)' -> ['2.3']

    Args:
        text: Text to search for equation references.

    Returns:
        Sorted unique list of equation label strings.
    """
    refs: set[str] = set()
    for m in EQUATION_REF_RE.finditer(text):
        label = m.group(1).strip()
        if label:
            refs.add(label)
    return sorted(refs)


def extract_variable_glossary(text: str) -> dict[str, str]:
    """Extract mapping of variable symbols to their explanatory definitions from natural language.

    Example:
        'where $RS$ denotes runs scored, and $RA$ is the runs allowed' ->
        {'RS': 'runs scored', 'RA': 'runs allowed'}
    """
    glossary: dict[str, str] = {}
    for m in VARIABLE_DEF_RE.finditer(text):
        var = m.group(1).strip("$").strip()
        desc = m.group(2).strip()
        if var and desc:
            glossary[var] = desc
    return glossary
