"""Batch ingest new canonical presets into PostgreSQL with BGE-M3 embeddings."""

from __future__ import annotations

import asyncio

from kb.ingest.pipeline import IngestionPipeline
from kb.storage.database import DatabaseManager
from kb.sync.web import WebGlossaryHarvester


async def main() -> None:
    presets = [
        "ZiPS",
        "Marcel",
        "Markov_Chain_Baseball",
        "Nathan_Trajectory_Physics",
    ]
    manager = DatabaseManager()
    await manager.init_db()
    pipeline = IngestionPipeline(db_manager=manager)
    harvester = WebGlossaryHarvester()

    print(f"[*] Ingesting {len(presets)} new presets in a single session...")
    for p in presets:
        print(f"--> Ingesting preset: {p}")
        res = await harvester.ingest_preset(p, pipeline=pipeline, force=True)
        print(f"    [{res.status.upper()}] {res.citekey}: {res.formula_count} formulas, {res.chunk_count} chunks")

    await manager.close()
    print("[*] All 4 new presets successfully ingested!")

if __name__ == "__main__":
    asyncio.run(main())
