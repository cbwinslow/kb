"""Unit tests for PreprintHarvester."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from kb.sync.harvester import PreprintHarvester

SAMPLE_ATOM_FEED = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title type="text">arXiv Query: search_query=baseball</title>
  <id>http://arxiv.org/api/feed</id>
  <entry>
    <id>http://arxiv.org/abs/2401.12345v1</id>
    <published>2024-01-15T12:00:00Z</published>
    <title> Hierarchical Bayesian Modeling of Baseball Pitch Patterns </title>
    <summary> We propose a new Bayesian framework for pitch trajectory estimation. </summary>
    <author><name>Jane Doe</name></author>
    <author><name>John Smith</name></author>
    <link title="pdf" href="http://arxiv.org/pdf/2401.12345v1" type="application/pdf"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2305.67890v2</id>
    <published>2023-05-20T08:00:00Z</published>
    <title> Physics of the Sweeper Breaking Ball in Major League Baseball </title>
    <summary> Aerodynamic analysis of wake-effects and spin rate. </summary>
    <author><name>Alan Nathan</name></author>
    <link title="pdf" href="http://arxiv.org/pdf/2305.67890v2" type="application/pdf"/>
  </entry>
</feed>
"""


def test_parse_atom_feed() -> None:
    harvester = PreprintHarvester()
    entries = harvester.parse_atom_feed(SAMPLE_ATOM_FEED)

    assert len(entries) == 2
    assert entries[0]["arxiv_id"] == "2401.12345"
    assert entries[0]["title"] == "Hierarchical Bayesian Modeling of Baseball Pitch Patterns"
    assert entries[0]["year"] == 2024
    assert entries[0]["authors"] == ["Jane Doe", "John Smith"]
    assert "pdf" in entries[0]["pdf_url"]

    assert entries[1]["arxiv_id"] == "2305.67890"
    assert entries[1]["year"] == 2023
    assert entries[1]["authors"] == ["Alan Nathan"]


@pytest.mark.asyncio
async def test_filter_existing() -> None:
    mock_db = MagicMock()
    mock_session = AsyncMock()
    # In SQLAlchemy async session, session.execute() returns a synchronous Result/CursorResult
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [("2305.67890", "arxiv_2305_67890")]
    mock_session.execute.return_value = mock_result
    mock_db.session_factory.return_value.__aenter__.return_value = mock_session

    harvester = PreprintHarvester(db_manager=mock_db)
    papers = [
        {"arxiv_id": "2401.12345", "title": "Paper 1"},
        {"arxiv_id": "2305.67890", "title": "Paper 2"},
    ]

    new_papers = await harvester.filter_existing(papers)
    assert len(new_papers) == 1
    assert new_papers[0]["arxiv_id"] == "2401.12345"


@pytest.mark.asyncio
async def test_harvest_cycle_no_new(tmp_path: Path) -> None:
    harvester = PreprintHarvester(download_dir=tmp_path / "papers", fixtures_dir=tmp_path / "fixtures")
    # Mock query_arxiv to return 1 paper and filter_existing to return 0
    with (
        patch.object(harvester, "query_arxiv", new=AsyncMock(return_value=[{"arxiv_id": "1234.5678"}])),
        patch.object(harvester, "filter_existing", new=AsyncMock(return_value=[])),
    ):
        result = await harvester.harvest(query="test", limit=5)
        assert result.scanned == 1
        assert result.new_found == 0
        assert result.ingested == 0
        assert result.skipped == 1
