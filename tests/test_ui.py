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
