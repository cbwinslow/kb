"""Hermetic unit tests for web glossary harvester and markdown pipeline ingestion."""

from __future__ import annotations

import uuid

import pytest
from sqlalchemy import select

from kb.ingest.pipeline import IngestionPipeline
from kb.storage.database import DatabaseManager
from kb.storage.embeddings import MockEmbeddingGenerator
from kb.storage.models import Chunk, Document, Formula
from kb.sync.web import SABERMETRIC_GLOSSARY_PRESETS, WebGlossaryHarvester


def test_web_harvester_html_to_markdown() -> None:
    """Verifies that WebGlossaryHarvester cleans HTML and converts to structured markdown."""
    harvester = WebGlossaryHarvester()
    sample_html = """
    <html>
      <head><title>FanGraphs Sabermetric Library - wOBA</title></head>
      <body>
        <nav><a href="/">Home</a><a href="/leaders">Leaders</a></nav>
        <article class="entry-content">
          <h1>Weighted On-Base Average (wOBA)</h1>
          <p>Weighted On-Base Average measures overall offensive value.</p>
          <p>The standard formula is:</p>
          <p>$$wOBA = \\frac{0.69 \\cdot uBB + 0.72 \\cdot HBP + 0.89 \\cdot 1B + 1.27 \\cdot 2B}{PA}$$</p>
        </article>
        <footer><p>&copy; 2026 FanGraphs</p></footer>
      </body>
    </html>
    """
    title, body_html = harvester.extract_article(
        sample_html, url="https://library.fangraphs.com/offense/woba/"
    )
    assert "Weighted On-Base Average" in title
    assert "<nav>" not in body_html
    assert "<footer>" not in body_html

    markdown = harvester.html_to_markdown(body_html)
    assert "# Weighted On-Base Average (wOBA)" in markdown
    assert (
        r"$$wOBA = \frac{0.69 \cdot uBB + 0.72 \cdot HBP + 0.89 \cdot 1B + 1.27 \cdot 2B}{PA}$$"
        in markdown
    )


@pytest.mark.asyncio
async def test_ingest_markdown_source_and_deduplication() -> None:
    """Verifies that markdown content is chunked, formulas are extracted, and saved to DB."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_web_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    embedder = MockEmbeddingGenerator(dimension=1024)
    pipeline = IngestionPipeline(db_manager=db, embedder=embedder)

    md_text = """# Pythagorean Expectation

Bill James created the Pythagorean expectation for baseball.

## Mathematical Formula

The winning percentage is given by:

$$WinPct = \\frac{RS^2}{RS^2 + RA^2}$$

Where:
- $RS$ is runs scored
- $RA$ is runs allowed
"""

    res1 = await pipeline.ingest_markdown_source(
        citekey="james_pythag_test",
        title="Pythagorean Expectation",
        markdown_text=md_text,
        url="http://test.example.com/pythag",
    )

    assert res1.status == "success"
    assert res1.chunk_count >= 1
    assert res1.formula_count >= 1

    # Verify records in database
    async with db.get_session() as session:
        doc = (
            await session.execute(select(Document).where(Document.citekey == "james_pythag_test"))
        ).scalar_one()
        assert doc.title == "Pythagorean Expectation"

        chunks = list(
            (await session.execute(select(Chunk).where(Chunk.citekey == "james_pythag_test")))
            .scalars()
            .all()
        )
        assert len(chunks) == res1.chunk_count

        formulas = list(
            (await session.execute(select(Formula).where(Formula.citekey == "james_pythag_test")))
            .scalars()
            .all()
        )
        assert len(formulas) >= 1
        valid_eqs = [f for f in formulas if f.is_valid and f.is_equality]
        assert len(valid_eqs) >= 1

    # Deduplication test
    res2 = await pipeline.ingest_markdown_source(
        citekey="james_pythag_test",
        title="Pythagorean Expectation",
        markdown_text=md_text,
        force=False,
    )
    assert res2.status == "skipped"
    await db.close()


@pytest.mark.asyncio
async def test_ingest_preset_canonical_formulas() -> None:
    """Verifies that pre-bundled canonical glossary presets ingest with valid formulas."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_preset_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    embedder = MockEmbeddingGenerator(dimension=1024)
    pipeline = IngestionPipeline(db_manager=db, embedder=embedder)
    harvester = WebGlossaryHarvester()

    assert "wOBA" in SABERMETRIC_GLOSSARY_PRESETS
    res = await harvester.ingest_preset("wOBA", pipeline=pipeline)
    assert res.status == "success"
    assert res.formula_count >= 1

    async with db.get_session() as session:
        formulas = list(
            (
                await session.execute(
                    select(Formula).where(Formula.citekey == "fangraphs_woba_glossary")
                )
            )
            .scalars()
            .all()
        )
        assert len(formulas) >= 1
        woba_form = [
            f
            for f in formulas
            if f.is_valid and ("wOBA" in f.raw_latex or "w_{OBA}" in (f.sanitized_latex or ""))
        ]
        assert len(woba_form) >= 1
        assert woba_form[0].is_valid

    await db.close()


@pytest.mark.asyncio
async def test_ingest_statcast_and_re24_presets() -> None:
    """Verifies that Statcast bat tracking and Tom Tango RE24 presets ingest valid formulas."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_statcast_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    embedder = MockEmbeddingGenerator(dimension=1024)
    pipeline = IngestionPipeline(db_manager=db, embedder=embedder)
    harvester = WebGlossaryHarvester()

    assert "RE24" in SABERMETRIC_GLOSSARY_PRESETS
    assert "Statcast_Bat_Tracking" in SABERMETRIC_GLOSSARY_PRESETS

    # Ingest RE24
    res_re = await harvester.ingest_preset("RE24", pipeline=pipeline)
    assert res_re.status == "success"
    assert res_re.formula_count >= 1

    # Ingest Statcast Bat Tracking
    res_sc = await harvester.ingest_preset("Statcast_Bat_Tracking", pipeline=pipeline)
    assert res_sc.status == "success"
    assert res_sc.formula_count >= 1

    async with db.get_session() as session:
        # Check Statcast formulas
        sc_formulas = list(
            (
                await session.execute(
                    select(Formula).where(Formula.citekey == "statcast_bat_tracking_glossary")
                )
            )
            .scalars()
            .all()
        )
        assert len(sc_formulas) >= 1
        valid_sc = [f for f in sc_formulas if f.is_valid]
        assert len(valid_sc) >= 1

    await db.close()
