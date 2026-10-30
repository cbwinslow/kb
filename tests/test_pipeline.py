"""Hermetic unit tests for domain-agnostic batch pipeline and discovery."""

from __future__ import annotations

import uuid
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest
from docling_core.types.doc.document import DoclingDocument
from docling_core.types.doc.labels import DocItemLabel

from kb.ingest.chunker import DocumentChunker
from kb.ingest.parser import ParsedDocument
from kb.ingest.pipeline import (
    BatchIngestionRunner,
    DirectorySourceDiscoverer,
    IngestionPipeline,
    PaperSource,
)
from kb.storage import DatabaseManager, MockEmbeddingGenerator


class DummyParser:
    """Mock document parser returning a synthetic DoclingDocument for hermetic testing."""

    def parse_pdf(self, path: Path) -> ParsedDocument:
        doc = DoclingDocument(name=path.stem)
        doc.add_text(label=DocItemLabel.SECTION_HEADER, text="1. Methodology")
        doc.add_text(
            label=DocItemLabel.TEXT,
            text=(
                r"Given run differential $RD = RS - RA$, "
                r"expected wins are $W \approx 0.5 + 0.1 \times RD$."
            ),
        )
        return ParsedDocument(
            file_path=str(path),
            device_used="cpu",
            num_pages=1,
            document=doc,
            markdown="# 1. Methodology\nGiven run differential $RD = RS - RA$...",
            metadata={"title": f"Synthetic {path.stem}"},
        )


def test_directory_discoverer_nested_and_sidecars(tmp_path: Path) -> None:
    """Verifies that DirectorySourceDiscoverer handles nested folders, flat PDFs, and SOURCE.md."""
    # 1. Nested folder with SOURCE.md
    sub_dir = tmp_path / "1312.7158"
    sub_dir.mkdir(parents=True)
    pdf_file = sub_dir / "1312.7158.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 mock content")

    source_md = sub_dir / "SOURCE.md"
    source_md.write_text(
        "# Source: 1312.7158\n\n"
        "- **Citation**: Benjamin S. Baumer; Shane T. Jensen (2013). "
        "openWAR: An Open Source System for Evaluating Overall Player Performance. "
        "arXiv:1312.7158v3 [stat.AP].\n"
        "- **Canonical URL**: https://arxiv.org/abs/1312.7158 ; "
        "DOI https://doi.org/10.48550/arXiv.1312.7158\n",
        encoding="utf-8",
    )

    # 2. Flat PDF directly in root
    flat_pdf = tmp_path / "simple_paper.pdf"
    flat_pdf.write_bytes(b"%PDF-1.4 flat content")

    discoverer = DirectorySourceDiscoverer(tmp_path, recursive=True, parse_sidecars=True)
    sources = discoverer.discover()

    assert len(sources) == 2
    by_citekey = {s.citekey: s for s in sources}

    # Verify nested sidecar parsing
    assert "1312_7158" in by_citekey
    s_nested = by_citekey["1312_7158"]
    assert s_nested.pdf_path == pdf_file
    assert s_nested.year == 2013
    assert "openWAR" in (s_nested.title or "")
    assert s_nested.authors == ["Benjamin S. Baumer", "Shane T. Jensen"]
    assert s_nested.doi == "10.48550/arXiv.1312.7158"

    # Verify flat PDF
    assert "simple_paper" in by_citekey
    s_flat = by_citekey["simple_paper"]
    assert s_flat.pdf_path == flat_pdf
    assert s_flat.title == "simple_paper"


