"""
xsq_writer.py

Writes translated xLights EffectDB entries back into an
existing XSQ document while preserving the original XML
structure.
"""

from pathlib import Path
import xml.etree.ElementTree as ET

from core.services.effect_serializer import EffectSerializer


class XSQWriter:

    def __init__(self):

        self._tree = None
        self._root = None
        self._effect_db = None

        self._serializer = EffectSerializer()

    # ---------------------------------------------------------

    def load(
        self,
        filename,
    ):

        filename = Path(filename)

        print(f"Opening: {filename.name}")

        self._tree = ET.parse(filename)

        self._root = self._tree.getroot()

        self._effect_db = self._root.find("EffectDB")

        if self._effect_db is None:
            raise RuntimeError(
                "EffectDB not found."
            )

    # ---------------------------------------------------------

    def write(
        self,
        sequence,
    ) -> int:

        if self._effect_db is None:
            raise RuntimeError(
                "No XSQ loaded."
            )

        changed = 0

        for effect in sequence.effects():

            effect_xml = self._effect_db[
                effect.effect_id
            ]

            new_text = self._serializer.serialize(
                effect
            )

            old_text = effect_xml.text or ""

            if new_text != old_text:

                effect_xml.text = new_text

                changed += 1

        return changed

    # ---------------------------------------------------------

    def save(
        self,
        filename,
    ):

        if self._tree is None:
            raise RuntimeError(
                "No XSQ loaded."
            )

        filename = Path(filename)

        self._tree.write(
            filename,
            encoding="utf-8",
            xml_declaration=True,
        )

        print(f"Saved: {filename.name}")