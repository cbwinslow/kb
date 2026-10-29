"""LaTeX equation sanitizer for repairing OCR artifacts, Unicode glitches, and formatting formulas for SymPy."""

from __future__ import annotations

import re
import unicodedata
from typing import ClassVar


class EquationSanitizer:
    """Sanitizer for cleaning and normalizing LaTeX mathematical expressions into valid SymPy ASTs."""

    # Regex patterns for environment, label, tag cleanup
    TAG_RE: ClassVar[re.Pattern[str]] = re.compile(
        r"[\s,;.]*(?:\\tag\{[^}]*\}|\([0-9]+(?:\.[0-9]+)*\)|\([A-Za-z0-9]+\.[0-9]+\))[\s,;.]*$"
    )
    LABEL_RE: ClassVar[re.Pattern[str]] = re.compile(r"\\label\{[^}]*\}")
    ENV_STRIP_RE: ClassVar[re.Pattern[str]] = re.compile(
        r"\\begin\{(?:equation|align|aligned|gather|displaymath)\*?\}"
        r"([\s\S]*?)"
        r"\\end\{(?:equation|align|aligned|gather|displaymath)\*?\}"
    )
    DOLLAR_STRIP_RE: ClassVar[re.Pattern[str]] = re.compile(r"^\${1,2}|\${1,2}$")

    # Common multi-letter domain metric variables mapped to subscripted symbols for SymPy
    COMPOUND_SYMBOLS: ClassVar[list[tuple[str, str]]] = [
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

    UNICODE_GREEK_MAP: ClassVar[dict[str, str]] = {
        "α": r"\alpha ",
        "β": r"\beta ",
        "γ": r"\gamma ",
        "δ": r"\delta ",
        "ε": r"\epsilon ",
        "ϵ": r"\epsilon ",
        "ζ": r"\zeta ",
        "η": r"\eta ",
        "θ": r"\theta ",
        "ϑ": r"\theta ",
        "ι": r"\iota ",
        "κ": r"\kappa ",
        "λ": r"\lambda ",
        "μ": r"\mu ",
        "µ": r"\mu ",
        "ν": r"\nu ",
        "ξ": r"\xi ",
        "π": r"\pi ",
        "ϖ": r"\varpi ",
        "ρ": r"\rho ",
        "ϱ": r"\varrho ",
        "σ": r"\sigma ",
        "ς": r"\varsigma ",
        "τ": r"\tau ",
        "υ": r"\upsilon ",
        "φ": r"\phi ",
        "ϕ": r"\phi ",
        "χ": r"\chi ",
        "ψ": r"\psi ",
        "ω": r"\omega ",
        "Γ": r"\Gamma ",
        "Δ": r"\Delta ",
        "Θ": r"\Theta ",
        "Λ": r"\Lambda ",
        "Ξ": r"\Xi ",
        "Π": r"\Pi ",
        "Σ": r"\Sigma ",
        "Υ": r"\Upsilon ",
        "Φ": r"\Phi ",
        "Ψ": r"\Psi ",
        "Ω": r"\Omega ",
    }

    UNICODE_OPERATORS_MAP: ClassVar[dict[str, str]] = {
        "∑": r"\sum ",
        "∏": r"\prod ",
        "∫": r"\int ",
        "∂": r"\partial ",
        "√": r"\sqrt ",
        "∈": r"\in ",
        "∉": r"\notin ",
        "≤": r"\le ",
        "≥": r"\ge ",
        "≠": r"\ne ",
        "≈": r"\approx ",
        "∼": r"\sim ",
        "≃": r"\simeq ",
        "≡": r"\equiv ",
        "∝": r"\propto ",
        "∞": r"\infty ",
        "∥": "|",
        "‖": "|",
        "∣": "|",
        "×": r"\times ",
        "·": r"\cdot ",
        "∗": "*",
        "−": "-",
        "…": r"\dots ",
        "±": r"\pm ",
        "∓": r"\mp ",
        "ℓ": "l",
        "′": "'",
        "″": "''",
        "ˆ": "",
        "˜": r"\sim ",
        "∀": r"\forall ",
        "∃": r"\exists ",
        "∅": r"\emptyset ",
        "∪": r"\cup ",
        "∩": r"\cap ",
        "⊂": r"\subset ",
        "⊆": r"\subseteq ",
        "→": r"\to ",
        "⇒": r"\Rightarrow ",
        "↔": r"\leftrightarrow ",
        "⇔": r"\Leftrightarrow ",
        "\ufffd": " ",
    }

    UNICODE_SUBSCRIPTS: ClassVar[dict[str, str]] = {
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
        "₊": "_+",
        "₋": "_-",
        "₌": "_=",
        "₍": "_(",
        "₎": "_)",
        "ₐ": "_a",
        "ₑ": "_e",
        "ₕ": "_h",
        "ᵢ": "_i",
        "ⱼ": "_j",
        "ₖ": "_k",
        "ₗ": "_l",
        "ₘ": "_m",
        "ₙ": "_n",
        "ₒ": "_o",
        "ₚ": "_p",
        "ᵣ": "_r",
        "ₛ": "_s",
        "ₜ": "_t",
        "ᵤ": "_u",
        "ᵥ": "_v",
        "ₓ": "_x",
    }

    UNICODE_SUPERSCRIPTS: ClassVar[dict[str, str]] = {
        "⁰": "^0",
        "¹": "^1",
        "²": "^2",
        "³": "^3",
        "⁴": "^4",
        "⁵": "^5",
        "⁶": "^6",
        "⁷": "^7",
        "⁸": "^8",
        "⁹": "^9",
        "⁺": "^+",
        "⁻": "^-",
        "⁼": "^=",
        "⁽": "^(",
        "⁾": "^)",
        "ⁿ": "^n",
        "ⁱ": "^i",
    }

    MACRO_PATTERNS: ClassVar[list[str]] = [
        r"\\boldsymbol\s*\{([^}]*)\}",
        r"\\bm\s*\{([^}]*)\}",
        r"\\mathbf\s*\{([^}]*)\}",
        r"\\mathbb\s*\{([^}]*)\}",
        r"\\mathcal\s*\{([^}]*)\}",
        r"\\mathscr\s*\{([^}]*)\}",
        r"\\mathfrak\s*\{([^}]*)\}",
        r"\\mathrm\s*\{([^}]*)\}",
        r"\\mathit\s*\{([^}]*)\}",
        r"\\text\s*\{([A-Za-z0-9_]+)\}",
        r"\\operatorname\s*\{([^}]*)\}",
    ]

    def clean_unicode(self, text: str) -> str:
        """Replace Unicode Greek, math operators, sub/superscripts, and decompose mathematical alphanumerics.

        Args:
            text: LaTeX text containing potential Unicode characters.

        Returns:
            Normalized ASCII LaTeX string.
        """
        for char, rep in self.UNICODE_OPERATORS_MAP.items():
            text = text.replace(char, rep)

        for char, rep in self.UNICODE_GREEK_MAP.items():
            text = text.replace(char, rep)

        for char, rep in self.UNICODE_SUBSCRIPTS.items():
            text = text.replace(char, rep)

        for char, rep in self.UNICODE_SUPERSCRIPTS.items():
            text = text.replace(char, rep)

        # Decompose Mathematical Alphanumerics (U+1D400 - U+1D7FF) to ASCII base characters
        chars: list[str] = []
        for c in text:
            if 0x1D400 <= ord(c) <= 0x1D7FF:
                chars.append(unicodedata.normalize("NFKD", c))
            else:
                chars.append(c)
        return "".join(chars)

    def unwrap_macros(self, text: str) -> str:
        """Unwrap font formatting and operator macros that ANTLR parser chokes on.

        Args:
            text: LaTeX string with formatting macros.

        Returns:
            LaTeX string with macros unwrapped.
        """
        prev = None
        while prev != text:
            prev = text
            for pat in self.MACRO_PATTERNS:
                text = re.sub(pat, r"\1", text)

        # Handle unbraced font macros (e.g., \mathbf x -> x)
        text = re.sub(
            r"\\(?:boldsymbol|bm|mathbf|mathbb|mathcal|mathrm|mathit)\s+([A-Za-z0-9])",
            r"\1",
            text,
        )
        # Remove invisible delimiters
        text = text.replace(r"\left.", "").replace(r"\right.", "")
        return text

    def balance_braces(self, text: str) -> str:
        """Balance unmatched curly braces caused by truncation or OCR extraction errors.

        Args:
            text: LaTeX string.

        Returns:
            LaTeX string with balanced braces.
        """
        open_c = text.count("{")
        close_c = text.count("}")
        if open_c > close_c:
            text = text + ("}" * (open_c - close_c))
        elif close_c > open_c:
            diff = close_c - open_c
            while diff > 0 and text.endswith("}"):
                text = text[:-1]
                diff -= 1
        return text

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

        # 4. Clean Unicode characters (Greek, operators, subscripts, math alphanumerics)
        text = self.clean_unicode(text)

        # 5. Unwrap ANTLR-incompatible macros (\boldsymbol, \mathbb, etc.)
        text = self.unwrap_macros(text)

        # 6. Ensure standard math function names have backslashes if missing
        text = re.sub(
            r"(?<!\\)\b(arccos|arcsin|arctan|cos|sin|tan|log|ln|exp)\b",
            r"\\\1",
            text,
        )

        # 7. Remove OCR piecewise artifacts and trailing conditions
        text = re.sub(r"[]", "", text)
        text = re.sub(r"\\begin\{cases\}", "", text)
        text = re.sub(r"\\end\{cases\}", "", text)
        # Remove trailing English explanatory text commonly caught in formulas
        text = re.sub(r"\\text\{otherwise\}|\botherwise\b", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\\text\{if\}\s*.*$|\bif\s+.*$", "", text, flags=re.IGNORECASE)

        # 8. Fix common OCR spacing glitches around fractions, integrals, exponents
        text = re.sub(r"\\frac\s*\{", r"\\frac{", text)
        text = re.sub(r"\^\s*\{", r"^{", text)
        text = re.sub(r"_\s*\{", r"_{", text)
        text = re.sub(r"∫\s*", r"\\int ", text)
        text = re.sub(r"∑\s*", r"\\sum ", text)

        # 9. Strip trailing semicolons, commas, periods, and spacing tags
        text = re.sub(r"\\(?:quad|qquad)\s*$", "", text)
        text = re.sub(r"[\s,;.]+$", "", text).strip()

        # 10. Repair unescaped percent signs
        text = re.sub(r"(?<!\\)%", r"\%", text)

        # 11. Balance curly braces
        text = self.balance_braces(text)

        # 12. Protect compound multi-letter variables (e.g. \text{RS} or RS -> R_{S})
        if protect_compound_symbols:
            for symbol, replacement in self.COMPOUND_SYMBOLS:
                text = re.sub(rf"\\(?:text|mathrm|mathbf)\{{{symbol}\}}", replacement, text)
                text = re.sub(rf"\b{symbol}\b", replacement, text)

        return text.strip()
