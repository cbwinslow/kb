"""Unit tests for the Web UI and REST API."""

from __future__ import annotations

import pytest
from starlette.testclient import TestClient

from kb.ui.app import create_app


@pytest.fixture
def test_client() -> TestClient:
    app = create_app()
    return TestClient(app)


def test_ui_index(test_client: TestClient) -> None:
    response = test_client.get("/")
    assert response.status_code == 200
    assert "Scientific Knowledge Base" in response.text
    assert "Mathematical Derivation Network" in response.text


def test_ui_stats_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/api/stats")
    assert response.status_code == 200
    data = response.json()
    assert "documents" in data
    assert "chunks" in data
    assert "formulas" in data
    assert "tables" in data
    assert data["documents"] >= 0


def test_ui_lineage_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/api/lineage?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert "nodes" in data
    assert "edges" in data
    assert "num_nodes" in data


def test_ui_formulas_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/api/formulas?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_ui_tables_endpoint(test_client: TestClient) -> None:
    response = test_client.get("/api/tables?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_ui_eval_endpoint_missing_id(test_client: TestClient) -> None:
    response = test_client.get("/api/eval")
    assert response.status_code == 400
    assert "Missing formula_id" in response.json()["error"]


def test_ui_eval_endpoint_not_found(test_client: TestClient) -> None:
    response = test_client.get("/api/eval?formula_id=999999999")
    assert response.status_code == 404
    assert "not found" in response.json()["error"]


def test_ui_playground_route(test_client: TestClient) -> None:
    """Verify /playground route serves interactive HTML dashboard."""
    response = test_client.get("/playground")
    assert response.status_code == 200
    assert "Interactive Formula Playground" in response.text
    assert "pg-curve-svg" in response.text


def test_ui_presets_endpoint(test_client: TestClient) -> None:
    """Verify /api/presets returns canonical sabermetric presets."""
    response = test_client.get("/api/presets")
    assert response.status_code == 200
    presets = response.json()
    assert isinstance(presets, list)
    assert len(presets) >= 3
    preset_ids = [p["id"] for p in presets]
    assert "pythagorean" in preset_ids
    assert "fip" in preset_ids
    assert "woba" in preset_ids


def test_ui_eval_custom_latex(test_client: TestClient) -> None:
    """Verify dynamic evaluation of custom formula with direct parameters."""
    payload = {
        "formula_id": "custom",
        "latex": r"W = \frac{R_S^{2}}{R_S^{2} + R_A^{2}}",
        "inputs": {"R_S": 800, "R_A": 650},
    }
    response = test_client.post("/api/eval", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    # 800^2 / (800^2 + 650^2) = 640000 / (640000 + 422500) = 0.60235
    assert pytest.approx(float(data["result"]), rel=1e-3) == 0.60235


def test_ui_eval_custom_latex_with_ontology_aliases(test_client: TestClient) -> None:
    """Verify dynamic evaluation maps canonical alias inputs (runs_scored, runs_allowed)."""
    payload = {
        "formula_id": "custom",
        "latex": r"W = \frac{R_S^{1.83}}{R_S^{1.83} + R_A^{1.83}}",
        "inputs": {"runs_scored": 750, "runs_allowed": 650},
    }
    response = test_client.post("/api/eval", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    # Expected Pythagorean value for 750/650 with gamma 1.83 is ~0.5651
    assert pytest.approx(float(data["result"]), rel=1e-3) == 0.5651


def test_ui_chain_endpoint_missing_id(test_client: TestClient) -> None:
    """Verify /api/chain requires formula_id parameter."""
    response = test_client.get("/api/chain")
    assert response.status_code == 400
    assert "formula_id parameter is required" in response.json()["error"]


def test_ui_graphql_endpoint(test_client: TestClient) -> None:
    """Verify GraphQL endpoint responds to queries."""
    query = "{ concepts { name } }"
    response = test_client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "concepts" in data["data"]
    assert len(data["data"]["concepts"]) > 0


def test_ui_coverage_endpoint(test_client: TestClient) -> None:
    """Verify /api/coverage returns formula coverage report."""
    response = test_client.get("/api/coverage?limit=20")
    assert response.status_code == 200
    data = response.json()
    assert "total_formulas" in data
    assert "valid_formulas" in data
    assert "parse_yield_pct" in data
    assert "unique_symbols" in data
    assert "character_accounting" in data
    assert "error_taxonomy" in data


def test_ui_validate_endpoint(test_client: TestClient) -> None:
    """Verify /api/validate endpoint scores formulas and returns quality scorecard."""
    response = test_client.get(r"/api/validate?latex=W%20%3D%20\frac{R_S^2}{R_S^2%20%2B%20R_A^2}")
    assert response.status_code == 200
    data = response.json()
    assert "total_score" in data
    assert "letter_grade" in data
    assert "tier_scores" in data
    assert "checks" in data
    assert data["total_score"] >= 88.0
    assert data["letter_grade"] == "A"


def test_ui_formulas_endpoint_grade_filter(test_client: TestClient) -> None:
    """Verify /api/formulas supports grade filtering."""
    response_grade = test_client.get("/api/formulas?grade=A&limit=5")
    assert response_grade.status_code == 200
    assert isinstance(response_grade.json(), list)


def test_ui_formulas_endpoint_status_filter(test_client: TestClient) -> None:
    """Verify /api/formulas supports status filtering."""
    response_status = test_client.get("/api/formulas?status=passed&limit=5")
    assert response_status.status_code == 200
    assert isinstance(response_status.json(), list)


def test_ui_repair_endpoint_not_found(test_client: TestClient) -> None:
    """Verify /api/formulas/{id}/repair returns 404 for nonexistent formula."""
    response = test_client.post("/api/formulas/nonexistent-id-99999/repair")
    assert response.status_code == 404
    assert "not found" in response.json()["error"]


@pytest.mark.asyncio
async def test_ui_repair_endpoint_success() -> None:
    """Verify /api/formulas/{id}/repair repairs latex in-place and returns scorecard."""
    import uuid

    from kb.storage.database import DatabaseManager
    from kb.storage.models import Document, Formula

    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_ui_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.session_factory() as session:
        doc = Document(
            id=f"doc_{db_id}",
            citekey="test_citekey",
            title="Test Doc",
            file_path="/tmp/test.pdf",
            year=2024,
        )
        session.add(doc)
        formula = Formula(
            id=f"form_{db_id}",
            document_id=doc.id,
            citekey="test_citekey",
            raw_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
            sanitized_latex=r"W = \frac{R_S^2}{R_S^2 + R_A^2}",
            sympy_repr=None,
            symbols=[],
            is_valid=False,
            is_equality=False,
        )
        session.add(formula)
        await session.commit()

    app = create_app(db_manager=db)
    client = TestClient(app)

    res = client.post(f"/api/formulas/form_{db_id}/repair")
    assert res.status_code == 200
    data = res.json()
    assert data["formula_id"] == f"form_{db_id}"
    assert data["is_valid"] is True
    assert data["is_equality"] is True
    assert data["validation_score"] >= 88.0
    assert data["letter_grade"] == "A"
    assert "scorecard" in data
    assert "tier_scores" in data["scorecard"]
    assert data["scorecard"]["tier_scores"]["ast_roundtrip"] > 0

    await db.close()
