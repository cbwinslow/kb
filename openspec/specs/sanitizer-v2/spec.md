# Specification: Universal Equation Sanitizer 2.0

## Scope & Purpose
Extends `EquationSanitizer` to resolve the NFKD execution order bug, strip Docling Private Use Area font artifacts and combining accents, and map high-frequency mathematical operators to ensure SymPy grammar compatibility.

## Requirements
1. **NFKD Deconstruction Pipeline**:
   - `clean_unicode` MUST execute `unicodedata.normalize('NFKD', c)` for Mathematical Alphanumerics ($U+1D400 - U+1D7FF$) BEFORE Greek letter translation, ensuring Mathematical Bold/Italic Greek letters are converted to ASCII LaTeX macros.
2. **Missing Symbol Mappings**:
   - MUST map `\u2206` (Increment) $\to$ `\Delta `.
   - MUST map `\u2126` (Ohm) $\to$ `\Omega `.
   - MUST map `\u2207` (Nabla) $\to$ `\nabla `.
   - MUST map `\u2020` (Dagger) $\to$ `\dagger `.
   - MUST map `\u22a4` (Down Tack / Transpose) $\to$ `^T`.
   - MUST map `\u27e8` $\to$ `\langle ` and `\u27e9` $\to$ `\rangle `.
3. **Artifact Stripping**:
   - MUST strip combining accents: `\u20d7` (vector arrow), `\u02d9` (dot), `\xaf` (macron), `\u0302` (hat).
   - MUST strip Docling PUA font glyphs in range `\uf8e0` through `\uf8ff`.