@pytest.mark.asyncio
async def test_batch_pipeline_ingest_and_deduplication(tmp_path: Path) -> None:
    """Verifies that IngestionPipeline executes hermetically and deduplicates existing records."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_pipe_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    pdf_path = tmp_path / "pythag.pdf"
    pdf_path.write_bytes(b"%PDF-1.4 dummy pdf")

    source = PaperSource(
        pdf_path=pdf_path,
        citekey="miller2005_test",
        title="Derivation of Pythagorean Expectation",
        authors=["Steven J. Miller"],
        year=2005,
    )

    embedder = MockEmbeddingGenerator(dimension=1024)
    dummy_parser: Any = DummyParser()
    chunker = DocumentChunker(mode="hierarchical")
    fixtures_dir = tmp_path / "fixtures"

    pipeline = IngestionPipeline(
        db_manager=db,
        embedder=embedder,
        parser=dummy_parser,
        chunker=chunker,
        fixtures_dir=fixtures_dir,
    )

    # 1. First run: Successful ingestion
    res1 = await pipeline.ingest_source(source)
    assert res1.status == "success"
    assert res1.citekey == "miller2005_test"
    assert res1.chunk_count > 0
    assert res1.formula_count > 0

    # 2. Second run without force: Skipped via deduplication
    res2 = await pipeline.ingest_source(source, force=False)
    assert res2.status == "skipped"
    assert "already exists" in (res2.reason or "")

    # 3. Third run with force=True: Overwrites successfully
    res3 = await pipeline.ingest_source(source, force=True)
    assert res3.status == "success"

    await db.close()


@pytest.mark.asyncio
async def test_batch_runner_isolated_error_resilience(tmp_path: Path) -> None:
    """Verifies that BatchIngestionRunner isolates failures and aggregates statistics."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_runner_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    valid_pdf = tmp_path / "valid.pdf"
    valid_pdf.write_bytes(b"%PDF-1.4 valid")

    missing_pdf = tmp_path / "non_existent.pdf"

    sources = [
        PaperSource(pdf_path=valid_pdf, citekey="valid_paper"),
        PaperSource(pdf_path=missing_pdf, citekey="broken_paper"),
    ]

    pipeline = IngestionPipeline(
        db_manager=db,
        embedder=MockEmbeddingGenerator(dimension=1024),
        parser=DummyParser(),  # type: ignore[arg-type]
        fixtures_dir=tmp_path / "fixtures",
    )
    runner = BatchIngestionRunner(pipeline=pipeline)

    progress_reports = []
    stats = await runner.run(sources, on_progress=lambda r: progress_reports.append(r.status))

    assert stats.total_scanned == 2
    assert stats.total_ingested == 1
    assert stats.total_errors == 1
    assert len(stats.errors) == 1
    assert stats.errors[0][0] == "broken_paper"
    assert progress_reports == ["success", "error"]

    await db.close()


@pytest.mark.asyncio
async def test_openalex_discoverer_pre_download_dedup(tmp_path: Path) -> None:
    """Verifies that OpenAlexSourceDiscoverer skips downloading PDFs for already-ingested papers."""
    from unittest.mock import MagicMock

    from kb.enrich.openalex import OpenAlexClient, OpenAlexWork
    from kb.ingest.pipeline import OpenAlexSourceDiscoverer
    from kb.storage.models import Document

    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_oa_dedup_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    async with db.get_session() as session:
        doc = Document(
            id="doc_oa_1",
            citekey="openalex_smith2023_w1111",
            title="Statistical Mechanics of Baseball Pitching",
            openalex_id="W1111",
            doi="10.1000/oa.1",
        )
        session.add(doc)
        await session.commit()

    mock_client = MagicMock(spec=OpenAlexClient)
    mock_client.base_url = "https://api.openalex.org"
    mock_client.transport = None
    mock_client.get_headers.return_value = {"User-Agent": "test"}

    work1 = OpenAlexWork(
        id="https://openalex.org/W1111",
        title="Statistical Mechanics of Baseball Pitching",
        doi="10.1000/oa.1",
        authors=["Jane Smith"],
        publication_year=2023,
        cited_by_count=42,
        pdf_url="https://example.com/pdf1.pdf",
    )
    work2 = OpenAlexWork(
        id="https://openalex.org/W2222",
        title="New Novel Study of Exit Velocity",
        doi="10.1000/oa.2",
        authors=["Bob Jones"],
        publication_year=2024,
        cited_by_count=5,
        pdf_url="https://example.com/pdf2.pdf",
    )

    def parse_side_effect(item: dict[str, Any]) -> OpenAlexWork:
        if item.get("id") == "W1111":
            return work1
        return work2

    mock_client.parse_work_json.side_effect = parse_side_effect

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "results": [{"id": "W1111"}, {"id": "W2222"}]
    }

    discoverer = OpenAlexSourceDiscoverer(
        openalex_client=mock_client,
        download_dir=tmp_path / "oa_downloads",
        db_manager=db,
    )

    pdf_download_called_urls: list[str] = []

    async def mock_get(_client: Any, url: str, **_kwargs: Any) -> MagicMock:
        if "api.openalex.org" in url:
            return mock_resp
        pdf_download_called_urls.append(url)
        mock_pdf_resp = MagicMock()
        mock_pdf_resp.status_code = 200
        mock_pdf_resp.content = b"%PDF-1.4 " + (b"A" * 1500)
        return mock_pdf_resp

    with patch("httpx.AsyncClient.get", new=mock_get):
        sources = await discoverer.discover(query="baseball", limit=10)

    # work1 should have been skipped BEFORE calling get(work1.pdf_url)
    assert len(sources) == 1
    assert sources[0].title == "New Novel Study of Exit Velocity"
    assert "https://example.com/pdf1.pdf" not in pdf_download_called_urls
    assert "https://example.com/pdf2.pdf" in pdf_download_called_urls

    await db.close()
