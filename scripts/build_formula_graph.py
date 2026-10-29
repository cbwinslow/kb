"""Builds and queries the mathematical derivation graph from formulas in the KB."""

from __future__ import annotations

import argparse
import asyncio
import sys

from sqlalchemy import select

from kb.math.lineage import DerivationNode, FormulaLineageGraph
from kb.storage.database import DatabaseManager
from kb.storage.models import Document, Formula

sys.stdout.reconfigure(encoding="utf-8")


async def build_and_query_graph(
    symbol: str | None = None,
    citekey: str | None = None,
    min_overlap: int = 2,
    export_mermaid: bool = False,
) -> int:
    db = DatabaseManager()
    await db.init_db()

    print(f"[*] Loading extracted formulas and documents from {db.url.split('@')[-1]}...")
    async with db.get_session() as session:
        # Fetch all formulas and their parent document metadata
        stmt = select(Formula, Document.year, Document.title).join(
            Document, Formula.document_id == Document.id, isouter=True
        )
        if citekey:
            stmt = stmt.where(Formula.citekey == citekey)

        res = await session.execute(stmt)
        rows = res.all()

    print(f"[*] Loaded {len(rows)} mathematical formulas from database.")

    graph = FormulaLineageGraph()
    for row in rows:
        f: Formula = row[0]
        doc_year: int | None = row[1]

        # Filter by symbol if requested
        if symbol:
            sym_lower = symbol.lower()
            has_sym = any(sym_lower in s.lower() for s in (f.symbols or []))
            if not has_sym and sym_lower not in f.raw_latex.lower():
                continue

        node = DerivationNode(
            formula_id=f.id,
            citekey=f.citekey,
            raw_latex=f.raw_latex,
            sanitized_latex=f.sanitized_latex,
            symbols=f.symbols or [],
            lhs=f.lhs,
            rhs=f.rhs,
            is_valid=f.is_valid,
            is_equality=f.is_equality,
            year=doc_year,
        )
        graph.add_node(node)

    print(f"[*] Registered {len(graph.nodes)} candidate nodes in derivation graph.")
    inferred_edges = graph.infer_lineage_edges(min_symbol_overlap=min_overlap)
    print(f"[+] Inferred {inferred_edges} derivation / dependency edges.")

    if export_mermaid and graph.edges:
        print("\n" + "=" * 60)
        print("Mermaid Derivation Diagram:")
        print("=" * 60)
        print(graph.to_mermaid(max_edges=30))
        print("=" * 60)
    elif graph.edges:
        print("\nTop Inferred Formula Derivations:")
        for idx, edge in enumerate(graph.edges[:15], 1):
            src = graph.nodes[edge.source_id]
            tgt = graph.nodes[edge.target_id]
            src_yr = str(src.year or "?")
            tgt_yr = str(tgt.year or "?")
            print(
                f"[{idx:2d}] {src.citekey} ({src_yr}) -> {tgt.citekey} ({tgt_yr}) "
                f"| {edge.relation.value:<15} | Shared: {edge.shared_symbols}"
            )

    await db.close()
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build mathematical formula lineage and derivation graph."
    )
    parser.add_argument("--symbol", type=str, default=None, help="Filter formulas by symbol")
    parser.add_argument("--citekey", type=str, default=None, help="Filter formulas by citekey")
    parser.add_argument(
        "--min-overlap", type=int, default=2, help="Minimum shared symbols for edge"
    )
    parser.add_argument("--mermaid", action="store_true", help="Print Mermaid diagram")

    args = parser.parse_args()
    asyncio.run(
        build_and_query_graph(
            symbol=args.symbol,
            citekey=args.citekey,
            min_overlap=args.min_overlap,
            export_mermaid=args.mermaid,
        )
    )


if __name__ == "__main__":
    main()
