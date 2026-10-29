"""Formula and Variable Coverage Metrics Engine.

Audits mathematical formula parsing yield, symbol definitions vs. usages,
ontology mapping rates, orphan variables, and character distributions across
scientific literature and local memory collections.
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select

from kb.math.ontology import SymbolOntology

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from kb.math.extractor import ExtractedFormula
    from kb.storage.models import Formula


class FormulaCoverageReport(BaseModel):
    """Structured report detailing mathematical formula parsing yield and variable coverage."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    total_formulas: int = Field(default=0, description="Total formulas audited")
    valid_formulas: int = Field(default=0, description="Formulas parsed successfully by SymPy")
    invalid_formulas: int = Field(default=0, description="Formulas failing SymPy validation")
    equality_formulas: int = Field(
        default=0, description="Formulas defining an explicit equality (LHS = RHS)"
    )
    parse_yield_pct: float = Field(default=0.0, description="Percentage of valid formulas")
    equality_yield_pct: float = Field(
        default=0.0, description="Percentage of equality formulas among valid"
    )
    unique_symbols: list[str] = Field(default_factory=list, description="Unique symbols extracted")
    defined_symbols: list[str] = Field(
        default_factory=list, description="Symbols defined on LHS of equality formulas"
    )
    consumed_symbols: list[str] = Field(
        default_factory=list, description="Symbols consumed on RHS or free expressions"
    )
    ontology_mapped_symbols: list[str] = Field(
        default_factory=list, description="Symbols mapping directly to SymbolOntology concepts"
    )
    orphan_symbols: list[str] = Field(
        default_factory=list,
        description="Consumed symbols lacking an LHS definition and unmapped to canonical ontology",
    )
    error_taxonomy: dict[str, int] = Field(
        default_factory=dict, description="Taxonomy of parser failure reasons and counts"
    )
    character_accounting: dict[str, int] = Field(
        default_factory=dict, description="Distribution of non-ASCII characters across formulas"
    )

    def to_markdown(self) -> str:
        """Format the coverage metrics report as clean GitHub-Flavored Markdown."""
        lines: list[str] = []
        lines.append("# Mathematical Formula & Variable Coverage Report")
        lines.append("")
        lines.append("## Executive Summary")
        lines.append(f"- **Total Formulas Audited**: {self.total_formulas:,}")
        lines.append(
            f"- **Valid SymPy AST Formulas**: {self.valid_formulas:,} ({self.parse_yield_pct:.2f}%)"
        )
        lines.append(f"- **Invalid Formulas**: {self.invalid_formulas:,}")
        lines.append(
            f"- **Equality Relations ($LHS = RHS$)**: {self.equality_formulas:,} ({self.equality_yield_pct:.2f}% of valid)"
        )
        lines.append(f"- **Total Unique Symbols**: {len(self.unique_symbols):,}")
        lines.append(
            f"- **Ontology-Mapped Symbols**: {len(self.ontology_mapped_symbols):,} ({len(self.ontology_mapped_symbols) / max(len(self.unique_symbols), 1) * 100:.1f}%)"
        )
        lines.append(f"- **Orphan / Unbound Symbols**: {len(self.orphan_symbols):,}")
        lines.append("")

        lines.append("## Symbol Utilization Analysis")
        lines.append("| Metric | Count | Sample Identifiers |")
        lines.append("| --- | --- | --- |")
        lines.append(
            f"| Defined (LHS) | {len(self.defined_symbols):,} | `{', '.join(self.defined_symbols[:10])}` |"
        )
        lines.append(
            f"| Consumed (RHS) | {len(self.consumed_symbols):,} | `{', '.join(self.consumed_symbols[:10])}` |"
        )
        lines.append(
            f"| Canonical Mapped | {len(self.ontology_mapped_symbols):,} | `{', '.join(self.ontology_mapped_symbols[:10])}` |"
        )
        lines.append(
            f"| Orphan / Unconstrained | {len(self.orphan_symbols):,} | `{', '.join(self.orphan_symbols[:10])}` |"
        )
        lines.append("")

        if self.character_accounting:
            lines.append("## Non-ASCII Character Accounting (Top 15)")
            lines.append("| Unicode | Hex Code | Frequency |")
            lines.append("| --- | --- | --- |")
            sorted_chars = sorted(
                self.character_accounting.items(), key=lambda x: x[1], reverse=True
            )[:15]
            for ch, count in sorted_chars:
                codepoint = f"U+{ord(ch):04X}"
                char_display = ch if ord(ch) >= 32 and ch != "|" else f"`{codepoint}`"
                lines.append(f"| {char_display} | `{codepoint}` | {count:,} |")
            lines.append("")

        if self.error_taxonomy:
            lines.append("## Parser Error Taxonomy (Top 10)")
            lines.append("| Error Category | Occurrences |")
            lines.append("| --- | --- |")
            sorted_errors = sorted(self.error_taxonomy.items(), key=lambda x: x[1], reverse=True)[
                :10
            ]
            for err, count in sorted_errors:
                lines.append(f"| `{err}` | {count:,} |")
            lines.append("")

        return "\n".join(lines)

    def to_json(self, indent: int = 2) -> str:
        """Format the coverage metrics report as formatted JSON."""
        return self.model_dump_json(indent=indent)


