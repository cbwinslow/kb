"""Physical dimensional analysis and unit compatibility checking using SymPy units."""

from __future__ import annotations

import logging
from typing import Any

from sympy.physics.units import (
    acceleration,
    energy,
    force,
    frequency,
    length,
    mass,
    momentum,
    time,
    velocity,
)
from sympy.physics.units.dimensions import Dimension
from sympy.physics.units.systems.si import SI

from kb.math.ontology import CanonicalConcept, SymbolOntology, get_symbol_ontology

logger = logging.getLogger(__name__)

DIMENSION_MAP: dict[str, Any] = {
    "dimensionless": Dimension(1),
    "length": length,
    "time": time,
    "mass": mass,
    "velocity": velocity,
    "acceleration": acceleration,
    "force": force,
    "energy": energy,
    "momentum": momentum,
    "frequency": frequency,
    "density": mass / (length**3),
    "angle": Dimension(1),
}


class DimensionalValidator:
    """Validates physical dimensional consistency between formulas and variable substitutions."""

    def __init__(self, ontology: SymbolOntology | None = None) -> None:
        """Initialize validator with optional symbol ontology.

        Args:
            ontology: SymbolOntology instance. Defaults to global ontology.
        """
        self.ontology = ontology or get_symbol_ontology()
        self._dim_system = SI.get_dimension_system()

    def get_dimension_for_concept(self, concept: CanonicalConcept | str | None) -> Any:
        """Resolve the physical dimension corresponding to a canonical concept or name.

        Args:
            concept: CanonicalConcept enum or string key.

        Returns:
            SymPy Dimension object or Dimension(1) for dimensionless.
        """
        if not concept:
            return Dimension(1)

        c_enum: CanonicalConcept | None = None
        if isinstance(concept, CanonicalConcept):
            c_enum = concept
        else:
            try:
                c_enum = CanonicalConcept(concept)
            except ValueError:
                c_enum = self.ontology.resolve_canonical(concept)

        if not c_enum:
            return Dimension(1)

        concept_def = self.ontology.get_concept(c_enum)
        if not concept_def:
            return Dimension(1)

        dim_str = getattr(concept_def, "dimension", "dimensionless").lower()
        return DIMENSION_MAP.get(dim_str, Dimension(1))

    def are_compatible(self, dim1: Any, dim2: Any) -> bool:
        """Check if two physical dimensions are equivalent in SI system.

        Args:
            dim1: First dimension or concept name.
            dim2: Second dimension or concept name.

        Returns:
            True if dimensions match; False otherwise.
        """
        resolved_1 = (
            self.get_dimension_for_concept(dim1)
            if not isinstance(dim1, (Dimension, type(velocity)))
            else dim1
        )
        resolved_2 = (
            self.get_dimension_for_concept(dim2)
            if not isinstance(dim2, (Dimension, type(velocity)))
            else dim2
        )

        if resolved_1 == resolved_2:
            return True

        if self._dim_system is None:
            return False

        try:
            return bool(self._dim_system.equivalent_dims(resolved_1, resolved_2))
        except Exception as err:
            logger.debug("Dimension check error between %s and %s: %s", dim1, dim2, err)
            return False

    def validate_substitution(
        self,
        target_concept: CanonicalConcept | str | None,
        source_concept: CanonicalConcept | str | None,
    ) -> tuple[bool, str]:
        """Validate whether a source concept can substitute for a target concept.

        Args:
            target_concept: Canonical concept being replaced.
            source_concept: Canonical concept providing the replacement.

        Returns:
            Tuple of (is_valid, reason_message).
        """
        if not target_concept or not source_concept:
            # If concept is unspecified, allow substitution with warning
            return True, "Unconstrained dimensional parameter"

        dim_target = self.get_dimension_for_concept(target_concept)
        dim_source = self.get_dimension_for_concept(source_concept)

        if self.are_compatible(dim_target, dim_source):
            return True, f"Dimensions match: {dim_target} == {dim_source}"

        msg = (
            f"Dimensional mismatch: target '{target_concept}' has dimension '{dim_target}', "
            f"but source '{source_concept}' has dimension '{dim_source}'"
        )
        logger.warning(msg)
        return False, msg
