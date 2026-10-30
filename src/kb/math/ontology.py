"""Semantic Symbol Ontology and Canonical Column Mapping.

Bridges heterogeneous mathematical notations across academic literature
(e.g., $R_S, \\text{RS}, R, r, H_R, \\text{HR}, I_P, \\text{IP}$) with canonical
concepts and empirical tabular columns (Retrosheet, Statcast, baseballpy, Lahman).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import StrEnum
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import polars as pl


class CanonicalConcept(StrEnum):
    """Canonical concept identifiers for baseball and sports analytics domain."""

    RUNS_SCORED = "runs_scored"
    RUNS_ALLOWED = "runs_allowed"
    HOME_RUNS = "home_runs"
    WALKS = "walks"
    STRIKEOUTS = "strikeouts"
    INNINGS_PITCHED = "innings_pitched"
    HITS = "hits"
    AT_BATS = "at_bats"
    PLATE_APPEARANCES = "plate_appearances"
    SINGLES = "singles"
    DOUBLES = "doubles"
    TRIPLES = "triples"
    HIT_BY_PITCH = "hit_by_pitch"
    INTENTIONAL_WALKS = "intentional_walks"
    SACRIFICE_FLIES = "sacrifice_flies"
    EARNED_RUNS = "earned_runs"
    WINS = "wins"
    LOSSES = "losses"
    GAMES = "games"
    WIN_PCT = "win_pct"
    GAMMA = "gamma"
    STOLEN_BASES = "stolen_bases"
    CAUGHT_STEALING = "caught_stealing"
    ERRORS = "errors"
    BAT_SPEED = "bat_speed"
    SWING_LENGTH = "swing_length"
    ATTACK_ANGLE = "attack_angle"
    FAST_SWING_RATE = "fast_swing_rate"
    BLAST_RATE = "blast_rate"
    SQUARED_UP_RATE = "squared_up_rate"
    EXIT_VELOCITY = "exit_velocity"
    LEVERAGE_INDEX = "leverage_index"
    RUN_EXPECTANCY = "run_expectancy"
    VELOCITY = "velocity"
    ACCELERATION = "acceleration"
    TIME = "time"
    MASS = "mass"
    FORCE = "force"
    GRAVITY = "gravity"
    AIR_DENSITY = "air_density"
    DRAG_COEFFICIENT = "drag_coefficient"
    LIFT_COEFFICIENT = "lift_coefficient"
    ANGULAR_VELOCITY = "angular_velocity"
    RADIUS_DISTANCE = "radius_distance"
    PROBABILITY = "probability"
    MEAN = "mean"
    VARIANCE_STDDEV = "variance_stddev"
    SAMPLE_SIZE = "sample_size"
    CORRELATION = "correlation"
    ENERGY = "energy"
    MOMENTUM = "momentum"


@dataclass(frozen=True)
class ConceptDefinition:
    """Definition and metadata for a canonical quantitative concept."""

    canonical_name: CanonicalConcept
    latex_repr: str
    aliases: list[str] = field(default_factory=list)
    description: str = ""
    domain: str = "baseball"


class SymbolOntology:
    """Ontology repository managing symbol definitions, aliases, and DataFrame column binding."""

    def __init__(self) -> None:
        """Initialize ontology with canonical sports analytics concepts and aliases."""
        self._concepts: dict[CanonicalConcept, ConceptDefinition] = {}
        self._alias_index: dict[str, CanonicalConcept] = {}
        self._register_default_concepts()

    @property
    def concepts(self) -> dict[CanonicalConcept, ConceptDefinition]:
        """Return the mapping of registered canonical concepts."""
        return self._concepts

    def get_concept(self, canonical: CanonicalConcept) -> ConceptDefinition | None:
        """Retrieve concept definition by CanonicalConcept enum."""
        return self._concepts.get(canonical)

    def get_concept_aliases(self, canonical: CanonicalConcept) -> list[str]:
        """Return all declared aliases for a canonical concept."""
        concept = self._concepts.get(canonical)
        return list(concept.aliases) if concept else []

    def register(self, definition: ConceptDefinition) -> None:
        """Register a new concept definition into the ontology.

        Args:
            definition: ConceptDefinition to register.
        """
        self._concepts[definition.canonical_name] = definition
        # Index canonical name itself
        self._index_alias(definition.canonical_name.value, definition.canonical_name)

        # Index all declared aliases
        for alias in definition.aliases:
            self._index_alias(alias, definition.canonical_name)

    def _index_alias(self, alias_str: str, canonical: CanonicalConcept) -> None:
        """Index raw and normalized forms of an alias pointing to a canonical concept."""
        raw_key = alias_str.strip()
        self._alias_index[raw_key] = canonical
        norm_key = self.normalize_symbol(alias_str)
        if norm_key:
            self._alias_index[norm_key] = canonical

    @staticmethod
    def normalize_symbol(symbol: str) -> str:
        """Normalize mathematical symbol representation to a clean alphanumeric identifier.

        Handles LaTeX formatting commands, curly braces, subscripts, math modes, and casing.

        Args:
            symbol: Raw symbol or LaTeX fragment (e.g. 'R_{S}', '\\text{RS}', 'H_R').

        Returns:
            Normalized lowercase token (e.g. 'rs', 'hr', 'runs_scored').
        """
        if not symbol:
            return ""

        s = str(symbol).strip()
        # Remove LaTeX math delimiters
        s = s.strip("$")

        # Handle special accent wrappers like \bar{x} -> x_bar, \hat{x} -> x_hat
        s = re.sub(r"\\(?:bar|overline)\{([^}]+)\}", r"\1_bar", s)
        s = re.sub(r"\\hat\{([^}]+)\}", r"\1_hat", s)

        # Strip standard LaTeX font and text wrappers: \text{...}, \mathrm{...}, \mathbf{...}
        s = re.sub(r"\\[a-zA-Z]+\{([^}]+)\}", r"\1", s)

        # Remove stray backslashes
        s = s.replace("\\", "")

        # Remove curly braces
        s = s.replace("{", "").replace("}", "")

        # Replace non-alphanumeric chars (except underscore) with underscore
        s = re.sub(r"[^a-zA-Z0-9_]+", "_", s)

        # Trim leading/trailing underscores and collapse multiples
        s = re.sub(r"_+", "_", s).strip("_")

        return s.lower()

    def resolve_canonical(self, symbol: str) -> CanonicalConcept | None:
        """Resolve a raw author symbol or DataFrame column to a canonical concept.

        Args:
            symbol: Variable name, column header, or LaTeX symbol string.

        Returns:
            CanonicalConcept enum member if resolved, else None.
        """
        if not symbol:
            return None

        # 1. Exact raw match
        trimmed = symbol.strip()
        if trimmed in self._alias_index:
            return self._alias_index[trimmed]

        # 2. Case-insensitive exact match
        for k, v in self._alias_index.items():
            if k.lower() == trimmed.lower():
                return v

        # 3. Normalized symbol match
        norm = self.normalize_symbol(symbol)
        if norm in self._alias_index:
            return self._alias_index[norm]

        # 4. Strip internal underscores from normalized symbol (e.g. r_s -> rs, h_r -> hr)
        collapsed = norm.replace("_", "")
        if collapsed in self._alias_index:
            return self._alias_index[collapsed]

        for k, v in self._alias_index.items():
            if k.replace("_", "").lower() == collapsed:
                return v

        return None

    def resolve_column_mapping(
        self,
        formula_symbols: list[str],
        available_columns: list[str],
    ) -> dict[str, str]:
        """Map formula argument symbols to existing DataFrame columns using ontology resolution.

        Args:
            formula_symbols: List of variable symbols required by the formula (e.g. ['R_S', 'R_A']).
            available_columns: List of columns present in the input DataFrame.

        Returns:
            Dictionary mapping formula symbol -> source column name in DataFrame.
            If a symbol cannot be mapped, it is excluded from the returned dictionary.
        """
        mapping: dict[str, str] = {}
        avail_canon_map: dict[CanonicalConcept, str] = {}

        # First pass: map available DataFrame columns to canonical concepts
        for col in available_columns:
            canon = self.resolve_canonical(col)
            if canon and canon not in avail_canon_map:
                avail_canon_map[canon] = col

        # Second pass: for each formula symbol, find the best matching available column
        for sym in formula_symbols:
            # 1. Direct column match (case-sensitive or insensitive)
            if sym in available_columns:
                mapping[sym] = sym
                continue

            direct_ci = next(
                (c for c in available_columns if c.lower() == sym.lower()),
                None,
            )
            if direct_ci:
                mapping[sym] = direct_ci
                continue

            # 2. Canonical resolution match
            sym_canon = self.resolve_canonical(sym)
            if sym_canon and sym_canon in avail_canon_map:
                mapping[sym] = avail_canon_map[sym_canon]
                continue

        return mapping

    def bind_dataframe(self, df: Any, formula_symbols: list[str]) -> Any:
        """Bind DataFrame columns to formula parameter symbols, creating aliases where needed.

        Supports both Polars and Pandas DataFrames.
        If a formula symbol already exists in `df`, it is preserved. If missing, the ontology
        finds the matching column and aliases or assigns it under the formula symbol name.

        Args:
            df: polars.DataFrame or pandas.DataFrame.
            formula_symbols: List of argument symbols expected by the formula.

        Returns:
            New or modified DataFrame with all resolved formula symbols present as columns.
        """
        # Determine columns
        if hasattr(df, "columns"):
            cols = list(df.columns)
        else:
            raise TypeError(f"Expected DataFrame with .columns attribute, got {type(df)}")

        col_mapping = self.resolve_column_mapping(formula_symbols, cols)

        # Detect Polars vs Pandas
        is_polars = hasattr(df, "with_columns")
        is_pandas = hasattr(df, "assign") and not is_polars

        if is_polars:
            import polars as pl

            exprs: list[pl.Expr] = []
            for formula_sym, source_col in col_mapping.items():
                if formula_sym not in cols:
                    exprs.append(pl.col(source_col).alias(formula_sym))
            if exprs:
                return df.with_columns(exprs)
            return df

        if is_pandas:
            assignments: dict[str, Any] = {}
            for formula_sym, source_col in col_mapping.items():
                if formula_sym not in cols:
                    assignments[formula_sym] = df[source_col]
            if assignments:
                return df.assign(**assignments)
            return df

        return df

    def _register_default_concepts(self) -> None:
        """Register the authoritative set of sabermetric and baseball concepts."""
        concepts: list[ConceptDefinition] = [
            ConceptDefinition(
                canonical_name=CanonicalConcept.RUNS_SCORED,
                latex_repr="R_S",
                aliases=[
                    "R_S",
                    "RS",
                    "R",
                    "runs",
                    "runs_scored",
                    "runs_for",
                    "Runs",
                    "RunsScored",
                    "run",
                    "r_s",
                ],
                description="Total runs scored by the team or player.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.RUNS_ALLOWED,
                latex_repr="R_A",
                aliases=[
                    "R_A",
                    "RA",
                    "runs_against",
                    "runs_allowed",
                    "RunsAllowed",
                    "ra",
                    "r_a",
                ],
                description="Total runs conceded or allowed by the team or pitcher.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.HOME_RUNS,
                latex_repr="H_R",
                aliases=[
                    "H_R",
                    "HR",
                    "hr",
                    "home_runs",
                    "homeruns",
                    "homers",
                    "HomeRuns",
                    "h_r",
                ],
                description="Home runs hit or allowed.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.WALKS,
                latex_repr="B_B",
                aliases=[
                    "B_B",
                    "BB",
                    "bb",
                    "walks",
                    "bases_on_balls",
                    "Walks",
                    "b_b",
                ],
                description="Bases on balls (walks).",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.STRIKEOUTS,
                latex_repr="K",
                aliases=[
                    "K",
                    "SO",
                    "so",
                    "k",
                    "strikeouts",
                    "strike_outs",
                    "Strikeouts",
                ],
                description="Strikeouts recorded.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.INNINGS_PITCHED,
                latex_repr="I_P",
                aliases=[
                    "I_P",
                    "IP",
                    "ip",
                    "innings",
                    "innings_pitched",
                    "InningsPitched",
                    "i_p",
                ],
                description="Innings pitched by the pitcher or team.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.HITS,
                latex_repr="H",
                aliases=[
                    "H",
                    "hits",
                    "Hits",
                    "h",
                ],
                description="Base hits.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.AT_BATS,
                latex_repr="AB",
                aliases=[
                    "AB",
                    "ab",
                    "at_bats",
                    "atbats",
                    "AtBats",
                ],
                description="At bats.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.PLATE_APPEARANCES,
                latex_repr="PA",
                aliases=[
                    "PA",
                    "pa",
                    "plate_appearances",
                    "PlateAppearances",
                ],
                description="Total plate appearances.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.SINGLES,
                latex_repr="H_1",
                aliases=[
                    "H_1",
                    "1B",
                    "single",
                    "singles",
                    "Singles",
                    "h_1",
                ],
                description="Single base hits.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.DOUBLES,
                latex_repr="H_2",
                aliases=[
                    "H_2",
                    "2B",
                    "double",
                    "doubles",
                    "Doubles",
                    "h_2",
                ],
                description="Double base hits.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.TRIPLES,
                latex_repr="H_3",
                aliases=[
                    "H_3",
                    "3B",
                    "triple",
                    "triples",
                    "Triples",
                    "h_3",
                ],
                description="Triple base hits.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.HIT_BY_PITCH,
                latex_repr="HBP",
                aliases=[
                    "HBP",
                    "hbp",
                    "hit_by_pitch",
                    "HitByPitch",
                ],
                description="Hit by pitch incidents.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.INTENTIONAL_WALKS,
                latex_repr="IBB",
                aliases=[
                    "IBB",
                    "ibb",
                    "intentional_walks",
                    "IntentionalWalks",
                ],
                description="Intentional bases on balls.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.SACRIFICE_FLIES,
                latex_repr="SF",
                aliases=[
                    "SF",
                    "sf",
                    "sacrifice_flies",
                    "SacrificeFlies",
                ],
                description="Sacrifice flies.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.EARNED_RUNS,
                latex_repr="ER",
                aliases=[
                    "ER",
                    "er",
                    "earned_runs",
                    "EarnedRuns",
                ],
                description="Earned runs charged against a pitcher or team.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.WINS,
                latex_repr="W",
                aliases=[
                    "W",
                    "wins",
                    "Wins",
                    "w",
                ],
                description="Wins recorded.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.LOSSES,
                latex_repr="L",
                aliases=[
                    "L",
                    "losses",
                    "Losses",
                    "l",
                ],
                description="Losses recorded.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.GAMES,
                latex_repr="G",
                aliases=[
                    "G",
                    "games",
                    "Games",
                    "g",
                ],
                description="Total games played.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.WIN_PCT,
                latex_repr="W_{pct}",
                aliases=[
                    "W_pct",
                    "W_{pct}",
                    "WPct",
                    "wpct",
                    "win_pct",
                    "win_percentage",
                    "WinPct",
                    "w_pct",
                ],
                description="Win percentage (wins divided by decisions or games).",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.GAMMA,
                latex_repr="\\gamma",
                aliases=[
                    "gamma",
                    "\\gamma",
                    "exp",
                    "exponent",
                    "alpha",
                    "\\alpha",
                ],
                description="Pythagorean expectation exponent parameter.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.BAT_SPEED,
                latex_repr="v_{bat}",
                aliases=["v_{bat}", "v_bat", "bat_speed", "BatSpeed", "batspeed", "vbat"],
                description="Statcast bat tracking swing speed at point of contact (mph).",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.SWING_LENGTH,
                latex_repr="l_{swing}",
                aliases=["l_{swing}", "l_swing", "swing_length", "SwingLength", "swinglength"],
                description="Distance traveled by the sweet spot of the bat from start of swing to contact (ft).",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.ATTACK_ANGLE,
                latex_repr="\\theta_{attack}",
                aliases=[
                    "\\theta_{attack}",
                    "theta_attack",
                    "attack_angle",
                    "AttackAngle",
                    "launch_angle_bat",
                ],
                description="Vertical angle of bat's path at point of contact (degrees).",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.FAST_SWING_RATE,
                latex_repr="FSR",
                aliases=["FSR", "fast_swing_rate", "FastSwingRate", "fast_swing_pct"],
                description="Percentage of competitive swings reaching 75+ mph.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.BLAST_RATE,
                latex_repr="BlastRate",
                aliases=["BlastRate", "blast_rate", "blast_pct", "BlastPct", "blasts"],
                description="Percentage of contact events combining 75+ mph bat speed with 80%+ squared-up rate.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.SQUARED_UP_RATE,
                latex_repr="SquaredUp",
                aliases=["SquaredUp", "squared_up_rate", "squared_up", "sq_up", "squared_up_pct"],
                description="Ratio of observed exit velocity to maximum physical collision exit velocity potential.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.EXIT_VELOCITY,
                latex_repr="v_{exit}",
                aliases=[
                    "v_{exit}",
                    "v_exit",
                    "EV",
                    "exit_velocity",
                    "launch_speed",
                    "ExitVelocity",
                ],
                description="Speed of the baseball off the bat upon batted ball event (mph).",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.LEVERAGE_INDEX,
                latex_repr="LI",
                aliases=["LI", "li", "leverage_index", "LeverageIndex", "pLI", "gmLI", "inLI"],
                description="Quantitative measure of the swing's win expectation importance in a game.",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.RUN_EXPECTANCY,
                latex_repr="RE",
                aliases=[
                    "RE",
                    "re",
                    "run_expectancy",
                    "RunExpectancy",
                    "RE24",
                    "\\Delta RE",
                    "delta_re",
                ],
                description="Expected runs scored from a specific base-out state through the end of the inning.",
            ),
            # Universal scientific, physical, and statistical concepts
            ConceptDefinition(
                canonical_name=CanonicalConcept.VELOCITY,
                latex_repr="v",
                aliases=[
                    "v",
                    "V",
                    "v_0",
                    "v_x",
                    "v_y",
                    "v_z",
                    "v_{0}",
                    "v_{x}",
                    "v_{y}",
                    "v_{z}",
                    "\\vec{v}",
                    "vel",
                    "velocity",
                    "speed",
                ],
                description="Linear velocity or speed vector component (m/s or mph).",
                domain="physics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.ACCELERATION,
                latex_repr="a",
                aliases=[
                    "a",
                    "A",
                    "a_x",
                    "a_y",
                    "a_z",
                    "a_{x}",
                    "a_{y}",
                    "a_{z}",
                    "\\vec{a}",
                    "accel",
                    "acceleration",
                ],
                description="Linear acceleration vector component (m/s^2).",
                domain="physics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.TIME,
                latex_repr="t",
                aliases=[
                    "t",
                    "T",
                    "\\Delta t",
                    "\\delta t",
                    "delta_t",
                    "t_0",
                    "t_{0}",
                    "t_f",
                    "t_{flight}",
                    "time",
                    "duration",
                ],
                description="Time interval or epoch timestamp (s).",
                domain="physics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.MASS,
                latex_repr="m",
                aliases=["m", "M", "m_{ball}", "m_{bat}", "m_b", "mass", "weight"],
                description="Mass of projectile, implement, or body (kg or oz).",
                domain="physics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.FORCE,
                latex_repr="F",
                aliases=[
                    "F",
                    "f",
                    "\\vec{F}",
                    "F_{drag}",
                    "F_{magnus}",
                    "F_{gravity}",
                    "F_d",
                    "F_m",
                    "F_g",
                    "force",
                ],
                description="Vector force acting on projectile or body (N or lbf).",
                domain="physics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.GRAVITY,
                latex_repr="g",
                aliases=["g", "G", "g_0", "gravity"],
                description="Standard gravitational acceleration (9.81 m/s^2 or 32.2 ft/s^2).",
                domain="physics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.AIR_DENSITY,
                latex_repr="\\rho",
                aliases=["\\rho", "rho", "\\rho_{air}", "rho_air", "air_density"],
                description="Atmospheric air density (kg/m^3).",
                domain="aerodynamics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.DRAG_COEFFICIENT,
                latex_repr="C_d",
                aliases=[
                    "C_d",
                    "c_d",
                    "C_D",
                    "c_D",
                    "C_{d}",
                    "C_{D}",
                    "drag_coef",
                    "drag_coefficient",
                ],
                description="Dimensionless aerodynamic drag coefficient.",
                domain="aerodynamics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.LIFT_COEFFICIENT,
                latex_repr="C_l",
                aliases=[
                    "C_l",
                    "c_l",
                    "C_L",
                    "c_L",
                    "C_{l}",
                    "C_{L}",
                    "lift_coef",
                    "lift_coefficient",
                ],
                description="Dimensionless aerodynamic lift / Magnus coefficient.",
                domain="aerodynamics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.ANGULAR_VELOCITY,
                latex_repr="\\omega",
                aliases=[
                    "\\omega",
                    "omega",
                    "\\vec{\\omega}",
                    "spin",
                    "spin_rate",
                    "rpm",
                    "omega_x",
                    "omega_y",
                    "omega_z",
                ],
                description="Rotational velocity or spin rate (rad/s or rpm).",
                domain="aerodynamics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.RADIUS_DISTANCE,
                latex_repr="r",
                aliases=[
                    "r",
                    "R",
                    "d",
                    "x",
                    "y",
                    "z",
                    "h",
                    "\\Delta x",
                    "\\Delta y",
                    "\\Delta z",
                    "dist",
                    "distance",
                    "radius",
                    "coord",
                ],
                description="Spatial coordinate, radius, or distance displacement (m or ft).",
                domain="geometry",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.PROBABILITY,
                latex_repr="P",
                aliases=["P", "p", "\\Pr", "Pr", "prob", "probability"],
                description="Probability measure bounded in [0, 1].",
                domain="statistics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.MEAN,
                latex_repr="\\mu",
                aliases=["\\mu", "mu", "\\bar{x}", "bar_x", "mean", "expectation"],
                description="Mathematical expectation or arithmetic mean.",
                domain="statistics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.VARIANCE_STDDEV,
                latex_repr="\\sigma",
                aliases=[
                    "\\sigma",
                    "sigma",
                    "\\sigma^2",
                    "sigma_sq",
                    "s^2",
                    "std",
                    "variance",
                    "stddev",
                    "var",
                ],
                description="Population or sample standard deviation and variance.",
                domain="statistics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.SAMPLE_SIZE,
                latex_repr="N",
                aliases=["N", "n", "sample_size", "sample_count", "num_observations"],
                description="Total sample count or discrete population size.",
                domain="statistics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.CORRELATION,
                latex_repr="r",
                aliases=[
                    "corr",
                    "correlation",
                    "r_{xy}",
                    "R^2",
                    "r_sq",
                    "r_squared",
                    "pearson_r",
                ],
                description="Correlation coefficient or coefficient of determination (R^2).",
                domain="statistics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.ENERGY,
                latex_repr="E",
                aliases=["E", "KE", "PE", "energy", "kinetic_energy"],
                description="Mechanical kinetic or potential energy (J or ft-lbf).",
                domain="physics",
            ),
            ConceptDefinition(
                canonical_name=CanonicalConcept.MOMENTUM,
                latex_repr="p",
                aliases=["p_{mom}", "momentum", "angular_momentum", "L_{ang}"],
                description="Linear or angular momentum.",
                domain="physics",
            ),
        ]

        for c in concepts:
            self.register(c)


# Global default instance
_DEFAULT_ONTOLOGY = SymbolOntology()


def get_symbol_ontology() -> SymbolOntology:
    """Return the global singleton SymbolOntology instance."""
    return _DEFAULT_ONTOLOGY


def resolve_canonical(symbol: str) -> CanonicalConcept | None:
    """Resolve a raw author symbol to its canonical concept using the default ontology."""
    return _DEFAULT_ONTOLOGY.resolve_canonical(symbol)


def map_dataframe_columns(df: Any, formula_symbols: list[str]) -> Any:
    """Bind a Polars or Pandas DataFrame to formula parameters using the default ontology."""
    return _DEFAULT_ONTOLOGY.bind_dataframe(df, formula_symbols)
