"""Hermetic unit tests for Strawberry GraphQL schema and queries."""

from __future__ import annotations

import pytest

from kb.graphql.schema import schema


@pytest.mark.asyncio
async def test_graphql_query_concepts() -> None:
    """Verifies that concepts query returns canonical concepts from ontology."""
    query = """
    query {
        concepts {
            name
            latexRepr
            description
            aliases
        }
    }
    """
    result = await schema.execute(query)
    assert result.errors is None
    assert result.data is not None
    concepts = result.data["concepts"]
    assert len(concepts) >= 10

    names = [c["name"] for c in concepts]
    assert "runs_scored" in names
    assert "home_runs" in names
    assert "win_pct" in names


@pytest.mark.asyncio
async def test_graphql_query_formulas_and_documents() -> None:
    """Verifies querying formulas and documents through GraphQL."""
    query = """
    query {
        formulas(limit: 5) {
            id
            citekey
            latex
            isValid
            isEquality
        }
        documents(limit: 5) {
            id
            citekey
            title
            formulaCount
        }
    }
    """
    result = await schema.execute(query)
    assert result.errors is None
    assert result.data is not None
    assert "formulas" in result.data
    assert "documents" in result.data


@pytest.mark.asyncio
async def test_graphql_query_knowledge_graph() -> None:
    """Verifies multi-layer knowledge graph query returns nodes and edges."""
    query = """
    query {
        knowledgeGraph(limit: 10) {
            nodes {
                id
                label
                layer
            }
            edges {
                source
                target
                relation
            }
        }
    }
    """
    result = await schema.execute(query)
    assert result.errors is None
    assert result.data is not None
    kg = result.data["knowledgeGraph"]
    assert "nodes" in kg
    assert "edges" in kg


@pytest.mark.asyncio
async def test_graphql_query_formula_coverage() -> None:
    """Verifies formula coverage query in GraphQL."""
    query = """
    query {
        formulaCoverage(limit: 20) {
            totalFormulas
            validFormulas
            parseYieldPct
            uniqueSymbolsCount
            topCharacters
            topErrors
        }
    }
    """
    result = await schema.execute(query)
    assert result.errors is None
    assert result.data is not None
    cov = result.data["formulaCoverage"]
    assert "totalFormulas" in cov
    assert "validFormulas" in cov
    assert "parseYieldPct" in cov
    assert "uniqueSymbolsCount" in cov
