"""Unified structured logging, rotating file handlers, and execution timing telemetry."""

from __future__ import annotations

import functools
import inspect
import logging
import logging.handlers
import sys
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

DEFAULT_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s"
SIMPLE_LOG_FORMAT = "[%(levelname)s] %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(
    level: str = "INFO",
    log_file: Path | str | None = None,
    verbose: bool = False,
    quiet: bool = False,
) -> logging.Logger:
    """Configures root logging with console and optional rotating file handlers.

    Args:
        level: Base log level string (e.g. 'DEBUG', 'INFO', 'WARNING', 'ERROR').
        log_file: Optional file path for persistent rotating file logs.
        verbose: If True, overrides level to DEBUG with detailed formatting.
        quiet: If True, suppresses output below ERROR.

    Returns:
        The configured root logger.
    """
    if verbose:
        numeric_level = logging.DEBUG
        fmt = DEFAULT_LOG_FORMAT
    elif quiet:
        numeric_level = logging.ERROR
        fmt = SIMPLE_LOG_FORMAT
    else:
        numeric_level = getattr(logging, level.upper(), logging.INFO)
        fmt = SIMPLE_LOG_FORMAT

    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    # Remove existing handlers to avoid duplicates
    for handler in list(root_logger.handlers):
        root_logger.removeHandler(handler)

    # Console Handler
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(numeric_level)
    console_formatter = logging.Formatter(fmt, datefmt=DEFAULT_DATE_FORMAT)
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)

    # Rotating File Handler (if log_file specified)
    if log_file:
        file_path = Path(log_file)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.handlers.RotatingFileHandler(
            filename=str(file_path),
            maxBytes=10 * 1024 * 1024,  # 10 MB
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setLevel(logging.DEBUG)  # File captures detailed debug info
        file_formatter = logging.Formatter(DEFAULT_LOG_FORMAT, datefmt=DEFAULT_DATE_FORMAT)
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)

    return root_logger


def timed_stage(stage_name: str | None = None) -> Callable[[F], F]:
    """Decorator to measure and log execution duration of sync or async functions."""

    def decorator(func: F) -> F:
        name = stage_name or func.__name__
        logger = logging.getLogger(func.__module__)

        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
                start_time = time.perf_counter()
                logger.debug("Starting stage: %s", name)
                try:
                    result = await func(*args, **kwargs)
                    elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                    logger.info("Completed stage '%s' in %.2f ms", name, elapsed_ms)
                    return result
                except Exception as exc:
                    elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                    logger.error(
                        "Stage '%s' failed after %.2f ms with error: %s",
                        name,
                        elapsed_ms,
                        exc,
                        exc_info=True,
                    )
                    raise

            return async_wrapper  # type: ignore[return-value]
        else:

            @functools.wraps(func)
            def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
                start_time = time.perf_counter()
                logger.debug("Starting stage: %s", name)
                try:
                    result = func(*args, **kwargs)
                    elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                    logger.info("Completed stage '%s' in %.2f ms", name, elapsed_ms)
                    return result
                except Exception as exc:
                    elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                    logger.error(
                        "Stage '%s' failed after %.2f ms with error: %s",
                        name,
                        elapsed_ms,
                        exc,
                        exc_info=True,
                    )
                    raise

            return sync_wrapper  # type: ignore[return-value]

    return decorator
