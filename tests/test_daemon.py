"""Unit tests for the ContinuousHarvesterDaemon."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from kb.sync.daemon import ContinuousHarvesterDaemon


def test_daemon_initialization() -> None:
    daemon = ContinuousHarvesterDaemon(
        interval_seconds=1800.0,
        queries=["test sabermetrics query"],
        limit_per_query=3,
        enable_ssh_push=False,
    )
    assert daemon.interval_seconds == 1800.0
    assert daemon.queries == ["test sabermetrics query"]
    assert daemon.limit_per_query == 3
    assert not daemon.enable_ssh_push


@pytest.mark.asyncio
async def test_daemon_run_bounded_cycles() -> None:
    daemon = ContinuousHarvesterDaemon(
        interval_seconds=0.01,
        queries=["test query"],
        limit_per_query=1,
        enable_ssh_push=False,
    )

    with patch.object(daemon, "run_single_cycle", new_callable=AsyncMock) as mock_cycle:
        mock_cycle.return_value = {
            "ingested": 1,
            "chunks": 10,
            "formulas": 2,
            "errors": [],
        }

        await daemon.run(max_cycles=2)
        assert mock_cycle.call_count == 2
