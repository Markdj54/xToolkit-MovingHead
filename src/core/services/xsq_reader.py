"""
xsq_reader.py

Reads an xLights .xsq file and converts it into a Sequence.

Version 2 populates each EffectDefinition using the
ParameterParser.
"""

from pathlib import Path
import xml.etree.ElementTree as ET

from core.domain.sequence import Sequence
from core.domain.effect_definition import EffectDefinition

from core.services.parameter_parser import ParameterParser


class XSQReader:

    def __init__(self):

        self.parameter_parser = ParameterParser()

    # ---------------------------------------------------------

    def read(self, filename) -> Sequence:

        filename = Path(filename)

        print(f"Opening: {filename.name}")

        tree = ET.parse(filename)

        root = tree.getroot()

        effect_db = root.find("EffectDB")

        if effect_db is None:
            raise RuntimeError("EffectDB not found.")

        sequence = Sequence()

        for effect_id, effect_xml in enumerate(effect_db):

            effect = self._parse_effect(
                effect_id,
                effect_xml,
            )

            sequence.add_effect(effect)

        print(
            f"Loaded {sequence.effect_count()} effects."
        )

        return sequence

    # ---------------------------------------------------------

    def _parse_effect(
        self,
        effect_id,
        effect_xml,
    ) -> EffectDefinition:

        effect = EffectDefinition(
            effect_id=effect_id,
            effect_type="Unknown",
        )

        #
        # Preserve the original XML node.
        #
        effect.set_xml_element(effect_xml)

        raw_text = effect_xml.text

        if raw_text is None:

            return effect

        parameters = self.parameter_parser.parse(
            raw_text.strip()
        )

        for name, value in parameters.items():

            effect.set(
                name,
                value,
            )

        return effect