class FormulaCoverageAnalyzer:
    """Analyzes mathematical expressions and corpus databases for yield and variable coverage."""

    def __init__(self, ontology: SymbolOntology | None = None) -> None:
        """Initialize analyzer with canonical symbol ontology.

        Args:
            ontology: Optional SymbolOntology instance. Default is instantiated if omitted.
        """
        self.ontology = ontology or SymbolOntology()

    def analyze_extracted_formulas(
        self, formulas: list[ExtractedFormula] | list[Formula] | list[dict[str, Any]]
    ) -> FormulaCoverageReport:
        """Analyze a collection of extracted formulas in-memory.

        Args:
            formulas: List of ExtractedFormula instances, Formula ORM models, or dictionaries.

        Returns:
            FormulaCoverageReport with complete coverage diagnostics.
        """
        total = len(formulas)
        valid_cnt = 0
        eq_cnt = 0

        defined_set: set[str] = set()
        consumed_set: set[str] = set()
        all_symbols_set: set[str] = set()
        char_counts: Counter[str] = Counter()
        error_counts: Counter[str] = Counter()

        for item in formulas:
            # Handle heterogeneous input representations
            is_valid: bool = (
                getattr(item, "is_valid", False)
                if not isinstance(item, dict)
                else item.get("is_valid", False)
            )
            is_eq: bool = (
                getattr(item, "is_equality", False)
                if not isinstance(item, dict)
                else item.get("is_equality", False)
            )
            lhs: str | None = (
                getattr(item, "lhs", None) if not isinstance(item, dict) else item.get("lhs")
            )
            raw: str = (
                getattr(item, "raw_latex", "")
                if not isinstance(item, dict)
                else item.get("raw_latex", "")
            )
            symbols: list[str] = (
                getattr(item, "symbols", [])
                if not isinstance(item, dict)
                else item.get("symbols", [])
            )
            err_msg: str | None = (
                getattr(item, "error_message", None)
                if not isinstance(item, dict)
                else item.get("error_message")
            )

            # Character accounting for non-ASCII
            for c in raw:
                if ord(c) > 127:
                    char_counts[c] += 1

            if is_valid:
                valid_cnt += 1
                if is_eq:
                    eq_cnt += 1
                    if lhs:
                        # Normalize LHS symbol
                        clean_lhs = lhs.strip().replace(" ", "")
                        defined_set.add(clean_lhs)
                        all_symbols_set.add(clean_lhs)

                for sym in symbols:
                    all_symbols_set.add(sym)
                    if not is_eq or (lhs and sym != lhs.strip().replace(" ", "")):
                        consumed_set.add(sym)
            else:
                category = self._categorize_error(err_msg, raw)
                error_counts[category] += 1

        invalid_cnt = total - valid_cnt
        parse_yield = (valid_cnt / total * 100.0) if total > 0 else 0.0
        eq_yield = (eq_cnt / valid_cnt * 100.0) if valid_cnt > 0 else 0.0

        # Ontology mapping
        mapped_symbols: list[str] = []
        for sym in sorted(all_symbols_set):
            if self.ontology.resolve_canonical(sym) is not None:
                mapped_symbols.append(sym)

        # Orphan symbols: consumed but not defined anywhere on LHS and not in ontology
        mapped_set = set(mapped_symbols)
        orphan_symbols = sorted(consumed_set - defined_set - mapped_set)

        return FormulaCoverageReport(
            total_formulas=total,
            valid_formulas=valid_cnt,
            invalid_formulas=invalid_cnt,
            equality_formulas=eq_cnt,
            parse_yield_pct=round(parse_yield, 2),
            equality_yield_pct=round(eq_yield, 2),
            unique_symbols=sorted(all_symbols_set),
            defined_symbols=sorted(defined_set),
            consumed_symbols=sorted(consumed_set),
            ontology_mapped_symbols=mapped_symbols,
            orphan_symbols=orphan_symbols,
            error_taxonomy=dict(error_counts.most_common(20)),
            character_accounting=dict(char_counts.most_common(30)),
        )

    async def analyze_corpus(
        self,
        limit: int | None = None,
        session: AsyncSession | None = None,
    ) -> FormulaCoverageReport:
        """Scan stored database formulas and compute coverage metrics across the corpus.

        Args:
            limit: Optional maximum number of formulas to scan.
            session: Optional existing AsyncSession. If None, acquires one from DatabaseManager.

        Returns:
            FormulaCoverageReport based on the stored database records.
        """
        from kb.storage.database import DatabaseManager
        from kb.storage.models import Formula

        if session is not None:
            stmt = select(Formula)
            if limit:
                stmt = stmt.limit(limit)
            results = (await session.execute(stmt)).scalars().all()
            return self.analyze_extracted_formulas(list(results))

        db = DatabaseManager()
        async with db.get_session() as sess:
            stmt = select(Formula)
            if limit:
                stmt = stmt.limit(limit)
            results = (await sess.execute(stmt)).scalars().all()
            return self.analyze_extracted_formulas(list(results))

    def _categorize_error(self, err_msg: str | None, raw: str) -> str:
        """Categorize parser errors into meaningful failure buckets."""
        if not err_msg:
            if not raw or not raw.strip():
                return "Empty formula"
            if any(ord(c) > 127 for c in raw):
                return "Unsanitized Unicode in raw LaTeX"
            return "Unclassified parser error"

        msg = err_msg.lower()
        if "i don't understand this" in msg:
            return "ANTLR unrecognized token or syntax"
        if "expected one of these" in msg:
            return "ANTLR syntax expectation mismatch"
        if "missing" in msg and ("}" in msg or ")" in msg or "]" in msg):
            return "Unbalanced brackets or braces"
        if "empty formula" in msg:
            return "Empty formula after sanitization"
        if "can only compare" in msg:
            return "Unsupported inequality comparison"
        return err_msg.split("\n")[0][:50]
