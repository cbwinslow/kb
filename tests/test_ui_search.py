"""Unit tests for Scholarly UI Explorer endpoints and async job polling."""

from __future__ import annotations

import unittest.mock as mock
import uuid

import pytest
from starlette.testclient import TestClient

from kb.enrich.web_search import SearchResult
from kb.storage.database import DatabaseManager
from kb.ui.app import create_app


@pytest.fixture
def test_app() -> TestClient:
    """Provides a TestClient connected to an in-memory database."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_ui_{db_id}?mode=memory&cache=shared&uri=true"
    db_manager = DatabaseManager(database_url=url, echo=False)
    app = create_app(db_manager)
    return TestClient(app)


def test_search_external_missing_query(test_app: TestClient):
    """Verify 400 when query parameter is missing."""
    resp = test_app.get("/api/search/external")
    assert resp.status_code == 400
    assert "required" in resp.json()["error"]


def test_search_external_mock_results(test_app: TestClient):
    """Verify external search returns normalized result JSON."""
    mock_paper = SearchResult(
        title="Physics of Baseball Aerodynamics",
        authors=["Alan Nathan"],
        year=2023,
        abstract="Wind tunnel measurements of seam-shifted wake effects.",
        source="arxiv",
        url="https://arxiv.org/abs/2301.0001",
        pdf_url="https://arxiv.org/pdf/2301.0001.pdf",
        citation_count=15,
        doi="10.1000/arxiv.2301.0001",
        arxiv_id="2301.0001",
    )

    with mock.patch("kb.enrich.web_search.ScholarlyWebSearcher.search", return_value=[mock_paper]):
        resp = test_app.get("/api/search/external?query=baseball+aerodynamics&source=arxiv")

    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["title"] == "Physics of Baseball Aerodynamics"
    assert data[0]["source"] == "arxiv"
    assert data[0]["citation_count"] == 15
    assert data[0]["pdf_url"] == "https://arxiv.org/pdf/2301.0001.pdf"


def test_harvest_ingest_url_lifecycle(test_app: TestClient):
    """Verify job dispatch and polling status endpoint."""
    # 1. Missing URL should 400
    resp = test_app.post("/api/harvest/ingest-url", json={})
    assert resp.status_code == 400

    # 2. Valid URL dispatches job
    payload = {
        "url": "https://example.com/paper.pdf",
        "title": "Test Preprint",
        "authors": ["Test Author"],
        "year": 2024,
    }

    with (
        mock.patch("kb.ui.app.fetch_pdf_bytes", new_callable=mock.AsyncMock, return_value=b"%PDF-1.4 bytes"),
        mock.patch("kb.ingest.pipeline.IngestionPipeline") as mock_pipeline_cls,
    ):
        mock_pipeline = mock.MagicMock()
        mock_pipeline.ingest_source = mock.AsyncMock()
        mock_res = mock.MagicMock()
        mock_res.status = "success"
        mock_res.citekey = "testauthor2024"
        mock_pipeline.ingest_source.return_value = mock_res
        mock_pipeline_cls.return_value = mock_pipeline

        resp = test_app.post("/api/harvest/ingest-url", json=payload)
        assert resp.status_code == 202
        job_data = resp.json()
        assert "job_id" in job_data
        assert job_data["status"] == "queued"
        job_id = job_data["job_id"]

        # 3. Poll job status
        poll_resp = test_app.get(f"/api/harvest/jobs/{job_id}")
        assert poll_resp.status_code == 200
        polled = poll_resp.json()
        assert polled["job_id"] == job_id
        assert polled["url"] == "https://example.com/paper.pdf"

    # 4. Unknown job returns 404
    missing_resp = test_app.get("/api/harvest/jobs/job_unknown123")
    assert missing_resp.status_code == 404
