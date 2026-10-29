"""LaTeX equation sanitizer for repairing OCR artifacts and formatting formulas for SymPy."""

from __future__ import annotations

import re


class EquationSanitizer:
    """Sanitizer for cleaning and normalizing LaTeX mathematical expressions."""

    # Regex patterns for cleanup
    TAG_RE = re.compile(
        r"[\s,;.]*(?:\\tag\{[^}]*\}|\([0-9]+(?:\.[0-9]+)*\)|\([A-Za-z0-9]+\.[0-9]+\))[\s,;.]*$"
    )
    LABEL_RE = re.compile(r"\\label\{[^}]*\}")
    ENV_STRIP_RE = re.compile(
        r"\\begin\{(?:equation|align|aligned|gather|displaymath)\*?\}"
        r"([\s\S]*?)"
        r"\\end\{(?:equation|align|aligned|gather|displaymath)\*?\}"
    )
    DOLLAR_STRIP_RE = re.compile(r"^\${1,2}|\${1,2}$")

    # Common multi-letter domain metric variables mapped to subscripted symbols for SymPy
    COMPOUND_SYMBOLS = [
        ("RS", "R_{S}"),
        ("RA", "R_{A}"),
        ("HR", "H_{R}"),
        ("BB", "B_{B}"),
        ("SO", "S_{O}"),
        ("IP", "I_{P}"),
        ("AB", "A_{B}"),
        ("TB", "T_{B}"),
        ("OBP", "O_{BP}"),
        ("SLG", "S_{LG}"),
        ("OPS", "O_{PS}"),
        ("FIP", "F_{IP}"),
        ("wOBA", "w_{OBA}"),
        ("WAR", "W_{AR}"),
    ]

    UNICODE_GREEK_MAP = {
        "α": r"\alpha ",
        "β": r"\beta ",
        "γ": r"\gamma ",
        "δ": r"\delta ",
        "ε": r"\epsilon ",
        "θ": r"\theta ",
        "λ": r"\lambda ",
        "µ": r"\mu ",
        "μ": r"\mu ",
        "π": r"\pi ",
        "σ": r"\sigma ",
        "τ": r"\tau ",
        "φ": r"\phi ",
        "ω": r"\omega ",
        "Γ": r"\Gamma ",
        "Δ": r"\Delta ",
        "Θ": r"\Theta ",
        "Λ": r"\Lambda ",
        "Σ": r"\Sigma ",
        "Ω": r"\Omega ",
    }

    def sanitize(self, raw_latex: str, protect_compound_symbols: bool = True) -> str:
        """Sanitize raw LaTeX string into a clean expression parseable by SymPy.

        Args:
            raw_latex: Raw LaTeX string (can include $$ delimiters, tags, or OCR glitches).
            protect_compound_symbols: If True, maps domain metrics (RS, RA, etc.) to subscripted
                symbols (R_{S}, R_{A}) so SymPy treats them as single variables rather than R*S.

        Returns:
            Cleaned LaTeX string suitable for SymPy parse_latex.
        """
        text = raw_latex.strip()

        # 1. Strip outer delimiters ($$, $, \[...\])
        if text.startswith(r"\[") and text.endswith(r"\]"):
            text = text[2:-2].strip()
        text = self.DOLLAR_STRIP_RE.sub("", text).strip()

        # 2. Extract inner content from environments like \begin{equation} ... \end{equation}
        env_match = self.ENV_STRIP_RE.search(text)
        if env_match:
            text = env_match.group(1).strip()

        # 3. Strip equation labels and tags (e.g., \tag{1}, \label{eq:1}, (1.2), (2.1))
        text = re.sub(r"\\tag\*?\{[^}]*\}", "", text).strip()
        text = self.TAG_RE.sub("", text).strip()
        text = self.LABEL_RE.sub("", text).strip()

        # 4. Normalize unicode math and Greek symbols
        for char, replacement in self.UNICODE_GREEK_MAP.items():
            text = text.replace(char, replacement)

        unicode_subs = {
            "₀": "_0",
            "₁": "_1",
            "₂": "_2",
            "₃": "_3",
            "₄": "_4",
            "₅": "_5",
            "₆": "_6",
            "₇": "_7",
            "₈": "_8",
            "₉": "_9",
        }
        for sub_char, sub_rep in unicode_subs.items():
            text = text.replace(sub_char, sub_rep)

        text = text.replace("×", r"\times ").replace("·", r"\cdot ").replace("−", "-")
        text = text.replace("≤", r"\le ").replace("≥", r"\ge ").replace("≠", r"\ne ")
        text = text.replace("∞", r"\infty ").replace("‖", "|").replace("…", r"\dots ")

        # Ensure standard math function names have backslashes if missing
        text = re.sub(
            r"(?<!\\)\b(arccos|arcsin|arctan|cos|sin|tan|log|ln|exp)\b",
            r"\\\1",
            text,
        )

        # 5. Remove OCR piecewise artifacts and trailing conditions
        text = re.sub(r"[]", "", text)
        text = re.sub(r"\\begin\{cases\}", "", text)
        text = re.sub(r"\\end\{cases\}", "", text)
        # Remove trailing English explanatory text commonly caught in formulas
        text = re.sub(r"\\text\{otherwise\}|\botherwise\b", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\\text\{if\}\s*.*$|\bif\s+.*$", "", text, flags=re.IGNORECASE)

        # 6. Fix common OCR spacing glitches around fractions, integrals, exponents
        text = re.sub(r"\\frac\s*\{", r"\\frac{", text)
        text = re.sub(r"\^\s*\{", r"^{", text)
        text = re.sub(r"_\s*\{", r"_{", text)
        text = re.sub(r"∫\s*", r"\\int ", text)
        text = re.sub(r"∑\s*", r"\\sum ", text)

        # 7. Strip trailing semicolons, commas, periods, and spacing tags
        text = re.sub(r"\\(?:quad|qquad)\s*$", "", text)
        text = re.sub(r"[\s,;.]+$", "", text).strip()

        # 8. Repair unescaped percent signs
        text = re.sub(r"(?<!\\)%", r"\%", text)

        # 9. Protect compound multi-letter variables (e.g. \text{RS} or RS -> R_{S})
        if protect_compound_symbols:
            for symbol, replacement in self.COMPOUND_SYMBOLS:
                # Replace \text{RS} or \mathrm{RS} with replacement
                text = re.sub(rf"\\(?:text|mathrm|mathbf)\{{{symbol}\}}", replacement, text)
                # Replace isolated word symbol (bounded by non-word characters or operators)
                text = re.sub(rf"\b{symbol}\b", replacement, text)

        return text.strip()
