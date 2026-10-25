"""Unit tests for mathematical formula lineage and derivation graph module."""

from kb.math.lineage import (
    DerivationEdge,
    DerivationNode,
    DerivationRelation,
    FormulaLineageGraph,
)


def test_lineage_graph_basic_construction() -> None:
    graph = FormulaLineageGraph()

    node_a = DerivationNode(
        formula_id="form_a",
        citekey="miller2005",
        raw_latex="WP = \\frac{RS^\\gamma}{RS^\\gamma + RA^\\gamma}",
        sanitized_latex="WP = RS^\\gamma / (RS^\\gamma + RA^\\gamma)",
        symbols=["WP", "RS", "RA", "gamma"],
        is_equality=True,
        year=2005,
    )
    node_b = DerivationNode(
        formula_id="form_b",
        citekey="dayaratna2012",
        raw_latex="WP \\approx \\frac{1}{2} + \\frac{\\gamma}{4 R_{ave}} (RS - RA)",
        sanitized_latex="WP \\approx 0.5 + (\\gamma / (4 * R_{ave})) * (RS - RA)",
        symbols=["WP", "RS", "RA", "gamma", "R_ave"],
        is_equality=False,
        year=2012,
    )

    graph.add_node(node_a)
    graph.add_node(node_b)

    assert len(graph.nodes) == 2
    assert "form_a" in graph.nodes
    assert "form_b" in graph.nodes


def test_infer_lineage_edges() -> None:
    graph = FormulaLineageGraph()

    # Miller 2005 Pythagorean expectation
    node_a = DerivationNode(
        formula_id="miller_pythag",
        citekey="miller2005",
        raw_latex="WP = \\frac{RS^\\gamma}{RS^\\gamma + RA^\\gamma}",
        sanitized_latex="WP = RS^\\gamma / (RS^\\gamma + RA^\\gamma)",
        symbols=["WP", "RS", "RA", "gamma"],
        is_equality=True,
        year=2005,
    )
    # Dayaratna 2012 Linear approximation
    node_b = DerivationNode(
        formula_id="dayaratna_linear",
        citekey="dayaratna2012",
        raw_latex="WP \\approx \\frac{1}{2} + \\frac{\\gamma}{4 R_{ave}} (RS - RA)",
        sanitized_latex="WP \\approx 0.5 + (\\gamma / (4 * R_{ave})) * (RS - RA)",
        symbols=["WP", "RS", "RA", "gamma"],
        is_equality=False,
        year=2012,
    )

    graph.add_node(node_a)
    graph.add_node(node_b)

    inferred_count = graph.infer_lineage_edges(min_symbol_overlap=2, jaccard_threshold=0.5)
    assert inferred_count == 1
    assert len(graph.edges) == 1

    edge = graph.edges[0]
    assert edge.source_id == "miller_pythag"
    assert edge.target_id == "dayaratna_linear"
    assert edge.relation == DerivationRelation.APPROXIMATION
    assert "gamma" in edge.shared_symbols
    assert edge.confidence > 0.5


def test_lineage_traversal_and_mermaid() -> None:
    graph = FormulaLineageGraph()

    node_1 = DerivationNode(
        formula_id="n1",
        citekey="paper1",
        raw_latex="y = f(x)",
        sanitized_latex="y = f(x)",
        symbols=["x", "y"],
        is_equality=True,
        year=2000,
    )
    node_2 = DerivationNode(
        formula_id="n2",
        citekey="paper2",
        raw_latex="y = g(x)",
        sanitized_latex="y = g(x)",
        symbols=["x", "y"],
        is_equality=True,
        year=2010,
    )

    graph.add_node(node_1)
    graph.add_node(node_2)
    edge = DerivationEdge(
        source_id="n1",
        target_id="n2",
        relation=DerivationRelation.DERIVATION,
        confidence=0.85,
        reason="Shared variables",
        shared_symbols=["x", "y"],
    )
    graph.add_edge(edge)

    upstream = graph.get_upstream("n2")
    assert len(upstream) == 1
    assert upstream[0].source_id == "n1"

    downstream = graph.get_downstream("n1")
    assert len(downstream) == 1
    assert downstream[0].target_id == "n2"

    mermaid_str = graph.to_mermaid()
    assert "flowchart TD" in mermaid_str
    assert "n1 -->" in mermaid_str

    as_dict = graph.to_dict()
    assert as_dict["node_count"] == 2
    assert as_dict["edge_count"] == 1
