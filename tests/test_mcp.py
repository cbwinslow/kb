"""Unit and integration tests for FastMCP agent service and CLI."""

from __future__ import annotations

import uuid

import pytest

from kb.cli import build_parser
from kb.enrich.openalex import OpenAlexClient
from kb.mcp.server import create_mcp_server
from kb.storage import (
    BenchmarkTable,
    Chunk,
    DatabaseManager,
    Document,
    Formula,
)
from kb.storage.embeddings import MockEmbeddingGenerator
from tests.test_openalex import MockOpenAlexTransport


@pytest.fixture
def test_db_manager() -> DatabaseManager:
    """Provides an in-memory async database manager for hermetic FastMCP testing."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_{db_id}?mode=memory&cache=shared&uri=true"
    return DatabaseManager(database_url=url, echo=False)


@pytest.mark.asyncio
async def test_mcp_tools_registration(test_db_manager: DatabaseManager) -> None:
    """Verifies that all required KB tools are registered with FastMCP."""
    server = create_mcp_server(test_db_manager, embedder=MockEmbeddingGenerator())
    # Check tool names registered on FastMCP
    tools = await server.list_tools()
    tool_names = [t.name for t in tools]

    assert "kb_search_literature" in tool_names
    assert "kb_get_formula" in tool_names
    assert "kb_compile_formula" in tool_names
    assert "kb_execute_formula" in tool_names
    assert "kb_get_benchmark_table" in tool_names
    assert "kb_get_bibtex" in tool_names
    assert "kb_get_citations" in tool_names
    assert "kb_get_related_papers" in tool_names
    await test_db_manager.close()


@pytest.mark.asyncio
async def test_mcp_tools_execution(test_db_manager: DatabaseManager) -> None:
    """Verifies end-to-end tool execution against test database data."""
    await test_db_manager.init_db()

    # Populate test data
    async with test_db_manager.get_session() as session:
        doc = Document(
            citekey="miller2005",
            title="A Derivation of the Pythagorean Expectation for Baseball",
            authors=["Steven J. Miller"],
            year=2005,
            arxiv_id="math/0509698",
        )
        session.add(doc)
        await session.flush()

        chunk_text = "[miller2005 | Models] Pythagorean expectation relates runs to wins."
        chunk = Chunk(
            document_id=doc.id,
            chunk_index=0,
            citekey=doc.citekey,
            raw_text="W = \\frac{R_S^\\gamma}{R_S^\\gamma + R_A^\\gamma}",
            enriched_text=chunk_text,
            section_path=["2. Models"],
            has_math=True,
            has_table=False,
            embedding=MockEmbeddingGenerator().embed_query(chunk_text),
        )
        session.add(chunk)
        await session.flush()

        formula = Formula(
            document_id=doc.id,
            chunk_id=chunk.id,
            citekey=doc.citekey,
            raw_latex="W = \\frac{R_S^\\gamma}{R_S^\\gamma + R_A^\\gamma}",
            sanitized_latex="W = \\frac{R_S^\\gamma}{R_S^\\gamma + R_A^\\gamma}",
            sympy_repr="Eq(W, R_S**gamma / (R_A**gamma + R_S**gamma))",
            symbols=["W", "R_S", "R_A", "gamma"],
            is_valid=True,
            is_equality=True,
            lhs="W",
            rhs="R_S**gamma / (R_A**gamma + R_S**gamma)",
        )
        session.add(formula)

        table = BenchmarkTable(
            document_id=doc.id,
            chunk_id=chunk.id,
            citekey=doc.citekey,
            caption="Table 1: Empirical Exponent Fits",
            parquet_path="data/fixtures/miller2005/table_0.parquet",
            csv_path="data/fixtures/miller2005/table_0.csv",
            num_rows=30,
            num_cols=4,
            column_names=["Season", "Exponent_gamma", "StdErr", "R_Squared"],
        )
        session.add(table)

    mock_embedder = MockEmbeddingGenerator()
    mock_openalex = OpenAlexClient(transport=MockOpenAlexTransport())
    server = create_mcp_server(
        test_db_manager,
        embedder=mock_embedder,
        openalex_client=mock_openalex,
    )

    # 1. Test kb_search_literature tool call
    search_res = await server.call_tool(
        "kb_search_literature",
        {"query": "Pythagorean expectation", "citekey": "miller2005"},
    )
    assert not search_res.is_error
    assert len(search_res.content) >= 1
    content_str = str(search_res.content[0])
    assert "miller2005" in content_str
    assert "dense_rank" in content_str
    assert "rrf_score" in content_str

    # 2. Test kb_get_formula tool call
    formula_res = await server.call_tool(
        "kb_get_formula",
        {"citekey": "miller2005", "query": "gamma"},
    )
    assert not formula_res.is_error
    assert len(formula_res.content) >= 1
    assert "gamma" in str(formula_res.content[0])

    # 3. Test kb_get_benchmark_table tool call
    table_res = await server.call_tool(
        "kb_get_benchmark_table",
        {"citekey": "miller2005"},
    )
    assert not table_res.is_error
    assert len(table_res.content) >= 1
    assert "Exponent_gamma" in str(table_res.content[0])

    # 4. Test kb_get_bibtex tool call
    bibtex_res = await server.call_tool(
        "kb_get_bibtex",
        {"citekey": "miller2005"},
    )
    assert not bibtex_res.is_error
    bibtex_text = str(bibtex_res.content[0])
    assert "@article{miller2005" in bibtex_text
    assert "Steven J. Miller" in bibtex_text
    assert "math/0509698" in bibtex_text

    # 5. Test kb_get_citations tool call
    citations_res = await server.call_tool(
        "kb_get_citations",
        {"openalex_id": "W1533576069"},
    )
    assert not citations_res.is_error
    assert len(citations_res.content) >= 1
    assert "Sports Data Mining" in str(citations_res.content[0])

    await test_db_manager.close()


def test_cli_parser() -> None:
    """Verifies that the CLI parser configures all subcommands correctly."""
    parser = build_parser()

    # mcp serve
    args = parser.parse_args(["mcp", "serve"])
    assert args.subcommand == "mcp"
    assert args.mcp_subcommand == "serve"

    # db check
    args = parser.parse_args(["db", "check"])
    assert args.subcommand == "db"
    assert args.db_subcommand == "check"

    # db init
    args = parser.parse_args(["db", "init"])
    assert args.subcommand == "db"
    assert args.db_subcommand == "init"

    # ingest
    args = parser.parse_args([
        "ingest",
        "data/fixtures/miller2008.pdf",
        "--citekey",
        "miller2008",
        "--year",
        "2008",
    ])
    assert args.subcommand == "ingest"
    assert str(args.pdf_path).endswith("miller2008.pdf")
    assert args.citekey == "miller2008"
    assert args.year == 2008

    # enrich openalex
    args = parser.parse_args(["enrich", "openalex", "--citekey", "miller2005"])
    assert args.subcommand == "enrich"
    assert args.enrich_subcommand == "openalex"
    assert args.citekey == "miller2005"
