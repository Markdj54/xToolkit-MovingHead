"""
effect_serializer.py

Serializes an EffectDefinition back into the xLights
EffectDB parameter string.
"""

from core.domain.effect_definition import EffectDefinition


class EffectSerializer:

    # ---------------------------------------------------------

    def serialize(
        self,
        effect: EffectDefinition,
    ) -> str:

        parts = []

        for name, value in effect.parameters.items():

            parts.append(
                f"{name}={value}"
            )

        return ",".join(parts)