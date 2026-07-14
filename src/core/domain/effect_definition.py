"""
effect_definition.py

Represents one entry from the xLights EffectDB.
"""

from dataclasses import dataclass, field


@dataclass
class EffectDefinition:

    effect_id: int

    effect_type: str

    parameters: dict[str, str] = field(default_factory=dict)

    # ---------------------------------------------------------

    def get(self, name: str, default=None):

        return self.parameters.get(name, default)

    # ---------------------------------------------------------

    def set(self, name: str, value):

        self.parameters[name] = str(value)

    # ---------------------------------------------------------

    def has(self, name: str) -> bool:

        return name in self.parameters

    # ---------------------------------------------------------

    def parameter_count(self) -> int:

        return len(self.parameters)

    # ---------------------------------------------------------

    def is_moving_head(self) -> bool:

        for name in self.parameters:

            if "_DMX" in name:
                return True

        return False

    # ---------------------------------------------------------

    def __str__(self):

        return (
            f"EffectDefinition("
            f"id={self.effect_id}, "
            f"type='{self.effect_type}', "
            f"parameters={len(self.parameters)})"
        )