"""
effect_definition.py

Represents one entry from the xLights EffectDB.
"""

from dataclasses import dataclass, field
from xml.etree.ElementTree import Element


@dataclass
class EffectDefinition:

    effect_id: int

    effect_type: str

    parameters: dict[str, str] = field(default_factory=dict)

    _xml_element: Element | None = field(
        default=None,
        repr=False,
        compare=False,
    )

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

        for name in self.parameters.keys():

            if "DMX" in name:
                return True

        return False

    # ---------------------------------------------------------

    def set_xml_element(
        self,
        element: Element,
    ) -> None:

        self._xml_element = element

    # ---------------------------------------------------------

    def xml_element(self) -> Element | None:

        return self._xml_element

    # ---------------------------------------------------------

    def has_xml_element(self) -> bool:

        return self._xml_element is not None

    # ---------------------------------------------------------

    def __str__(self):

        return (
            f"EffectDefinition("
            f"id={self.effect_id}, "
            f"type='{self.effect_type}', "
            f"parameters={len(self.parameters)})"
        )