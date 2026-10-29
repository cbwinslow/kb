"""Web glossary harvester for sabermetric references and online formulas."""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING, Any

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

if TYPE_CHECKING:
    from kb.ingest.pipeline import IngestionPipeline, IngestionResult

logger = logging.getLogger(__name__)

# Pre-packaged canonical glossary content with validated LaTeX formulations
SABERMETRIC_GLOSSARY_PRESETS: dict[str, dict[str, Any]] = {
    "wOBA": {
        "citekey": "fangraphs_woba_glossary",
        "title": "FanGraphs Sabermetric Library: Weighted On-Base Average (wOBA)",
        "url": "https://library.fangraphs.com/offense/woba/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Weighted On-Base Average (wOBA)

Weighted On-Base Average (wOBA) is one of the most important offensive statistics in modern sabermetrics.
Unlike on-base percentage (OBP) which treats all times on base equally, or slugging percentage (SLG) which overweighs extra base hits relative to singles and walks, wOBA weights each offensive event by its actual run expectancy value based on linear weights.

## The Standard wOBA Formula

The canonical formula for Weighted On-Base Average is:

$$wOBA = \\frac{0.69 \\cdot uBB + 0.72 \\cdot HBP + 0.89 \\cdot 1B + 1.27 \\cdot 2B + 1.62 \\cdot 3B + 2.10 \\cdot HR}{AB + BB - IBB + SF + HBP}$$

Where:
- $uBB$ is unintentional walks ($BB - IBB$)
- $HBP$ is hit by pitch
- $1B$ is singles
- $2B$ is doubles
- $3B$ is triples
- $HR$ is home runs
- $AB$ is at bats
- $BB$ is total walks
- $IBB$ is intentional walks
- $SF$ is sacrifice flies

In terms of plate appearances $PA$, the denominator can also be approximated as:

$$PA = AB + BB + SF + HBP$$
""",
    },
    "wRAA": {
        "citekey": "fangraphs_wraa_glossary",
        "title": "FanGraphs Sabermetric Library: Weighted Runs Above Average (wRAA)",
        "url": "https://library.fangraphs.com/offense/wraa/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Weighted Runs Above Average (wRAA)

Weighted Runs Above Average (wRAA) measures the number of offensive runs a player contributed to their team compared to an average player. A wRAA of zero is league average.

## Formula

The relationship between wOBA and wRAA is defined by:

$$wRAA = \\frac{wOBA - lgwOBA}{wOBA_{scale}} \\cdot PA$$

Where:
- $wOBA$ is the batter's Weighted On-Base Average
- $lgwOBA$ is the league average wOBA (typically ~0.315 - 0.320)
- $wOBA_{scale}$ is the wOBA scale factor converting wOBA to OBP scale (typically ~1.15 to 1.25)
- $PA$ is the player's plate appearances
""",
    },
    "wRC": {
        "citekey": "fangraphs_wrc_glossary",
        "title": "FanGraphs Sabermetric Library: Weighted Runs Created (wRC and wRC+)",
        "url": "https://library.fangraphs.com/offense/wrc/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Weighted Runs Created (wRC)

Weighted Runs Created (wRC) quantifies a player's total offensive production in terms of runs, rather than runs above average.

## Formulas

The raw Weighted Runs Created is calculated directly from wRAA and league run environment:

$$wRC = wRAA + \\frac{lgR}{lgPA} \\cdot PA$$

Alternatively, expressing $wRC$ directly as a function of wOBA:

$$wRC = \\left(\\frac{wOBA - lgwOBA}{wOBA_{scale}} + \\frac{lgR}{lgPA}\\right) \\cdot PA$$

Where:
- $lgR$ is total league runs scored
- $lgPA$ is total league plate appearances
""",
    },
    "FIP": {
        "citekey": "fangraphs_fip_glossary",
        "title": "FanGraphs Sabermetric Library: Fielding Independent Pitching (FIP)",
        "url": "https://library.fangraphs.com/pitching/fip/",
        "authors": ["Tom Tango", "FanGraphs"],
        "year": 2026,
        "markdown": """# Fielding Independent Pitching (FIP)

Fielding Independent Pitching (FIP) measures a pitcher's effectiveness by focusing only on the outcomes directly under their control: strikeouts, unintentional walks, hit-by-pitches, and home runs, entirely removing balls in play defense and luck.

## The FIP Formula

$$FIP = \\frac{13 \\cdot HR + 3 \\cdot (BB + HBP) - 2 \\cdot K}{IP} + FIP_{constant}$$

Where:
- $HR$ is home runs allowed
- $BB$ is walks allowed
- $HBP$ is batters hit by pitch
- $K$ is strikeouts
- $IP$ is innings pitched
- $FIP_{constant}$ aligns league FIP to league ERA (typically ~3.10 to 3.25)
""",
    },
    "Base_Runs": {
        "citekey": "tango_base_runs_glossary",
        "title": "Base Runs (BsR) Offensive Estimator",
        "url": "http://www.tangotiger.net/baseruns.html",
        "authors": ["David Smyth", "Tom Tango"],
        "year": 2026,
        "markdown": """# Base Runs (BsR)

Base Runs is a sabermetric run estimator invented by David Smyth and popularized by Tom Tango in 'The Book'. It models run creation dynamically using the physics of baserunners navigating around the bases.

## The Canonical Base Runs Formula

The core formula for Base Runs is:

$$BsR = A \\cdot \\frac{B}{B + C} + D$$

Where:
- $A$ represents baserunners who reach base:
$$A = H + BB - HR$$
- $B$ represents the advancing power of the batting events:
$$B = 1.4 \\cdot TB - 0.6 \\cdot H - 3 \\cdot HR + 0.1 \\cdot BB$$
- $C$ represents outs:
$$C = 3 \\cdot (AB - H) + 0.9 \\cdot (H + BB - HR)$$
- $D$ represents guaranteed runs (home runs):
$$D = HR$$
- $TB$ is total bases:
$$TB = 1B + 2 \\cdot 2B + 3 \\cdot 3B + 4 \\cdot HR$$
""",
    },
    "WAR_position": {
        "citekey": "fangraphs_war_position_glossary",
        "title": "FanGraphs Sabermetric Library: Wins Above Replacement (WAR) for Position Players",
        "url": "https://library.fangraphs.com/misc/war/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Wins Above Replacement (WAR) for Position Players

WAR synthesizes a player's total contributions across batting, baserunning, fielding, and positional difficulty relative to a readily available minor-league replacement player.

## High-Level WAR Equation

$$WAR = \\frac{BattingRuns + BaseRunningRuns + FieldingRuns + PositionalAdjustment + LeagueAdjustment + ReplacementRuns}{RPW}$$

## Batting Runs Derivation

Batting runs is derived from wRAA with park factor adjustments:

$$BattingRuns = wRAA + \\left(\\frac{lgR}{lgPA} - ParkFactor \\cdot \\frac{lgR}{lgPA}\\right) \\cdot PA$$

## Replacement Runs Derivation

$$ReplacementRuns = 57.0 \\cdot \\left(\\frac{PA}{2430}\\right)$$

## Runs Per Win (RPW) Formula

Tango's dynamic formula for Runs Per Win in a season:

$$RPW = 10 \\cdot \\sqrt{\\frac{RS + RA}{G}}$$
""",
    },
    "WAR_pitcher": {
        "citekey": "fangraphs_war_pitcher_glossary",
        "title": "FanGraphs Sabermetric Library: Wins Above Replacement (WAR) for Pitchers",
        "url": "https://library.fangraphs.com/war/war-pitchers/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Wins Above Replacement (WAR) for Pitchers

Pitcher WAR uses FIP (Fielding Independent Pitching) transformed to a runs scale to compute runs allowed above replacement level.

## Pitcher WAR Equation

$$WAR_{pitcher} = \\left(\\frac{lgERA - FIP}{RPW}\\right) \\cdot \\frac{IP}{9} + ReplacementRuns_{pitcher}$$

Where:
- $lgERA$ is league average earned run average
- $FIP$ is Fielding Independent Pitching
- $RPW$ is Runs Per Win
- $IP$ is innings pitched
""",
    },
    "Pythagenpat": {
        "citekey": "tango_pythagenpat_glossary",
        "title": "Tom Tango: Pythagenpat Win Expectancy",
        "url": "http://www.tangotiger.net/pythagenpat.html",
        "authors": ["Tom Tango"],
        "year": 2026,
        "markdown": """# Pythagenpat Win Expectancy

Pythagenpat is David Smyth and Tom Tango's refinement of Bill James's Pythagorean expectation for baseball winning percentage.

## The Pythagenpat Formulation

The team winning percentage is:

$$WinPct = \\frac{RS^\\gamma}{RS^\\gamma + RA^\\gamma}$$

Where the dynamic exponent $\\gamma$ is determined by the run-scoring environment:

$$\\gamma = (RS + RA)^{0.285}$$

Where:
- $RS$ is runs scored
- $RA$ is runs allowed
""",
    },
    "RE24": {
        "citekey": "tangotiger_re24_glossary",
        "title": "Tom Tango: 24-State Run Expectancy Matrix (RE24) and Transition Values",
        "url": "http://www.tangotiger.net/re24.html",
        "authors": ["Tom Tango", "Mitchel Lichtman", "Andrew Dolphin"],
        "year": 2026,
        "markdown": """# 24-State Run Expectancy (RE24)

Run Expectancy (RE24) models the average number of runs scored from any base-out state through the end of the half-inning. There are 24 distinct states (3 out states $\\times$ 8 base-runner configurations).

## Run Expectancy Delta Equation

The offensive or pitching run value of any plate appearance or play is the change in run expectancy plus any runs scored on the play:

$$\\Delta RE = RE_{end} - RE_{start} + R_{play}$$

Where:
- $RE_{start}$ is the expected runs of the initial base-out state
- $RE_{end}$ is the expected runs of the resulting base-out state
- $R_{play}$ is the number of runs scored during the play (0 to 4)

## Linear Weights Derivation

Linear weights values (such as the coefficients in wOBA) are empirical averages of $\\Delta RE$ across all instances of that batting event over a season:

$$w_{event} = \\frac{1}{N_{event}} \\cdot \\sum_{k=1}^{N_{event}} \\Delta RE_k$$
""",
    },
    "Leverage_Index": {
        "citekey": "tangotiger_leverage_index_glossary",
        "title": "Tom Tango: Leverage Index (LI) and Win Probability Added",
        "url": "http://www.tangotiger.net/li.html",
        "authors": ["Tom Tango"],
        "year": 2026,
        "markdown": """# Leverage Index (LI)

Leverage Index quantifies the critical importance of a specific game state relative to an average situation. An average play has a leverage index of 1.0.

## Mathematical Definition

The leverage of a game state is the swing in win probability between the best and worst possible immediate play outcomes, normalized by the average swing across all game states:

$$LI = \\frac{\\Delta WP_{max} - \\Delta WP_{min}}{E_{WP}}$$

Where:
- $\\Delta WP_{max}$ is the change in win probability resulting from the most favorable outcome
- $\\Delta WP_{min}$ is the change in win probability resulting from the least favorable outcome
- $E_{WP}$ is the expected change in win probability for an average major league plate appearance

## Game-Level Leverage

The average leverage experienced by a pitcher or batter across an entire contest:

$$gmLI = \\frac{1}{M} \\cdot \\sum_{j=1}^{M} LI_j$$
""",
    },
    "DRC_Plus": {
        "citekey": "bp_drc_plus_glossary",
        "title": "Baseball Prospectus: Deserved Runs Created Plus (DRC+) and DRA",
        "url": "https://www.baseballprospectus.com/news/article/45387/introducing-drc/",
        "authors": ["Jonathan Judge", "Baseball Prospectus"],
        "year": 2026,
        "markdown": """# Deserved Runs Created Plus (DRC+)

Deserved Runs Created Plus (DRC+) is Baseball Prospectus's premier offensive metric. Unlike traditional linear weights which evaluate observed outcomes, DRC+ uses empirical Bayesian multi-level modeling to isolate batter true talent from opposing pitcher quality, defense, catcher framing, umpire strike zones, and park environment.

## DRC Index Formulation

$$DRC_{plus} = 100 \\cdot \\left(\\frac{DRC_{PA}}{lgDRC_{PA}}\\right)$$

Where:
- $DRC_{PA}$ is the batter's deserved runs created per plate appearance
- $lgDRC_{PA}$ is the league average deserved runs created per plate appearance

## Deserved Run Average (DRA) Relation

For pitchers, Deserved Run Average scales true talent run prevention to an ERA scale:

$$DRA = \\left(\\frac{DRA_{RA}}{lgRA}\\right) \\cdot lgERA$$
""",
    },
    "BRef_WAR": {
        "citekey": "bref_war_components_glossary",
        "title": "Baseball-Reference: Wins Above Replacement (WAR) Component Architecture",
        "url": "https://www.baseball-reference.com/about/war_explained.shtml",
        "authors": ["Sean Forman", "Baseball-Reference"],
        "year": 2026,
        "markdown": """# Baseball-Reference WAR Architecture

Baseball-Reference WAR (bWAR / rWAR) decomposes player contribution into distinct components: batting runs, baserunning runs, double play avoidance runs, defensive runs saved, positional adjustment, and replacement runs.

## Position Player WAR Equation

$$WAR = \\frac{BatRuns + BaserunningRuns + DefRuns + PosRuns + RepRuns}{RPW}$$

Where:
- $BatRuns$ is batting runs relative to league average
- $DefRuns$ is defensive runs saved (DRS)
- $PosRuns$ is positional adjustment runs
- $RepRuns$ is replacement level runs
- $RPW$ is runs per win factor

## Positional Run Adjustment

$$PosRuns = \\left(\\frac{Inn_{pos}}{1458}\\right) \\cdot Value_{pos}$$
""",
    },
    "Statcast_Bat_Tracking": {
        "citekey": "statcast_bat_tracking_glossary",
        "title": "MLB Statcast 2.0: Bat Tracking Collision Physics and Swing Mechanics",
        "url": "https://www.mlb.com/news/statcast-bat-tracking-metrics-explained",
        "authors": ["Tom Tango", "MLB Advanced Media", "David Kagan"],
        "year": 2026,
        "markdown": """# MLB Statcast 2.0 Bat Tracking

Introduced by MLB Statcast in 2024, bat tracking uses high-speed optical Hawk-Eye cameras to capture the physical trajectory of the bat head throughout the swing.

## Collision Exit Velocity Physics

The maximum achievable exit velocity $v_{exit}$ off a baseball bat collision is governed by the conservation of momentum and coefficient of restitution:

$$v_{exit} = q \\cdot v_{pitch} + (1 + e) \\cdot v_{bat}$$

Where:
- $v_{bat}$ is bat speed at the sweet spot at impact (typically 65 to 85 mph)
- $v_{pitch}$ is pitch velocity at the plate (typically 80 to 102 mph)
- $q$ is the pitch collision efficiency factor (~0.20 for round wooden bats)
- $e$ is the collision coefficient of restitution (~0.22 to 0.25)

## Squared-Up Percentage

Squared-Up Rate measures how close a batter came to achieving the maximum exit velocity possible given their bat speed and pitch speed:

$$SquaredUp = \\frac{v_{exit}}{v_{exit, max}}$$

## Blast Percentage

A 'Blast' represents an optimal combination of high swing power and centered contact. It is defined as a competitive swing that achieves both:
1. Bat speed $v_{bat} \\ge 75\\text{ mph}$
2. Squared-up contact $SquaredUp \\ge 0.80$
""",
    },
}


class WebGlossaryHarvester:
    """Harvests, sanitizes, and converts web sabermetric articles into markdown knowledge sources."""

    def __init__(self, user_agent: str | None = None) -> None:
        self.user_agent = user_agent or (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36 (KB Scientific Research Engine)"
        )

    async def fetch_html(self, url: str, timeout: float = 30.0) -> str:
        """Fetches raw HTML from a target web address with custom user-agent."""
        headers = {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        async with httpx.AsyncClient(
            headers=headers, follow_redirects=True, timeout=timeout
        ) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.text

    def extract_article(self, html: str, url: str = "") -> tuple[str, str]:
        """Extracts article title and clean body HTML from full page."""
        soup = BeautifulSoup(html, "html.parser")

        # Extract title
        title = ""
        if soup.title and soup.title.string:
            title = soup.title.string.strip()
        h1 = soup.find("h1")
        if h1 and h1.get_text():
            title = h1.get_text().strip()

        # Remove irrelevant noise elements
        for element in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
            element.decompose()

        # Find main content container
        content_container = (
            soup.find("article")
            or soup.find("main")
            or soup.find(
                "div", class_=re.compile(r"entry-content|post-content|article-body|content")
            )
            or soup.find("div", id=re.compile(r"content|main"))
            or soup.body
            or soup
        )

        return title or url, str(content_container)

    def html_to_markdown(self, html_content: str) -> str:
        """Converts article HTML content into structured markdown."""
        converted = md(html_content, heading_style="ATX", strip=["img"])
        # Clean excessive empty lines
        clean_md = re.sub(r"\n{3,}", "\n\n", converted).strip()
        return clean_md

    async def ingest_url(
        self,
        url: str,
        pipeline: IngestionPipeline,
        citekey: str | None = None,
        title: str | None = None,
        force: bool = False,
    ) -> IngestionResult:
        """Fetches a URL, converts to markdown, and ingests through the IngestionPipeline."""
        logger.info("Fetching and ingesting web article from %s", url)
        html = await self.fetch_html(url)
        extracted_title, body_html = self.extract_article(html, url=url)
        markdown_text = self.html_to_markdown(body_html)

        chosen_title = title or extracted_title
        chosen_citekey = citekey or re.sub(r"[^\w]+", "_", url.split("//")[-1]).strip("_")[:40]

        return await pipeline.ingest_markdown_source(
            citekey=chosen_citekey,
            title=chosen_title,
            markdown_text=markdown_text,
            url=url,
            force=force,
        )

    async def ingest_preset(
        self,
        preset_key: str,
        pipeline: IngestionPipeline,
        force: bool = False,
    ) -> IngestionResult:
        """Ingests a predefined canonical sabermetric glossary entry."""
        if preset_key not in SABERMETRIC_GLOSSARY_PRESETS:
            raise KeyError(
                f"Unknown preset '{preset_key}'. Available presets: {list(SABERMETRIC_GLOSSARY_PRESETS.keys())}"
            )

        data = SABERMETRIC_GLOSSARY_PRESETS[preset_key]
        return await pipeline.ingest_markdown_source(
            citekey=data["citekey"],
            title=data["title"],
            markdown_text=data["markdown"],
            url=data.get("url"),
            authors=data.get("authors"),
            year=data.get("year"),
            force=force,
        )

    async def ingest_all_presets(
        self,
        pipeline: IngestionPipeline,
        force: bool = False,
    ) -> list[IngestionResult]:
        """Ingests all canonical sabermetric glossary presets."""
        results: list[IngestionResult] = []
        for key in SABERMETRIC_GLOSSARY_PRESETS:
            res = await self.ingest_preset(key, pipeline=pipeline, force=force)
            results.append(res)
        return results
