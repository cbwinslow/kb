"""In-place repair engine for previously ingested mathematical formulas in PostgreSQL."""

from __future__ import annotations

import logging
import time
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, Field
from sqlalchemy import select, update

from kb.math.extractor import ExtractedFormula, FormulaExtractor
from kb.math.sanitizer import EquationSanitizer

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)


class RepairResult(BaseModel):
    """Execution summary of an in-place formula repair migration."""

    total_scanned: int = Field(default=0, description="Total formulas examined")
    previously_valid: int = Field(default=0, description="Formulas already valid before repair")
    newly_recovered: int = Field(
        default=0, description="Formulas successfully recovered to valid ASTs"
    )
    still_invalid: int = Field(default=0, description="Formulas that remain unparsed")
    updated_records: int = Field(default=0, description="Database records updated")
    duration_seconds: float = Field(default=0.0, description="Total execution time in seconds")
    dry_run: bool = Field(default=False, description="Whether execution was a dry run")


class CorpusFormulaRepairer:
    """Repairs and re-parses stored database formulas in-place using upgraded sanitizers."""

    def __init__(
        self,
        sanitizer: EquationSanitizer | None = None,
        extractor: FormulaExtractor | None = None,
    ) -> None:
        """Initialize repairer with equation sanitizer and symbolic extractor.

        Args:
            sanitizer: Optional custom EquationSanitizer.
            extractor: Optional custom FormulaExtractor.
        """
        self.sanitizer = sanitizer or EquationSanitizer()
        self.extractor = extractor or FormulaExtractor(sanitizer=self.sanitizer)

    def repair_single(
        self,
        raw_latex: str,
        formula_id: str | None = None,
        chunk_id: str | None = None,
    ) -> ExtractedFormula:
        """Repair and re-parse a single LaTeX formula string using current sanitizer and extractor."""
        return self.extractor.parse_latex_string(
            raw_latex,
            formula_id=formula_id or "",
            chunk_id=chunk_id,
        )

    async def repair_corpus(
        self,
        batch_size: int = 250,
        dry_run: bool = False,
        only_invalid: bool = True,
        limit: int | None = None,
        session: AsyncSession | None = None,
        progress_callback: Callable[[int, int, int], None] | None = None,
    ) -> RepairResult:
        """Scan stored formulas, re-sanitize, re-parse into SymPy ASTs, and update in-place.

        Args:
            batch_size: Number of records to commit per database transaction batch.
            dry_run: If True, computes recovery statistics without persisting updates.
            only_invalid: If True, only attempts to repair formulas currently marked is_valid = False.
            limit: Optional maximum number of formulas to process.
            session: Optional AsyncSession. If omitted, uses DatabaseManager.
            progress_callback: Optional callback invoked with (processed, recovered, total).

        Returns:
            RepairResult summarizing recovery yield.
        """
        from kb.storage.database import DatabaseManager

        start_time = time.perf_counter()

        if session is not None:
            return await self._execute_repair(
                session=session,
                batch_size=batch_size,
                dry_run=dry_run,
                only_invalid=only_invalid,
                limit=limit,
                start_time=start_time,
                progress_callback=progress_callback,
            )

        db = DatabaseManager()
        async with db.get_session() as sess:
            return await self._execute_repair(
                session=sess,
                batch_size=batch_size,
                dry_run=dry_run,
                only_invalid=only_invalid,
                limit=limit,
                start_time=start_time,
                progress_callback=progress_callback,
            )

    async def _execute_repair(
        self,
        session: AsyncSession,
        batch_size: int,
        dry_run: bool,
        only_invalid: bool,
        limit: int | None,
        start_time: float,
        progress_callback: Callable[[int, int, int], None] | None,
    ) -> RepairResult:
        """Internal execution loop for processing formulas in batches."""
        from kb.storage.models import Formula

        stmt = select(Formula)
        if only_invalid:
            stmt = stmt.where(Formula.is_valid.is_(False))
        if limit:
            stmt = stmt.limit(limit)

        records = (await session.execute(stmt)).scalars().all()
        total = len(records)

        prev_valid = 0
        newly_recovered = 0
        still_invalid = 0
        updated_records = 0

        batch_updates: list[dict[str, Any]] = []

        for idx, formula in enumerate(records, start=1):
            if formula.is_valid:
                prev_valid += 1
                if only_invalid:
                    continue

            # Re-parse raw LaTeX with current extractor & sanitizer
            parsed = self.extractor.parse_latex_string(
                formula.raw_latex,
                formula_id=formula.id,
                chunk_id=formula.chunk_id,
            )

            if parsed.is_valid:
                if not formula.is_valid:
                    newly_recovered += 1
                # Prepare update payload
                sympy_repr_str = str(parsed.sympy_expr) if parsed.sympy_expr is not None else None
                update_data = {
                    "id": formula.id,
                    "sanitized_latex": parsed.sanitized_latex,
                    "sympy_repr": sympy_repr_str,
                    "symbols": parsed.symbols,
                    "is_valid": True,
                    "is_equality": parsed.is_equality,
                    "lhs": parsed.lhs,
                    "rhs": parsed.rhs,
                }
                batch_updates.append(update_data)
            else:
                still_invalid += 1
                # Update sanitized_latex even if still invalid, in case cleaner
                if parsed.sanitized_latex != formula.sanitized_latex:
                    batch_updates.append(
                        {
                            "id": formula.id,
                            "sanitized_latex": parsed.sanitized_latex,
                        }
                    )

            # Flush batch
            if len(batch_updates) >= batch_size:
                if not dry_run:
                    for item in batch_updates:
                        fid = item.pop("id")
                        await session.execute(
                            update(Formula).where(Formula.id == fid).values(**item)
                        )
                    await session.commit()
                updated_records += len(batch_updates)
                batch_updates.clear()

            if progress_callback and (idx % 100 == 0 or idx == total):
                progress_callback(idx, newly_recovered, total)

        # Flush any remaining updates
        if batch_updates:
            if not dry_run:
                for item in batch_updates:
                    fid = item.pop("id")
                    await session.execute(update(Formula).where(Formula.id == fid).values(**item))
                await session.commit()
            updated_records += len(batch_updates)
            batch_updates.clear()

        duration = time.perf_counter() - start_time
        return RepairResult(
            total_scanned=total,
            previously_valid=prev_valid,
            newly_recovered=newly_recovered,
            still_invalid=still_invalid,
            updated_records=updated_records if not dry_run else 0,
            duration_seconds=round(duration, 2),
            dry_run=dry_run,
        )
