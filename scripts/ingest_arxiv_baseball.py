"""Script to fetch and ingest fresh open-access baseball research papers from arXiv."""

from __future__ import annotations

import asyncio
import logging
from pathlib import Path

import httpx

from kb.ingest.pipeline import (
    BatchIngestionRunner,
    IngestionPipeline,
    IngestionResult,
    PaperSource,
)
from kb.storage.database import DatabaseManager

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("arxiv_ingest")

CANDIDATE_ARXIV_PAPERS = [
    {
        "id": "0911.4503",
        "title": "A Bayesian Variable Selection Approach to Major League Baseball Hitting Metrics",
        "authors": [
            "Blakeley B. McShane",
            "Alexander Braunstein",
            "James Piette",
            "Shane T. Jensen",
        ],
        "year": 2009,
    },
    {
        "id": "2207.00585",
        "title": "Predicting Ulnar Collateral Ligament Injury in Rookie MLB Pitchers",
        "authors": ["Sean A. Rendar", "Fenglong Ma"],
        "year": 2022,
    },
    {
        "id": "2601.11904",
        "title": "Structure of Pitch-Pattern Motifs in Major League Baseball",
        "authors": ["Youngjai Park", "Cheawoon Lim", "Seung-Woo Son", "Mi Jin Lee"],
        "year": 2026,
    },
    {
        "id": "2602.07030",
        "title": "Neural Sabermetrics with World Model: Predictive Modeling with LLMs",
        "authors": ["Young Jin Ahn", "Yiyang Du", "Zheyuan Zhang", "Haisen Kang"],
        "year": 2026,
    },
    {
        "id": "2303.04802",
        "title": "Estimating Ball Flight Characteristics and Spin Rate from Radar Tracking",
        "authors": ["David Kagan", "Alan M. Nathan"],
        "year": 2023,
    },
]


async def download_and_ingest_arxiv() -> int:
    download_dir = Path("data/arxiv_papers")
    download_dir.mkdir(parents=True, exist_ok=True)

    sources: list[PaperSource] = []

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as http_client:
        for p in CANDIDATE_ARXIV_PAPERS:
            arxiv_id = p["id"]
            clean_id = arxiv_id.replace(".", "_")
            citekey = f"arxiv_{clean_id}"
            pdf_path = download_dir / f"{arxiv_id}.pdf"

            if not pdf_path.exists():
                url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                logger.info("Downloading %s from %s...", arxiv_id, url)
                try:
                    resp = await http_client.get(url, headers={"User-Agent": "Mozilla/5.0"})
                    if resp.status_code == 200 and len(resp.content) > 1000:
                        pdf_path.write_bytes(resp.content)
                    else:
                        logger.warning("Failed downloading %s: HTTP %d", arxiv_id, resp.status_code)
                        continue
                except Exception as err:
                    logger.warning("Failed downloading %s: %s", arxiv_id, err)
                    continue

            sources.append(
                PaperSource(
                    pdf_path=pdf_path,
                    citekey=citekey,
                    title=p["title"],
                    authors=p["authors"],
                    year=p["year"],
                    doi=f"10.48550/arxiv.{arxiv_id}",
                    metadata={"arxiv_id": arxiv_id},
                )
            )

    logger.info("Prepared %d arXiv paper sources for ingestion.", len(sources))

    db_manager = DatabaseManager()
    await db_manager.init_db()

    pipeline = IngestionPipeline(
        db_manager=db_manager,
        fixtures_dir=Path("data/fixtures"),
    )
    runner = BatchIngestionRunner(pipeline=pipeline)

    def on_progress(res: IngestionResult) -> None:
        if res.status == "success":
            print(
                f"[INGESTED] {res.citekey:<20} in {res.duration_seconds:5.1f}s | "
                f"{res.chunk_count:3d} chunks | {res.formula_count:2d} formulas | "
                f"{res.table_count:2d} tbls | {res.title}"
            )
        elif res.status == "skipped":
            print(f"[SKIPPED]  {res.citekey:<20} | {res.reason}")
        else:
            print(f"[ERROR]    {res.citekey:<20} | {res.error}")

    stats = await runner.run(sources, on_progress=on_progress)
    print("\n" + "=" * 60)
    print("arXiv Fresh Ingestion Summary:")
    print(f"  Total scanned:         {stats.total_scanned}")
    print(f"  Successfully ingested: {stats.total_ingested}")
    print(f"  Skipped (duplicates):  {stats.total_skipped}")
    print(f"  Errors:                {stats.total_errors}")
    print(f"  Chunks created:        {stats.chunks_created}")
    print(f"  Formulas extracted:    {stats.formulas_extracted}")
    print(f"  Tables exported:       {stats.tables_extracted}")
    print("=" * 60)

    await db_manager.close()
    return 0


if __name__ == "__main__":
    asyncio.run(download_and_ingest_arxiv())
