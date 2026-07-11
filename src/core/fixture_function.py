"""
fixture_function.py

Canonical fixture functions used by xToolkit.
"""

from enum import Enum


class FixtureFunction(Enum):

    PAN = "Pan"

    PAN_FINE = "Pan Fine"

    TILT = "Tilt"

    TILT_FINE = "Tilt Fine"

    SPEED = "Pan/Tilt Speed"

    DIMMER = "Dimmer"

    SHUTTER = "Shutter"

    COLOR = "Color"

    GOBO = "Gobo"

    GOBO_ROTATE = "Gobo Rotate"

    PRISM = "Prism"

    PRISM_ROTATE = "Prism Rotate"

    FOCUS = "Focus"

    ZOOM = "Zoom"

    FROST = "Frost"

    IRIS = "Iris"

    UNKNOWN = "Unknown"

    def __str__(self):

        return self.value