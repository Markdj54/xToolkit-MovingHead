"""
rgbeffects_reader.py

Reads xLights rgbeffects.xml and produces Model objects.
"""

import xml.etree.ElementTree as ET

from core.domain.model import Model
from core.domain.moving_head_data import ColourSlot


class RGBEffectsReader:

    def __init__(self):
        self.models = []

    def load(self, filename):

        tree = ET.parse(filename)
        root = tree.getroot()

        self.models.clear()

        for xml_model in root.iter("model"):

            model = Model(xml_model.attrib)

            if model.has_moving_head_data():
                self._read_moving_head(model)

            self.models.append(model)

        return self.models

    def _read_moving_head(self, model):

        mh = model.moving_head

        #
        # Beam
        #

        mh.beam.length = float(model.get("DmxBeamLength", 0))

        mh.beam.width = float(model.get("DmxBeamWidth", 0))

        mh.beam.orientation = float(
            model.get("DmxBeamOrient", 0)
        )

        mh.beam.y_offset = float(
            model.get("DmxBeamYOffset", 0)
        )

        #
        # Channels
        #

        mh.dimmer_channel = int(
            model.get("MhDimmerChannel", 0)
        )

        mh.shutter_channel = int(
            model.get("DmxShutterChannel", 0)
        )

        mh.shutter_open_value = int(
            model.get("DmxShutterOpen", 0)
        )

        mh.shutter_on_value = int(
            model.get("DmxShutterOnValue", 0)
        )

        #
        # Colour wheel
        #

        mh.colour_wheel.channel = int(
            model.get("DmxColorWheelChannel", 0)
        )

        slot = 0

        while True:

            dmx_key = f"DmxColorWheelDMX{slot}"
            colour_key = f"DmxColorWheelColor{slot}"

            if dmx_key not in model.attributes:
                break

            dmx = int(model.get(dmx_key, 0))

            colour = model.get(colour_key, "")

            if dmx > 0:

                mh.colour_wheel.slots.append(

                    ColourSlot(

                        dmx=dmx,

                        colour=colour,

                    )

                )

            slot += 1