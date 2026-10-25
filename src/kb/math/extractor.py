"""LaTeX formula extractor and SymPy symbolic parser."""

from __future__ import annotations

import hashlib
import logging
import re
from typing import Any

from pydantic import BaseModel, ConfigDict, Field
from sympy.core.relational import Equality
from sympy.parsing.latex import parse_latex

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
