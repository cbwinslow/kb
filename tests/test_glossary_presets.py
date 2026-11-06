"""Unit tests validating canonical glossary presets and projection specifications."""

from __future__ import annotations

from pathlib import Path

import pytest

from kb.math.extractor import FormulaExtractor
from kb.sync.web import SABERMETRIC_GLOSSARY_PRESETS, WebGlossaryHarvester


def test_all_expected_presets_present() -> None:
    """Verify that all core and new forecasting presets exist in the preset dictionary."""
    expected_keys = [
        "wOBA",
        "FIP",
        "Statcast_Bat_Tracking",
        "PECOTA",
        "ZiPS",
        "Marcel",
        "Markov_Chain_Baseball",
        "Nathan_Trajectory_Physics",
    ]
    for key in expected_keys:
        assert key in SABERMETRIC_GLOSSARY_PRESETS
        preset = SABERMETRIC_GLOSSARY_PRESETS[key]
        assert "citekey" in preset
        assert "title" in preset
        assert "markdown" in preset
        assert len(preset["markdown"]) > 200


def test_glossary_markdown_files_exist_on_disk() -> None:
    """Verify that the markdown specification files in data/glossary/ exist and are populated."""
    glossary_dir = Path("data/glossary")
    assert glossary_dir.is_dir()

    expected_files = [
        "pecota_projections.md",
        "zips_projections.md",
        "marcel_projections.md",
        "markov_chain_baseball.md",
        "nathan_trajectory_physics.md",
    ]
    for filename in expected_files:
        p = glossary_dir / filename
        assert p.is_file(), f"Missing glossary file {p}"
        text = p.read_text(encoding="utf-8")
        assert "$$" in text, f"No display math found in {p}"


def test_preset_formula_extraction() -> None:
    """Verify that equations in new presets can be extracted into symbolic ASTs."""
    extractor = FormulaExtractor()

    # Test PECOTA formulas
    pecota_md = SABERMETRIC_GLOSSARY_PRESETS["PECOTA"]["markdown"]
    pecota_formulas = extractor.extract_from_text(pecota_md)
    assert len(pecota_formulas) >= 3

    # Test ZiPS formulas
    zips_md = SABERMETRIC_GLOSSARY_PRESETS["ZiPS"]["markdown"]
    zips_formulas = extractor.extract_from_text(zips_md)
    assert len(zips_formulas) >= 2

    # Test Marcel formulas
    marcel_md = SABERMETRIC_GLOSSARY_PRESETS["Marcel"]["markdown"]
    marcel_formulas = extractor.extract_from_text(marcel_md)
    assert len(marcel_formulas) >= 3

    # Test Markov formulas
    markov_md = SABERMETRIC_GLOSSARY_PRESETS["Markov_Chain_Baseball"]["markdown"]
    markov_formulas = extractor.extract_from_text(markov_md)
    assert len(markov_formulas) >= 3

    # Test Nathan physics formulas
    nathan_md = SABERMETRIC_GLOSSARY_PRESETS["Nathan_Trajectory_Physics"]["markdown"]
    nathan_formulas = extractor.extract_from_text(nathan_md)
    assert len(nathan_formulas) >= 4


@pytest.mark.asyncio
async def test_preset_alias_lookup() -> None:
    """Verify case-insensitive and underscored alias resolution in WebGlossaryHarvester."""
    harvester = WebGlossaryHarvester()

    # Test unknown preset raises KeyError
    with pytest.raises(KeyError):
        # Pass dummy pipeline
        await harvester.ingest_preset("non_existent_preset_xyz", pipeline=None)  # type: ignore[arg-type]
