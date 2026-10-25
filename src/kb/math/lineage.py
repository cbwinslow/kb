"""Mathematical formula lineage and derivation graph builder."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

logger = logging.getLogger(__name__)


class DerivationRelation(StrEnum):
    """Categorical relationship between mathematical formula nodes."""

    IDENTICAL = "identical"
    APPROXIMATION = "approximation"
    DERIVATION = "derivation"
    SHARED_SYMBOLS = "shared_symbols"
    VARIABLE_SPECIALIZATION = "variable_specialization"


@dataclass(frozen=True)
class DerivationNode:
    """Represents an extracted formula vertex in the derivation graph."""

    formula_id: str
    citekey: str
    raw_latex: str
    sanitized_latex: str
    symbols: list[str] = field(default_factory=list)
    lhs: str | None = None
    rhs: str | None = None
    is_valid: bool = False
    is_equality: bool = False
    year: int | None = None

    def symbol_set(self) -> set[str]:
        """Returns normalized set of mathematical symbols."""
        return {s.strip().lower() for s in self.symbols if s.strip()}


@dataclass(frozen=True)
class DerivationEdge:
    """Represents a directional mathematical lineage edge between two formula nodes."""

    source_id: str
    target_id: str
    relation: DerivationRelation
    confidence: float
    reason: str
    shared_symbols: list[str] = field(default_factory=list)


class FormulaLineageGraph:
    """Directed derivation graph tracking mathematical evolution across papers."""

    def __init__(self) -> None:
        self.nodes: dict[str, DerivationNode] = {}
        self.edges: list[DerivationEdge] = []
        self._adjacency: dict[str, list[DerivationEdge]] = {}
        self._reverse_adjacency: dict[str, list[DerivationEdge]] = {}

    def add_node(self, node: DerivationNode) -> None:
        """Registers a formula node in the graph."""
        self.nodes[node.formula_id] = node
        if node.formula_id not in self._adjacency:
            self._adjacency[node.formula_id] = []
        if node.formula_id not in self._reverse_adjacency:
            self._reverse_adjacency[node.formula_id] = []

    def add_edge(self, edge: DerivationEdge) -> None:
        """Registers a directed derivation edge."""
        if edge.source_id not in self.nodes or edge.target_id not in self.nodes:
            logger.debug(
                "Cannot add edge between unregistered nodes: %s -> %s",
                edge.source_id,
                edge.target_id,
            )
            return

        self.edges.append(edge)
        self._adjacency[edge.source_id].append(edge)
        self._reverse_adjacency[edge.target_id].append(edge)

    def infer_lineage_edges(
        self,
        min_symbol_overlap: int = 2,
        jaccard_threshold: float = 0.35,
    ) -> int:
        """Infers derivation and dependency relationships between all registered nodes."""
        node_list = list(self.nodes.values())
        added_count = 0

        # Sort nodes chronologically if publication years are present
        sorted_nodes = sorted(node_list, key=lambda n: n.year or 9999)

        for i, source in enumerate(sorted_nodes):
            s_symbols = source.symbol_set()
            if not s_symbols:
                continue

            for target in sorted_nodes[i + 1 :]:
                if source.citekey == target.citekey:
                    # Same document relations
                    continue

                t_symbols = target.symbol_set()
                if not t_symbols:
                    continue

                intersection = s_symbols & t_symbols
                if len(intersection) < min_symbol_overlap:
                    continue

                union = s_symbols | t_symbols
                jaccard = len(intersection) / len(union) if union else 0.0

                if jaccard < jaccard_threshold:
                    continue

                # Determine relationship type
                relation = DerivationRelation.SHARED_SYMBOLS
                confidence = round(jaccard, 2)
                reason = f"Shared symbols: {sorted(intersection)}"

                # Check for approximation indicators
                approx_signs = (r"\approx", r"\sim", "approx", "~")
                has_approx = any(sign in target.raw_latex for sign in approx_signs) or any(
                    sign in target.sanitized_latex for sign in approx_signs
                )

                if has_approx:
                    relation = DerivationRelation.APPROXIMATION
                    confidence = min(1.0, confidence + 0.2)
                    reason = f"Approximation of formulation sharing {sorted(intersection)}"
                elif target.is_equality and source.is_equality:
                    relation = DerivationRelation.DERIVATION
                    confidence = min(1.0, confidence + 0.15)
                    reason = f"Equation formulation sharing {sorted(intersection)}"

                edge = DerivationEdge(
                    source_id=source.formula_id,
                    target_id=target.formula_id,
                    relation=relation,
                    confidence=confidence,
                    reason=reason,
                    shared_symbols=sorted(intersection),
                )
                self.add_edge(edge)
                added_count += 1

        return added_count

    def get_upstream(self, formula_id: str) -> list[DerivationEdge]:
        """Returns direct incoming derivation edges for a formula."""
        return self._reverse_adjacency.get(formula_id, [])

    def get_downstream(self, formula_id: str) -> list[DerivationEdge]:
        """Returns direct outgoing derivation edges from a formula."""
        return self._adjacency.get(formula_id, [])

    def to_mermaid(self, max_edges: int = 50) -> str:
        """Renders the derivation graph as a Mermaid flowchart diagram."""
        lines = ["flowchart TD"]
        rendered_nodes: set[str] = set()

        for edge in self.edges[:max_edges]:
            src = self.nodes.get(edge.source_id)
            tgt = self.nodes.get(edge.target_id)
            if not src or not tgt:
                continue

            src_label = f"{src.citekey}"
            tgt_label = f"{tgt.citekey}"

            if edge.source_id not in rendered_nodes:
                lines.append(f'    {src.formula_id}["{src_label}"]')
                rendered_nodes.add(edge.source_id)

            if edge.target_id not in rendered_nodes:
                lines.append(f'    {tgt.formula_id}["{tgt_label}"]')
                rendered_nodes.add(edge.target_id)

            rel_text = f"{edge.relation.value} ({edge.confidence:.2f})"
            lines.append(f"    {edge.source_id} -->|{rel_text}| {edge.target_id}")

        return "\n".join(lines)

    def to_dict(self) -> dict[str, Any]:
        """Exports graph structure as a JSON-serializable dictionary."""
        return {
            "node_count": len(self.nodes),
            "edge_count": len(self.edges),
            "nodes": [
                {
                    "formula_id": n.formula_id,
                    "citekey": n.citekey,
                    "year": n.year,
                    "raw_latex": n.raw_latex,
                    "symbols": n.symbols,
                    "is_equality": n.is_equality,
                }
                for n in self.nodes.values()
            ],
            "edges": [
                {
                    "source": e.source_id,
                    "target": e.target_id,
                    "relation": e.relation.value,
                    "confidence": e.confidence,
                    "reason": e.reason,
                    "shared_symbols": e.shared_symbols,
                }
                for e in self.edges
            ],
        }
