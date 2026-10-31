"""Unit tests for multimodal figure VLM grounding and FastMCP figure tools."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from kb.enrich.vlm import FigureVLMProcessor
from kb.mcp.server import create_mcp_server
from kb.storage.models import Figure, Formula


@pytest.fixture
def vlm_processor() -> FigureVLMProcessor:
    """Fixture providing FigureVLMProcessor instance."""
    return FigureVLMProcessor()


def test_classify_diagram_type(vlm_processor: FigureVLMProcessor) -> None:
    """Verify diagram type classification from caption text."""
    assert (
        vlm_processor.classify_diagram_type("Figure 3: Baseball flight trajectory under aerodynamic drag")
        == "trajectory_plot"
    )
    assert (
        vlm_processor.classify_diagram_type("Exit velocity versus launch angle correlation")
        == "scatter_plot"
    )
    assert (
        vlm_processor.classify_diagram_type("Schematic diagram of wind tunnel experimental apparatus")
        == "schematic"
    )
    assert (
        vlm_processor.classify_diagram_type("Histogram of batted ball launch speed frequencies")
        == "bar_chart"
    )
    assert (
        vlm_processor.classify_diagram_type("Surface pressure contour map across spinning sphere")
        == "contour_map"
    )


def test_extract_axes_and_curves(vlm_processor: FigureVLMProcessor) -> None:
    """Verify extraction of axes labels, units, and curve styles."""
    caption = (
        "Figure 4: Batted ball distance (ft) versus launch angle (deg). "
        "Solid line shows 100 mph exit velocity; dashed curve represents 90 mph."
    )
    extracted = vlm_processor.extract_axes_and_curves(caption)

    axes = extracted.get("axes", {})
    assert "distance" in axes["y"]["label"].lower()
    assert axes["y"]["unit"] == "ft"
    assert "launch angle" in axes["x"]["label"].lower()
    assert axes["x"]["unit"] == "degrees"

    curves = extracted.get("curves", [])
    assert len(curves) == 2
    assert curves[0]["style"] == "solid"
    assert curves[1]["style"] == "dashed"


def test_link_formulas(vlm_processor: FigureVLMProcessor) -> None:
    """Verify linking of equation numbers and mathematical symbols in captions."""
    formula1 = Formula(
        id="formula_eq1",
        citekey="nathan2008",
        raw_latex=r"F_D = \frac{1}{2} C_D \rho A v^2",
        symbols=["C_D", "rho", "v"],
        is_valid=True,
    )
    formula2 = Formula(
        id="formula_eq2",
        citekey="nathan2008",
        raw_latex=r"y = v_0 \cdot t",
        symbols=["v_0", "t"],
        is_valid=True,
    )

    caption = "Figure 2: Drag force calculated according to Eq. (1) with drag coefficient C_D and speed v."
    linked = vlm_processor.link_formulas(caption, [formula1, formula2])

    assert "formula_eq1" in linked
    assert "formula_eq2" not in linked


def test_analyze_figure(vlm_processor: FigureVLMProcessor) -> None:
    """Verify end-to-end figure analysis and grounding result synthesis."""
    caption = "Trajectory height (m) versus range (m) calculated from Eq. (1) under constant gravity."
    formula = Formula(
        id="formula_eq1",
        citekey="adair2002",
        raw_latex="y = x",
        symbols=["x"],
        is_valid=True,
    )

    result = vlm_processor.analyze_figure(
        figure_id="fig_01",
        citekey="adair2002",
        caption=caption,
        available_formulas=[formula],
    )

    assert result.figure_id == "fig_01"
    assert result.citekey == "adair2002"
    assert result.diagram_type == "trajectory_plot"
    assert "Trajectory plot" in result.vlm_summary
    assert "formula_eq1" in result.formula_ids


@pytest.mark.asyncio
async def test_mcp_get_and_search_figures() -> None:
    """Verify kb_get_figure and kb_search_figures FastMCP tools."""
    mock_db = MagicMock()
    mock_session = AsyncMock()
    mock_db.get_session.return_value.__aenter__.return_value = mock_session

    fig = Figure(
        id="fig_test_123",
        document_id="doc_1",
        citekey="watts2000",
        caption="Aerodynamic lift versus spin rate of rotating baseball",
        figure_index=1,
        image_path="/vault/figures/watts2000_fig1.png",
        vlm_summary="Trajectory plot showing lift force versus spin rate.",
        detected_curves={"axes": {"x": {"label": "spin_rate"}}},
        formula_ids=["formula_lift_01"],
    )

    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [fig]
    mock_session.execute.return_value = mock_result

    server = create_mcp_server(db_manager=mock_db)

    # Verify registration
    tools = await server.list_tools()
    tool_names = [t.name for t in tools]
    assert "kb_get_figure" in tool_names
    assert "kb_search_figures" in tool_names

    # Test kb_get_figure
    res = await server.call_tool("kb_get_figure", {"citekey": "watts2000"})
    assert not res.is_error
    assert len(res.content) >= 1
    content_str = str(res.content[0])
    assert "fig_test_123" in content_str
    assert "watts2000" in content_str
    assert "formula_lift_01" in content_str

    # Test kb_search_figures
    res_search = await server.call_tool("kb_search_figures", {"query": "lift"})
    assert not res_search.is_error
    assert len(res_search.content) >= 1
    assert "fig_test_123" in str(res_search.content[0])
