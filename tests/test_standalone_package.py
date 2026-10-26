# pyright: reportMissingImports=false
"""Unit tests for standalone kb_formulas package."""

from __future__ import annotations

import sys
from pathlib import Path

import polars as pl

# Add packages/kb_formulas/src to sys.path
package_src = Path(__file__).parent.parent / "packages" / "kb_formulas" / "src"
if str(package_src) not in sys.path:
    sys.path.insert(0, str(package_src))


def test_standalone_package_import():
    """Verify standalone package imports cleanly without torch or database dependencies."""
    import kb_formulas

    # Verify presence of generated calculation functions
    exported_names = dir(kb_formulas)
    calc_funcs = [name for name in exported_names if name.startswith("calc_")]
    expr_funcs = [name for name in exported_names if name.startswith("expr_")]

    assert len(calc_funcs) >= 300
    assert len(expr_funcs) >= 300


def test_standalone_package_execution():
    """Verify scalar and Polars evaluation on standalone package."""
    from kb_formulas import (
        calc_val_1205_4750_1205_4,
        expr_val_1205_4750_1205_4,
    )

    # Scalar
    res = calc_val_1205_4750_1205_4(r=2.0)
    assert res == 176.0

    # Polars vectorized
    df = pl.DataFrame({"r": [1.0, 2.0, 3.0]})
    df_out = df.with_columns(out=expr_val_1205_4750_1205_4())
    assert df_out["out"].to_list() == [11.0, 176.0, 891.0]
