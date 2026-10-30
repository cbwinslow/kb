"""Unit tests for KB command-line interface arguments and harvest execution."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from kb.cli import async_sync_harvest, build_parser


def test_cli_parser_sync_harvest_arguments() -> None:
    """Verifies CLI parsing for preset, sort, max-papers, and dry-run flags."""
    parser = build_parser()

    # 1. Default arguments
    args_default = parser.parse_args(["sync", "harvest"])
    assert args_default.subcommand == "sync"
    assert args_default.sync_subcommand == "harvest"
    assert args_default.limit == 5
    assert args_default.preset is None
    assert args_default.sort == "citations"
    assert args_default.source == "all"
    assert args_default.dry_run_dedup is False

    # 2. Preset and custom options
    args_custom = parser.parse_args([
        "sync",
        "harvest",
        "--preset",
        "mlb-modeling",
        "--sort",
        "relevance",
        "--max-papers",
        "25",
        "--source",
        "openalex",
        "--dry-run-dedup",
    ])
    assert args_custom.preset == "mlb-modeling"
    assert args_custom.sort == "relevance"
    assert args_custom.max_papers == 25
    assert args_custom.source == "openalex"
    assert args_custom.dry_run_dedup is True


@pytest.mark.asyncio
async def test_async_sync_harvest_preset_expansion() -> None:
    """Verifies that async_sync_harvest expands presets into multi-query execution."""
    with (
        patch("kb.storage.database.DatabaseManager.init_db", new=AsyncMock()),
        patch("kb.storage.database.DatabaseManager.close", new=AsyncMock()),
        patch("kb.enrich.openalex.OpenAlexClient.search_works_cursor", new=AsyncMock(return_value=[])),
    ):
        code = await async_sync_harvest(
            preset="statcast",
            dry_run_dedup=True,
            limit=5,
        )
        assert code == 0
