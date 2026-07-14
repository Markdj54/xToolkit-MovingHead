"""
test_effect_roundtrip.py

Verifies that ParameterParser and EffectSerializer are
perfect inverses.

Sprint 11
"""

import unittest

import xml.etree.ElementTree as ET

from core.domain.effect_definition import EffectDefinition

from core.services.parameter_parser import ParameterParser
from core.services.effect_serializer import EffectSerializer


class TestEffectRoundTrip(unittest.TestCase):

    def test_round_trip(self):

        #
        # CHANGE THIS TO A REAL XSQ
        #
        xsq_file = "test_data/vendor.xsq"

        tree = ET.parse(xsq_file)

        root = tree.getroot()

        effect_db = root.find("EffectDB")

        self.assertIsNotNone(effect_db)

        parser = ParameterParser()

        serializer = EffectSerializer()

        #
        # Test every EffectDB entry.
        #
        for effect_id, effect_xml in enumerate(effect_db):

            original = effect_xml.text

            if original is None:

                continue

            effect = EffectDefinition(
                effect_id=effect_id,
                effect_type="Unknown",
            )

            parameters = parser.parse(
                original.strip()
            )

            for name, value in parameters.items():

                effect.set(
                    name,
                    value,
                )

            generated = serializer.serialize(
                effect
            )

            self.assertEqual(
                original.strip(),
                generated,
                msg=(
                    f"Round-trip failed "
                    f"for EffectDB[{effect_id}]"
                ),
            )


if __name__ == "__main__":

    unittest.main()