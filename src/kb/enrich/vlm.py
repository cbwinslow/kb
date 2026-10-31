"""Multimodal Figure VLM Grounding and Relational Extraction.

Analyzes scientific figures, diagrams, and trajectory plots to extract
visual semantics, axis metrics, curve trends, and relational links to formulas.
"""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, Field
from sqlalchemy import select

from kb.storage.models import Figure, Formula

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class FigureGroundingResult(BaseModel):
    """Structured visual and relational analysis of a scientific figure."""

    figure_id: str = Field(description="Unique identifier of the figure")
    citekey: str = Field(description="Document citekey")
    diagram_type: str = Field(
        default="line_chart",
        description="Classified diagram type (e.g. trajectory_plot, scatter_plot, line_chart)",
    )
    vlm_summary: str = Field(
        default="", description="Descriptive visual summary of plotted trends and relationships"
    )
    detected_curves: dict[str, Any] = Field(
        default_factory=dict, description="Extracted axes labels, units, and curve descriptions"
    )
    formula_ids: list[str] = Field(
        default_factory=list, description="IDs of linked mathematical formulas"
    )


class FigureVLMProcessor:
    """Processes scientific figures to extract visual attributes and link to mathematical formulas."""

    DIAGRAM_KEYWORDS: dict[str, list[str]] = {
        "trajectory_plot": ["trajectory", "flight path", "aerodynamic drag", "baseball flight", "pitch track"],
        "contour_map": ["contour", "heatmap", "surface", "density map", "field map"],
        "schematic": ["schematic", "apparatus", "experimental setup", "geometry", "diagram of"],
        "bar_chart": ["bar chart", "histogram", "frequencies", "bar graph"],
        "scatter_plot": ["scatter", "correlation", "versus", " vs.", " vs "],
        "line_chart": ["variation", "measured", "trend", "evolution", "profile", "response"],
    }

    UNIT_PATTERNS: list[tuple[str, str]] = [
        (r"\b(?:mph|mi/h)\b", "mph"),
        (r"\b(?:m/s|ms\^{-1})\b", "m/s"),
        (r"\b(?:deg|degrees|°)\b", "degrees"),
        (r"\b(?:rad|radians)\b", "radians"),
        (r"\b(?:ft|feet)\b", "ft"),
        (r"\b(?:m|meters)\b", "m"),
        (r"\b(?:rpm|rev/min)\b", "rpm"),
        (r"\b(?:s|sec|seconds)\b", "seconds"),
        (r"%", "percent"),
    ]

    def classify_diagram_type(self, text: str) -> str:
        """Classify scientific diagram type based on textual cues and terminology."""
        lower_text = text.lower()
        for dtype, kws in self.DIAGRAM_KEYWORDS.items():
            if any(kw in lower_text for kw in kws):
                return dtype
        return "line_chart"

    def extract_axes_and_curves(self, text: str) -> dict[str, Any]:
        """Extract x/y axis labels, measurement units, and curve descriptions from text."""
        x_label: str | None = None
        y_label: str | None = None
        x_unit: str | None = None
        y_unit: str | None = None

        # Detect 'Y versus X' or 'Y as a function of X'
        vs_match = re.search(r"([\w\s\-(),]+?)\s+(?:versus|vs\.?)\s+([\w\s\-(),]+)", text, re.IGNORECASE)
        fn_match = re.search(r"([\w\s\-(),]+?)\s+as\s+a\s+function\s+of\s+([\w\s\-(),]+)", text, re.IGNORECASE)

        y_raw = ""
        x_raw = ""
        if vs_match:
            y_raw = vs_match.group(1).strip()
            x_raw = vs_match.group(2).strip()
        elif fn_match:
            y_raw = fn_match.group(1).strip()
            x_raw = fn_match.group(2).strip()

        # Search for measurement units directly inside axis text
        if y_raw:
            for pat, unit in self.UNIT_PATTERNS:
                if re.search(pat, y_raw, re.IGNORECASE):
                    y_unit = unit
                    break

        if x_raw:
            for pat, unit in self.UNIT_PATTERNS:
                if re.search(pat, x_raw, re.IGNORECASE):
                    x_unit = unit
                    break

        # Fallback to general text if not found in axis phrases
        if y_unit is None or x_unit is None:
            for pat, unit in self.UNIT_PATTERNS:
                if re.search(pat, text, re.IGNORECASE):
                    if y_unit is None:
                        y_unit = unit
                    elif x_unit is None and unit != y_unit:
                        x_unit = unit

        # Clean figure prefix and parenthetical units from axis labels
        y_label = y_raw
        x_label = x_raw
        if y_label:
            y_label = re.sub(r"^(?:Figure|Fig\.?)\s*[0-9]+[\s.:-]*", "", y_label, flags=re.IGNORECASE).strip()
            y_label = re.sub(r"\s*\([^)]*\)", "", y_label).strip()
        if x_label:
            x_label = re.sub(r"[\s,;.]+$", "", x_label).strip()
            x_label = re.sub(r"\s*\([^)]*\)", "", x_label).strip()

        curves: list[dict[str, str]] = []
        if re.search(r"solid\s+(?:line|curve)", text, re.IGNORECASE):
            curves.append({"style": "solid", "description": "Primary experimental measurement"})
        if re.search(r"dashed\s+(?:line|curve)", text, re.IGNORECASE):
            curves.append({"style": "dashed", "description": "Theoretical or model simulation"})
        if re.search(r"dotted\s+(?:line|curve)", text, re.IGNORECASE):
            curves.append({"style": "dotted", "description": "Baseline reference trajectory"})

        return {
            "axes": {
                "x": {"label": x_label or "independent_variable", "unit": x_unit},
                "y": {"label": y_label or "dependent_variable", "unit": y_unit},
            },
            "curves": curves,
        }

    def link_formulas(
        self,
        text: str,
        available_formulas: list[Formula] | None = None,
    ) -> list[str]:
        """Identify formula IDs referenced in figure captions or contextual text blocks."""
        if not available_formulas:
            return []

        linked_ids: list[str] = []

        # 1. Match explicit equation references: Eq. (1), Equation 2, (1.2)
        eq_refs = re.findall(r"(?:Eq(?:uation)?\.?\s*\(?|(?<=\())([0-9]+(?:\.[0-9]+)*)(?:\)?)", text, re.IGNORECASE)
        ref_set = set(eq_refs)

        for f in available_formulas:
            # Check if formula ID or raw latex tag matches equation reference
            if any(ref in f.id for ref in ref_set):
                linked_ids.append(f.id)
                continue

            # Check if formula contains distinctive symbols referenced in caption
            symbols = f.symbols or []
            if symbols and all(sym in text for sym in symbols[:2]):
                linked_ids.append(f.id)

        return list(dict.fromkeys(linked_ids))

    def analyze_figure(
        self,
        figure_id: str,
        citekey: str,
        caption: str | None = None,
        chunk_text: str | None = None,
        available_formulas: list[Formula] | None = None,
    ) -> FigureGroundingResult:
        """Perform multimodal grounding on a scientific figure."""
        combined_text = f"{caption or ''} {chunk_text or ''}".strip()
        diagram_type = self.classify_diagram_type(combined_text)
        detected_curves = self.extract_axes_and_curves(combined_text)
        linked_formula_ids = self.link_formulas(combined_text, available_formulas)

        axes = detected_curves.get("axes", {})
        x_info = axes.get("x", {})
        y_info = axes.get("y", {})

        summary = (
            f"{diagram_type.replace('_', ' ').capitalize()} from {citekey}. "
            f"Plots {y_info.get('label', 'variable')} versus {x_info.get('label', 'variable')}. "
            f"Context: {caption[:120] if caption else 'Visual scientific evidence'}."
        )

        return FigureGroundingResult(
            figure_id=figure_id,
            citekey=citekey,
            diagram_type=diagram_type,
            vlm_summary=summary,
            detected_curves=detected_curves,
            formula_ids=linked_formula_ids,
        )

    async def batch_process_figures(
        self,
        session: AsyncSession,
        limit: int | None = None,
    ) -> list[FigureGroundingResult]:
        """Scan ungrounded figures from the database, compute grounding, and persist updates."""
        stmt = select(Figure).where(Figure.vlm_summary.is_(None))
        if limit:
            stmt = stmt.limit(limit)

        figures = list((await session.execute(stmt)).scalars().all())
        if not figures:
            return []

        results: list[FigureGroundingResult] = []
        for fig in figures:
            # Retrieve document formulas for relational linking
            f_stmt = select(Formula).where(Formula.citekey == fig.citekey)
            formulas = list((await session.execute(f_stmt)).scalars().all())

            grounding = self.analyze_figure(
                figure_id=fig.id,
                citekey=fig.citekey,
                caption=fig.caption,
                chunk_text=fig.chunk.enriched_text if fig.chunk else None,
                available_formulas=formulas,
            )

            fig.vlm_summary = grounding.vlm_summary
            fig.detected_curves = grounding.detected_curves
            fig.formula_ids = grounding.formula_ids
            results.append(grounding)

        await session.commit()
        return results
