"""Automated arXiv preprint harvester daemon with deduplication and ingestion."""

from __future__ import annotations

import asyncio
import logging
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx

from kb.ingest.dedup import DuplicateResolver
from kb.ingest.pipeline import (
    BatchIngestionRunner,
    IngestionPipeline,
    PaperSource,
)
from kb.storage.database import DatabaseManager

logger = logging.getLogger(__name__)

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


@dataclass(slots=True)
class HarvestResult:
    """Metrics from a single preprint harvesting cycle."""

    scanned: int = 0
    new_found: int = 0
    ingested: int = 0
    skipped: int = 0
    failed: int = 0
    chunks_created: int = 0
    formulas_extracted: int = 0
    tables_extracted: int = 0
    details: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Convert results to dictionary."""
        return {
            "scanned": self.scanned,
            "new_found": self.new_found,
            "ingested": self.ingested,
            "skipped": self.skipped,
            "failed": self.failed,
            "chunks_created": self.chunks_created,
            "formulas_extracted": self.formulas_extracted,
            "tables_extracted": self.tables_extracted,
            "details": self.details,
        }


class PreprintHarvester:
    """Discovers, filters, downloads, and ingests relevant arXiv research preprints."""

    def __init__(
        self,
        db_manager: DatabaseManager | None = None,
        download_dir: Path | None = None,
        fixtures_dir: Path | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self.db_manager = db_manager or DatabaseManager()
        self.download_dir = download_dir or Path("data/arxiv_papers")
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.fixtures_dir = fixtures_dir or Path("data/fixtures")
        self.fixtures_dir.mkdir(parents=True, exist_ok=True)
        self._external_client = http_client
        self.dedup_resolver = DuplicateResolver(self.db_manager)

    def _clean_text(self, text: str | None) -> str:
        """Strip whitespace, linebreaks, and extra spaces."""
        if not text:
            return ""
        return " ".join(text.strip().split())

    async def query_arxiv(
        self,
        query: str,
        categories: list[str] | None = None,
        max_results: int = 15,
    ) -> list[dict[str, Any]]:
        """Query arXiv Atom API for candidate research preprints."""
        search_terms: list[str] = []
        if query:
            if " OR " in query:
                or_clauses: list[str] = []
                for subq in query.split(" OR "):
                    sub_clean = re.sub(r"[^\w\s]", "", subq).strip()
                    if sub_clean:
                        sub_terms = [
                            f'all:"{t}"'
                            for t in sub_clean.split()
                            if t.upper() not in ("OR", "AND")
                        ]
                        if sub_terms:
                            or_clauses.append(
                                f"({' AND '.join(sub_terms)})"
                                if len(sub_terms) > 1
                                else sub_terms[0]
                            )
                if or_clauses:
                    search_terms.append(f"({' OR '.join(or_clauses)})")
            else:
                clean_q = re.sub(r"[^\w\s]", "", query).strip()
                terms = [f'all:"{t}"' for t in clean_q.split() if t.upper() not in ("OR", "AND")]
                if terms:
                    search_terms.append(" AND ".join(terms))

        if categories:
            cat_filter = " OR ".join(f"cat:{c}" for c in categories)
            search_terms.append(f"({cat_filter})")

        full_query = " AND ".join(search_terms) if search_terms else 'all:"sports analytics"'
        params = {
            "search_query": full_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": str(max_results),
        }

        client = self._external_client or httpx.AsyncClient(timeout=30.0, follow_redirects=True)
        try:
            for attempt in range(4):
                try:
                    resp = await client.get(ARXIV_API_URL, params=params)
                    if resp.status_code == 429:
                        wait_sec = 4.0 * (attempt + 1)
                        logger.warning(
                            "arXiv rate-limit 429 received, sleeping %.1fs (attempt %d/4)...",
                            wait_sec,
                            attempt + 1,
                        )
                        await asyncio.sleep(wait_sec)
                        continue
                    resp.raise_for_status()
                    return self.parse_atom_feed(resp.text)
                except httpx.HTTPStatusError as exc:
                    if attempt == 3:
                        logger.error("arXiv query failed after retries: %s", exc)
                        return []
                    await asyncio.sleep(3.0)
                except Exception as exc:
                    if attempt == 3:
                        logger.error("arXiv connection error: %s", exc)
                        return []
                    await asyncio.sleep(3.0)
            return []
        finally:
            if not self._external_client:
                await client.aclose()

    def parse_atom_feed(self, xml_text: str) -> list[dict[str, Any]]:
        """Parse arXiv Atom XML response into structured paper records."""
        root = ET.fromstring(xml_text)
        entries: list[dict[str, Any]] = []

        for entry in root.findall("atom:entry", ATOM_NS):
            id_elem = entry.find("atom:id", ATOM_NS)
            if id_elem is None or not id_elem.text:
                continue

            raw_id = id_elem.text.strip()
            # Extract standard arXiv ID e.g. "http://arxiv.org/abs/2104.05678v1" -> "2104.05678"
            match = re.search(r"(\d{4}\.\d{4,5})", raw_id)
            if not match:
                continue
            arxiv_id = match.group(1)

            title_elem = entry.find("atom:title", ATOM_NS)
            title = self._clean_text(title_elem.text if title_elem is not None else "")

            summary_elem = entry.find("atom:summary", ATOM_NS)
            summary = self._clean_text(summary_elem.text if summary_elem is not None else "")

            published_elem = entry.find("atom:published", ATOM_NS)
            year: int | None = None
            if published_elem is not None and published_elem.text:
                year_match = re.search(r"(\d{4})", published_elem.text)
                if year_match:
                    year = int(year_match.group(1))

            authors: list[str] = []
            for author_elem in entry.findall("atom:author", ATOM_NS):
                name_elem = author_elem.find("atom:name", ATOM_NS)
                if name_elem is not None and name_elem.text:
                    authors.append(self._clean_text(name_elem.text))

            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            for link in entry.findall("atom:link", ATOM_NS):
                if link.get("title") == "pdf" or link.get("type") == "application/pdf":
                    pdf_url = link.get("href", pdf_url)
                    break

            entries.append(
                {
                    "arxiv_id": arxiv_id,
                    "title": title,
                    "summary": summary,
                    "year": year,
                    "authors": authors,
                    "pdf_url": pdf_url,
                }
            )

        return entries

    async def filter_existing(self, papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Filter out preprints already ingested into the database using multi-attribute deduplication."""
        if not papers:
            return []

        cands = [
            {
                "citekey": f"arxiv_{p['arxiv_id'].replace('.', '_')}",
                "arxiv_id": p.get("arxiv_id"),
                "doi": p.get("doi"),
                "title": p.get("title"),
                "authors": p.get("authors"),
                "year": p.get("year"),
                "_raw": p,
            }
            for p in papers
        ]
        new_cands, _dups = await self.dedup_resolver.filter_candidates(cands)
        return [c["_raw"] for c in new_cands]

    async def harvest(
        self,
        query: str = "baseball OR sabermetrics OR statcast",
        categories: list[str] | None = None,
        limit: int = 5,
    ) -> HarvestResult:
        """Run a single harvesting pass: discover, filter, download, and ingest new preprints."""
        result = HarvestResult()
        logger.info("Starting preprint harvest: query='%s', limit=%d", query, limit)

        # 1. Query arXiv
        all_candidates = await self.query_arxiv(
            query=query, categories=categories, max_results=limit * 3
        )
        result.scanned = len(all_candidates)

        # 2. Filter out already ingested
        new_candidates = await self.filter_existing(all_candidates)
        result.new_found = len(new_candidates)
        result.skipped = result.scanned - result.new_found

        if not new_candidates:
            result.details.append("No new un-ingested preprints found.")
            return result

        # Select top candidates up to limit
        targets = new_candidates[:limit]
        sources: list[PaperSource] = []

        client = self._external_client or httpx.AsyncClient(timeout=45.0, follow_redirects=True)
        try:
            for p in targets:
                arxiv_id = p["arxiv_id"]
                clean_id = arxiv_id.replace(".", "_")
                citekey = f"arxiv_{clean_id}"
                pdf_path = self.download_dir / f"{arxiv_id}.pdf"

                if not pdf_path.exists():
                    logger.info("Downloading preprint %s from %s...", arxiv_id, p["pdf_url"])
                    try:
                        resp = await client.get(
                            p["pdf_url"], headers={"User-Agent": "Scientific-KB-Harvester/1.0"}
                        )
                        if resp.status_code == 200 and len(resp.content) > 1000:
                            pdf_path.write_bytes(resp.content)
                        else:
                            logger.warning(
                                "Failed downloading %s: HTTP %d", arxiv_id, resp.status_code
                            )
                            result.failed += 1
                            continue
                    except Exception as err:
                        logger.warning("Download error for %s: %s", arxiv_id, err)
                        result.failed += 1
                        continue

                sources.append(
                    PaperSource(
                        pdf_path=pdf_path,
                        citekey=citekey,
                        title=p["title"],
                        authors=p["authors"],
                        year=p["year"],
                        doi=f"10.48550/arxiv.{arxiv_id}",
                        metadata={"arxiv_id": arxiv_id, "abstract": p["summary"]},
                    )
                )
        finally:
            if not self._external_client:
                await client.aclose()

        if not sources:
            result.details.append("No valid PDFs downloaded for ingestion.")
            return result

        # 3. Execute Ingestion Pipeline
        pipeline = IngestionPipeline(
            db_manager=self.db_manager,
            fixtures_dir=self.fixtures_dir,
        )
        runner = BatchIngestionRunner(pipeline=pipeline)
        stats = await runner.run(sources)

        result.ingested = stats.total_ingested
        result.failed += stats.total_errors
        result.chunks_created = stats.chunks_created
        result.formulas_extracted = stats.formulas_extracted
        result.tables_extracted = stats.tables_extracted
        result.details.append(
            f"Successfully ingested {result.ingested} preprints, extracting "
            f"{result.chunks_created} chunks, {result.formulas_extracted} formulas, "
            f"and {result.tables_extracted} benchmark tables."
        )

        return result

    async def run_daemon(
        self,
        query: str = "baseball OR sabermetrics OR statcast",
        categories: list[str] | None = None,
        interval_seconds: float = 3600.0,
        limit_per_cycle: int = 5,
        max_cycles: int | None = None,
    ) -> None:
        """Run continuous background daemon harvesting preprints at specified intervals."""
        logger.info(
            "Preprint harvester daemon started (interval=%.1fs, limit=%d).",
            interval_seconds,
            limit_per_cycle,
        )
        cycle = 0
        while max_cycles is None or cycle < max_cycles:
            cycle += 1
            logger.info("Harvester daemon cycle #%d running...", cycle)
            try:
                res = await self.harvest(query=query, categories=categories, limit=limit_per_cycle)
                logger.info(
                    "Harvester cycle #%d finished: %d scanned, %d new, %d ingested.",
                    cycle,
                    res.scanned,
                    res.new_found,
                    res.ingested,
                )
            except Exception as err:
                logger.error("Harvester cycle #%d encountered error: %s", cycle, err)

            if max_cycles is not None and cycle >= max_cycles:
                break

            await asyncio.sleep(interval_seconds)
