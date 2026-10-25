"""Hermetic unit tests for domain-agnostic batch pipeline and discovery."""

from __future__ import annotations

import uuid
from pathlib import Path
from typing import Any

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
