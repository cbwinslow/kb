"""High-throughput batch preprint harvesting script to scale scientific corpus."""

from __future__ import annotations

import asyncio
import contextlib
import io
import logging
import shutil
import sys
from pathlib import Path
from typing import Any

import httpx
import torch
from sqlalchemy import or_, select

from kb.config import settings
from kb.ingest.pipeline import BatchIngestionRunner, IngestionPipeline, IngestionResult, PaperSource
from kb.storage.database import DatabaseManager
from kb.storage.models import Document
from kb.sync.harvester import PreprintHarvester
from kb.sync.ssh import SSHSyncManager

# Ensure UTF-8 stdout on Windows console
if isinstance(sys.stdout, io.TextIOWrapper):
    sys.stdout.reconfigure(encoding="utf-8")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("batch_scale")

TARGET_SEARCH_QUERIES = [
    "baseball",
    "sabermetrics",
    "statcast",
    "pitch trajectory",
    "bat ball collision",
    "catcher framing",
    "umpire judgment",
    "pitching strategy",
    "spin rate aerodynamics",
    "swing kinematics",
    "run expectancy",
    "win probability sports",
    "pitch recognition",
    "defensive positioning baseball",
    "seam shifted wake",
    "exit velocity launch angle",
    "batted ball profile",
    "spin axis gyro angle",
    "expected weighted on-base average",
    "leverage index baseball",
    "pitch clock fatigue",
    "bat tracking hawkeye",
    "biomechanical pitching efficiency",
]

DISK_FREE_FLOOR_GB = 2.0  # Safe floor on C: drive


def get_free_disk_gb(path: Path) -> float:
    """Return free disk space in gigabytes."""
    _total, _used, free = shutil.disk_usage(path)
    return free / (1024**3)


