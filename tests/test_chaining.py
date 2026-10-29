"""Hermetic unit tests for symbolic equation chaining, recursive substitution, and system solving."""

from __future__ import annotations

import uuid

import pytest

from kb.math.chaining import FormulaChainingEngine
from kb.math.extractor import FormulaExtractor
from kb.storage.database import DatabaseManager
from kb.storage.models import Document, Formula


@pytest.mark.asyncio
async def test_formula_chaining_recursive_substitution() -> None:
    """Verifies that FormulaChainingEngine recursively substitutes sub-equations into closed form."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_chain_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    extractor = FormulaExtractor()

    # Hierarchy of component formulas:
    # 1. W = B / R (e.g. WAR = BattingRuns / RPW)
    # 2. B = w + 5 (e.g. BattingRuns = wRAA + 5)
    # 3. w = o * P (e.g. wRAA = wOBA * PA)
    # 4. o = (0.7 * b + 0.9 * h) / P (e.g. wOBA)
    # 5. R = 10 (e.g. RPW)
    raw_formulas = [
        ("form_w", "test_citekey", r"W = \frac{B}{R}", "W"),
        ("form_b", "test_citekey", r"B = w + 5", "B"),
        ("form_wraa", "test_citekey", r"w = o \cdot P", "w"),
        ("form_woba", "test_citekey", r"o = \frac{0.7 \cdot b + 0.9 \cdot h}{P}", "o"),
        ("form_r", "test_citekey", r"R = 10", "R"),
    ]

    async with db.get_session() as session:
        doc = Document(id="test_citekey", citekey="test_citekey", title="Test Chaining")
        session.add(doc)
        await session.flush()

        for fid, citekey, latex, lhs in raw_formulas:
            ext = extractor.parse_latex_string(latex, formula_id=fid)
            f_record = Formula(
                id=fid,
                document_id=doc.id,
                citekey=citekey,
                raw_latex=ext.raw_latex,
                sanitized_latex=ext.sanitized_latex,
                sympy_repr=str(ext.sympy_expr) if ext.sympy_expr is not None else None,
                symbols=ext.symbols,
                is_valid=ext.is_valid,
                is_equality=ext.is_equality,
                lhs=ext.lhs or lhs,
                rhs=ext.rhs,
            )
            session.add(f_record)
        await session.commit()

    engine = FormulaChainingEngine(db_manager=db)
    result = await engine.chain_formula(formula_id="form_w", max_depth=5)

    assert result.target_formula_id == "form_w"
    assert len(result.trace_steps) >= 3

    # Check that component variables were substituted
    substituted_vars = [s.target_variable for s in result.trace_steps]
    assert "B" in substituted_vars
    assert "w" in substituted_vars
    assert "o" in substituted_vars

    # The primitive symbols should now be fundamental variables (b, h) and constants
    assert "b" in result.primitive_symbols or "h" in result.primitive_symbols
    assert "B" not in result.primitive_symbols
    assert "w" not in result.primitive_symbols
    assert "o" not in result.primitive_symbols
    assert "BattingRuns" not in result.primitive_symbols
    assert "wRAA" not in result.primitive_symbols
    assert "wOBA" not in result.primitive_symbols

    # Polars code should be generated
    assert result.polars_code != ""
    assert "pl.col" in result.polars_code

    await db.close()


@pytest.mark.asyncio
async def test_formula_chaining_cycle_prevention() -> None:
    """Verifies that circular formula definitions terminate cleanly without infinite loop."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_cycle_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    extractor = FormulaExtractor()

    # Mutual dependency: A = B + 1, B = A + 1
    raw_formulas = [
        ("form_a", "test_citekey", r"A = B + 1", "A"),
        ("form_b", "test_citekey", r"B = A + 1", "B"),
    ]

    async with db.get_session() as session:
        doc = Document(id="test_citekey", citekey="test_citekey", title="Test Cycle")
        session.add(doc)
        await session.flush()

        for fid, citekey, latex, lhs in raw_formulas:
            ext = extractor.parse_latex_string(latex, formula_id=fid)
            f_record = Formula(
                id=fid,
                document_id=doc.id,
                citekey=citekey,
                raw_latex=ext.raw_latex,
                sanitized_latex=ext.sanitized_latex,
                sympy_repr=str(ext.sympy_expr) if ext.sympy_expr is not None else None,
                symbols=ext.symbols,
                is_valid=ext.is_valid,
                is_equality=ext.is_equality,
                lhs=ext.lhs or lhs,
                rhs=ext.rhs,
            )
            session.add(f_record)
        await session.commit()

    engine = FormulaChainingEngine(db_manager=db)
    # Should terminate safely and record at most 1 or 2 substitution steps without recursion error
    result = await engine.chain_formula(formula_id="form_a", max_depth=5)
    assert result.target_formula_id == "form_a"
    assert len(result.trace_steps) <= 2
    await db.close()


@pytest.mark.asyncio
async def test_solve_system_of_equations() -> None:
    """Verifies solving simultaneous equations for unknown target parameters."""
    db_id = uuid.uuid4().hex
    url = f"sqlite+aiosqlite:///file:memdb_solve_{db_id}?mode=memory&cache=shared&uri=true"
    db = DatabaseManager(database_url=url, echo=False)
    await db.init_db()

    extractor = FormulaExtractor()

    # Equation 1: RD = RS - RA
    # Equation 2: W = RS + RA
    raw_formulas = [
        ("form_rd", "test_citekey", r"RD = RS - RA", "RD"),
        ("form_w", "test_citekey", r"W = RS + RA", "W"),
    ]

    async with db.get_session() as session:
        doc = Document(id="test_citekey", citekey="test_citekey", title="Test Solve")
        session.add(doc)
        await session.flush()

        for fid, citekey, latex, lhs in raw_formulas:
            ext = extractor.parse_latex_string(latex, formula_id=fid)
            f_record = Formula(
                id=fid,
                document_id=doc.id,
                citekey=citekey,
                raw_latex=ext.raw_latex,
                sanitized_latex=ext.sanitized_latex,
                sympy_repr=str(ext.sympy_expr) if ext.sympy_expr is not None else None,
                symbols=ext.symbols,
                is_valid=ext.is_valid,
                is_equality=ext.is_equality,
                lhs=ext.lhs or lhs,
                rhs=ext.rhs,
            )
            session.add(f_record)
        await session.commit()

    engine = FormulaChainingEngine(db_manager=db)
    # Solve for RS and RA in terms of W and RD
    solutions = await engine.solve_system(
        formula_ids=["form_rd", "form_w"],
        target_symbols=["RS", "RA"],
    )

    assert "RS" in solutions
    assert "RA" in solutions
    # Solution should contain input variables W, R, D
    assert "W" in solutions["RS"]
    assert "W" in solutions["RA"]

    await db.close()
