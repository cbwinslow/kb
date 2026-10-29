# Specification: Universal Unicode & Mathematical Sanitization

## Scope & Purpose
Extends LaTeX sanitization to convert all heterogeneous Unicode mathematical glyphs, Greek alphabets, mathematical alphanumeric variations, and styling macros into standardized, parseable LaTeX expressions compatible with SymPy's formal mathematical grammar.

## Requirements
1. **Mathematical Alphanumerics ($U+1D400 - U+1D7FF$)**:
   - `EquationSanitizer` MUST decompose and normalize all mathematical alphanumeric characters (e.g. bold, italic, sans-serif, fraktur, double-struck) using `NFKD` into ASCII letters and digits.
2. **Greek Alphabet & Variants**:
   - MUST map all Greek lowercase letters ($\alpha$ through $\omega$), uppercase letters ($\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Upsilon, \Phi, \Psi, \Omega$), and typographic variants ($\vartheta, \varphi, \varpi, \varrho, \varsigma, \epsilon, \phi$) to standard LaTeX macro equivalents.
3. **Mathematical Operators & Relations**:
   - MUST translate operators ($\sum, \prod, \int, \oint, \partial, \sqrt{}, \pm, \mp$) and relational symbols ($\in, \notin, \le, \ge, \ne, \approx, \sim, \equiv, \propto$) to valid LaTeX.
   - MUST replace Unicode replacement character `\uFFFD` with clean whitespace.
4. **LaTeX Macro Unwrapping**:
   - MUST unwrap font styling commands (`\boldsymbol{...}`, `\bm{...}`, `\mathbf{...}`, `\mathbb{...}`, `\mathcal{...}`, `\mathrm{...}`) to preserve variable names without artificial multiplication tokens.
   - MUST convert statistical function wrappers `\operatorname{Var}`, `\operatorname{E}`, `\operatorname{Cov}`, `\operatorname{Pr}` into standard function forms.
5. **Structural Integrity**:
   - MUST balance mismatched curly braces and strip trailing punctuation artifacts.