async def filter_existing_preprints(
    db_manager: DatabaseManager, candidates: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Filter out preprints already ingested in PostgreSQL."""
    if not candidates:
        return []

    arxiv_ids = [c["arxiv_id"] for c in candidates]
    citekeys = [f"arxiv_{c['arxiv_id'].replace('.', '_')}" for c in candidates]

    async with db_manager.session_factory() as session:
        stmt = select(Document.arxiv_id, Document.citekey).where(
            or_(Document.arxiv_id.in_(arxiv_ids), Document.citekey.in_(citekeys))
        )
        res = await session.execute(stmt)
        existing = res.fetchall()
        existing_arxiv = {row[0] for row in existing if row[0]}
        existing_cites = {row[1] for row in existing if row[1]}

    unseen: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for c in candidates:
        aid = c["arxiv_id"]
        ck = f"arxiv_{aid.replace('.', '_')}"
        if aid not in existing_arxiv and ck not in existing_cites and aid not in seen_ids:
            unseen.append(c)
            seen_ids.add(aid)

    return unseen


async def main() -> None:
    print("=" * 78)
    print("Scientific Corpus Expansion & Preprint Harvester Runner")
    print("=" * 78)

    db_manager = DatabaseManager()
    await db_manager.init_db()
    ssh_sync = SSHSyncManager()

    download_dir = settings.pdf_download_dir
    download_dir.mkdir(parents=True, exist_ok=True)
    fixtures_dir = settings.fixtures_dir
    fixtures_dir.mkdir(parents=True, exist_ok=True)

    all_discovered: list[dict[str, Any]] = []

    print("[*] Phase 1: Querying arXiv across domain-specific queries...")
    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as http_client:
        harvester = PreprintHarvester(
            db_manager=db_manager,
            download_dir=download_dir,
            fixtures_dir=fixtures_dir,
            http_client=http_client,
        )
        for query in TARGET_SEARCH_QUERIES:
            try:
                papers = await harvester.query_arxiv(query=query, max_results=20)
                all_discovered.extend(papers)
                print(f"  [+] Query '{query:<28}': found {len(papers):2d} candidates")
                await asyncio.sleep(3.2)  # Respectful arXiv pacing policy
            except Exception as e:
                print(f"  [-] Query '{query:<28}': failed with {e}")

    # Deduplicate against database
    unseen_preprints = await filter_existing_preprints(db_manager, all_discovered)
    print("-" * 78)
    print(f"[*] Total candidates discovered: {len(all_discovered)}")
    print(f"[*] Fresh, un-ingested preprints: {len(unseen_preprints)}")
    print("=" * 78)

    if not unseen_preprints:
        print("[*] All preprints are already ingested in the database!")
        await db_manager.close()
        return

    # Ingestion Pipeline Setup
    pipeline = IngestionPipeline(
        db_manager=db_manager,
        fixtures_dir=fixtures_dir,
    )
    runner = BatchIngestionRunner(pipeline=pipeline)

    total_ingested = 0
    total_chunks = 0
    total_formulas = 0
    total_tables = 0
    batch_size = 5

    async with httpx.AsyncClient(timeout=45.0, follow_redirects=True) as download_client:
        # Process in batches of 5 to protect host memory and disk
        for i in range(0, len(unseen_preprints), batch_size):
            batch = unseen_preprints[i : i + batch_size]
            sources: list[PaperSource] = []

            # Check disk space
            free_gb = get_free_disk_gb(Path("C:/"))
            if free_gb < DISK_FREE_FLOOR_GB:
                print(
                    f"[!] Warning: Low disk space on C: ({free_gb:.2f} GB free). Aborting further downloads."
                )
                break

            print(
                f"\n[*] Processing Batch {i // batch_size + 1} ({len(batch)} papers) | Disk free: {free_gb:.2f} GB"
            )

            for p in batch:
                arxiv_id = p["arxiv_id"]
                clean_id = arxiv_id.replace(".", "_")
                citekey = f"arxiv_{clean_id}"
                pdf_path = download_dir / f"{arxiv_id}.pdf"

                if not pdf_path.exists():
                    try:
                        resp = await download_client.get(
                            p["pdf_url"], headers={"User-Agent": "Scientific-KB-Batch/1.0"}
                        )
                        if resp.status_code == 200 and len(resp.content) > 1000:
                            pdf_path.write_bytes(resp.content)
                        else:
                            print(f"  [-] Download failed for {arxiv_id} (HTTP {resp.status_code})")
                            continue
                    except Exception as err:
                        print(f"  [-] Download error for {arxiv_id}: {err}")
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

            if not sources:
                continue

            def on_progress(res: IngestionResult) -> None:
                title_preview = (res.title or "Untitled")[:45]
                if res.status == "success":
                    print(
                        f"  [+] {res.citekey:<22} in {res.duration_seconds:4.1f}s | "
                        f"{res.chunk_count:2d} chunks | {res.formula_count:2d} forms | "
                        f"{res.table_count:2d} tbls | {title_preview}"
                    )
                elif res.status == "skipped":
                    print(f"  [~] {res.citekey:<22} | SKIPPED: {res.reason}")
                else:
                    print(f"  [x] {res.citekey:<22} | ERROR: {res.error}")

            # Run batch ingestion
            stats = await runner.run(sources, on_progress=on_progress)
            total_ingested += stats.total_ingested
            total_chunks += stats.chunks_created
            total_formulas += stats.formulas_extracted
            total_tables += stats.tables_extracted

            # Free GPU cache and prune temporary PDF downloads if disk starts dipping
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            # Archive raw preprints to remote homelab vault and clean up local workstation disk
            for s in sources:
                if s.pdf_path and s.pdf_path.exists():
                    if ssh_sync.is_configured:
                        ssh_sync.upload_pdf(s.pdf_path)
                    with contextlib.suppress(Exception):
                        s.pdf_path.unlink()

    if ssh_sync.is_configured:
        print("[*] Syncing updated fixture tree to homelab storage vault...")
        synced_fixtures = ssh_sync.upload_fixture_tree(settings.fixtures_dir)
        print(f"[*] Archived {synced_fixtures} fixture files to {ssh_sync.remote_fixtures_dir}")

    print("\n" + "=" * 78)
    print("Corpus Expansion Harvesting Completed")
    print("=" * 78)
    print(f"  Preprints Ingested:    {total_ingested}")
    print(f"  Chunks Created:        {total_chunks}")
    print(f"  Formulas Extracted:    {total_formulas}")
    print(f"  Benchmark Tables:      {total_tables}")
    print(f"  Final Drive C: Free:   {get_free_disk_gb(Path('C:/')):.2f} GB")
    print("=" * 78)

    await db_manager.close()


if __name__ == "__main__":
    asyncio.run(main())
