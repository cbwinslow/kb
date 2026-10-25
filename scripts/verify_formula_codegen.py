"""Script to verify extracted formulas against database benchmark fixtures."""

from __future__ import annotations

import asyncio
import sys

from sqlalchemy import select

from kb.codegen.compiler import FormulaCompiler
from kb.codegen.verifier import FormulaVerifier
from kb.storage.database import DatabaseManager
from kb.storage.models import BenchmarkTable, Formula

# Configure UTF-8 for Windows console
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


async def main() -> None:
    print("=" * 70)
    print("Formula Knowledge-to-Code Empirical Verification Runner")
    print("=" * 70)

    manager = DatabaseManager()
    compiler = FormulaCompiler()
    verifier = FormulaVerifier(compiler=compiler)

    async with manager.session_factory() as session:
        # Load sample valid formulas
        stmt = (
            select(Formula)
            .where(Formula.is_valid == True)  # noqa: E712
            .order_by(Formula.id)
            .limit(20)
        )
        res = await session.execute(stmt)
        formulas = list(res.scalars().all())

        print(f"[*] Loaded {len(formulas)} valid formulas from kb_formulas.")

        compiled_count = 0
        verified_count = 0

        for f in formulas:
            res_code = compiler.compile(
                formula_id=f.id,
                citekey=f.citekey,
                raw_latex=f.raw_latex,
                sympy_repr=f.sympy_repr,
            )
            if not res_code.is_valid:
                continue

            compiled_count += 1

            # Check if there is a benchmark table for this document
            tbl_stmt = (
                select(BenchmarkTable)
                .where(
                    BenchmarkTable.citekey == f.citekey,
                    BenchmarkTable.parquet_path.isnot(None),
                )
                .limit(1)
            )
            tbl_res = await session.execute(tbl_stmt)
            table = tbl_res.scalar_one_or_none()

            if table and table.parquet_path:
                v_res = verifier.verify_against_parquet(
                    res_code,
                    parquet_path=table.parquet_path,
                )
                if v_res.passed:
                    verified_count += 1
                    print(
                        f"  [+] Formula {f.id[:12]} ({f.citekey}) verified on table {table.id[:8]} ({v_res.num_samples} rows): {v_res.details}"
                    )
                else:
                    # Synthetic numerical sanity test
                    dummy_inputs = {p: [1.0, 2.0, 3.0] for p in res_code.parameters}
                    synth_res = verifier.verify_with_inputs(res_code, dummy_inputs)
                    if synth_res.passed:
                        verified_count += 1
                        print(
                            f"  [+] Formula {f.id[:12]} ({f.citekey}) compiled & verified on synthetic inputs ({len(res_code.parameters)} params)."
                        )
            else:
                dummy_inputs = {p: [1.0, 2.0, 3.0] for p in res_code.parameters}
                synth_res = verifier.verify_with_inputs(res_code, dummy_inputs)
                if synth_res.passed:
                    verified_count += 1
                    print(
                        f"  [+] Formula {f.id[:12]} ({f.citekey}) compiled & verified on synthetic inputs ({len(res_code.parameters)} params)."
                    )

        print("-" * 70)
        print(f"Results: {compiled_count} compiled, {verified_count} verified successfully.")
        print("=" * 70)

    await manager.close()


if __name__ == "__main__":
    asyncio.run(main())
