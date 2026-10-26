"""Continuous multi-source research paper harvester daemon with automatic homelab archival."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from kb.enrich.openalex import OpenAlexClient
from kb.ingest.pipeline import (
    BatchIngestionRunner,
    IngestionPipeline,
    OpenAlexSourceDiscoverer,
)
from kb.logging import timed_stage
from kb.storage.database import DatabaseManager
from kb.sync.harvester import PreprintHarvester
from kb.sync.ssh import SSHStorageSync

logger = logging.getLogger(__name__)

DEFAULT_DAEMON_QUERIES = [
    "baseball sabermetrics expected run value",
    "baseball aerodynamics drag spin trajectory",
    "major league baseball statcast metrics",
    "pitch sequencing game theory sabermetrics",
]


class ContinuousHarvesterDaemon:
    """Continuously harvests research papers across OpenAlex and arXiv, syncing to homelab storage."""

    def __init__(
        self,
        db_manager: DatabaseManager | None = None,
        ssh_sync: SSHStorageSync | None = None,
        download_dir: Path | str = "data/daemon_downloads",
        queries: Sequence[str] | None = None,
        limit_per_query: int = 5,
        interval_seconds: float = 3600.0,
        enable_ssh_push: bool = True,
    ) -> None:
        self.manager = db_manager or DatabaseManager()
        self.ssh_sync = ssh_sync or SSHStorageSync()
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.queries = list(queries or DEFAULT_DAEMON_QUERIES)
        self.limit_per_query = limit_per_query
        self.interval_seconds = interval_seconds
        self.enable_ssh_push = enable_ssh_push

    @timed_stage("daemon_harvest_cycle")
    async def run_single_cycle(self) -> dict[str, Any]:
        """Executes one discovery, ingestion, and homelab archival cycle."""
        logger.info("[*] Starting continuous harvester daemon cycle...")
        total_ingested = 0
        total_chunks = 0
        total_formulas = 0
        errors: list[str] = []

        # 1. Harvest Open Access papers via OpenAlex
        client = OpenAlexClient()
        pipeline = IngestionPipeline(db_manager=self.manager, openalex_client=client)
        batch_runner = BatchIngestionRunner(pipeline=pipeline)
        discoverer = OpenAlexSourceDiscoverer(openalex_client=client, download_dir=self.download_dir)

        for query in self.queries:
            logger.info("Querying OpenAlex for '%s'...", query)
            try:
                sources = await discoverer.discover(query=query, limit=self.limit_per_query)
                if sources:
                    stats = await batch_runner.run(sources, max_papers=self.limit_per_query)
                    total_ingested += stats.total_ingested
                    total_chunks += stats.chunks_created
                    total_formulas += stats.formulas_extracted

                    # Upload to homelab and unlink local file to save disk space
                    if self.enable_ssh_push:
                        for s in sources:
                            if s.pdf_path.exists():
                                try:
                                    await asyncio.to_thread(self.ssh_sync.upload_pdf, s.pdf_path)
                                    s.pdf_path.unlink(missing_ok=True)
                                except Exception as upload_err:
                                    logger.warning(
                                        "Could not sync %s to homelab: %s",
                                        s.pdf_path.name,
                                        upload_err,
                                    )

            except Exception as err:
                logger.error("Error processing query '%s': %s", query, err)
                errors.append(f"{query}: {err}")

            # Sleep between queries to respect repository rate limits
            await asyncio.sleep(3.0)

        # 2. Harvest preprints via arXiv
        try:
            harvester = PreprintHarvester(
                db_manager=self.manager,
                download_dir=self.download_dir,
            )
            arxiv_res = await harvester.harvest(
                query="baseball OR sabermetrics OR statcast",
                limit=self.limit_per_query,
            )
            total_ingested += arxiv_res.ingested
            total_chunks += arxiv_res.chunks_created
            total_formulas += arxiv_res.formulas_extracted

            if self.enable_ssh_push:
                for pdf_file in self.download_dir.glob("*.pdf"):
                    try:
                        await asyncio.to_thread(self.ssh_sync.upload_pdf, pdf_file)
                        pdf_file.unlink(missing_ok=True)
                    except Exception as upload_err:
                        logger.warning(
                            "Could not sync %s to homelab: %s", pdf_file.name, upload_err
                        )

        except Exception as err:
            logger.error("Error during arXiv harvest cycle: %s", err)
            errors.append(f"arxiv: {err}")

        logger.info(
            "Cycle completed: Ingested %d papers, %d chunks, %d formulas (Errors: %d).",
            total_ingested,
            total_chunks,
            total_formulas,
            len(errors),
        )

        return {
            "ingested": total_ingested,
            "chunks": total_chunks,
            "formulas": total_formulas,
            "errors": errors,
        }

    async def run(self, max_cycles: int | None = None) -> None:
        """Runs the continuous harvesting loop indefinitely or for max_cycles."""
        logger.info(
            "Starting ContinuousHarvesterDaemon (interval=%.1fs, queries=%d)...",
            self.interval_seconds,
            len(self.queries),
        )
        cycles = 0
        while max_cycles is None or cycles < max_cycles:
            cycles += 1
            logger.info("Starting daemon cycle #%d...", cycles)
            try:
                await self.run_single_cycle()
            except Exception as err:
                logger.error("Unhandled error in daemon cycle #%d: %s", cycles, err, exc_info=True)

            if max_cycles is not None and cycles >= max_cycles:
                logger.info("Reached maximum cycles (%d). Stopping daemon.", max_cycles)
                break

            logger.info("Daemon sleeping for %.1f seconds...", self.interval_seconds)
            await asyncio.sleep(self.interval_seconds)
