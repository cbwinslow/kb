"""Tests for unified logging, rotating file handlers, and timed_stage decorator."""

from __future__ import annotations

import logging
from pathlib import Path

import pytest

from kb.logging import setup_logging, timed_stage


def test_setup_logging_console_and_file(tmp_path: Path) -> None:
    log_file = tmp_path / "test_kb.log"
    logger = setup_logging(level="DEBUG", log_file=log_file, verbose=True)

    test_message = "Test log message for verification"
    logger.debug(test_message)

    # Verify log file was created and contains message
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert test_message in content
    assert "[DEBUG]" in content


def test_setup_logging_quiet() -> None:
    logger = setup_logging(quiet=True)
    assert logger.level == logging.ERROR


def test_timed_stage_sync() -> None:
    @timed_stage("sync_stage_test")
    def compute(a: int, b: int) -> int:
        return a + b

    result = compute(3, 4)
    assert result == 7


@pytest.mark.asyncio
async def test_timed_stage_async() -> None:
    @timed_stage("async_stage_test")
    async def async_compute(val: str) -> str:
        return val.upper()

    res = await async_compute("test")
    assert res == "TEST"


def test_timed_stage_exception() -> None:
    @timed_stage("failing_stage")
    def fail() -> None:
        raise ValueError("Intentional stage error")

    with pytest.raises(ValueError, match="Intentional stage error"):
        fail()
