"""
moving_head_data.py

Stores xLights-specific information about a moving head.

This data is NOT part of the canonical fixture comparison.

Instead it contains the implementation details required
for sequence conversion.
"""

from dataclasses import dataclass, field


@dataclass
class ColourSlot:
    """One colour wheel position."""

    dmx: int
    colour: str


@dataclass
class ColourWheel:
    """Colour wheel definition."""

    channel: int = 0

    slots: list[ColourSlot] = field(default_factory=list)


@dataclass
class Motor:

    coarse_channel: int = 0

    fine_channel: int = 0

    minimum: float = 0.0

    maximum: float = 0.0

    movement: float = 0.0

    reverse: bool = False

    upside_down: bool = False


@dataclass
class Beam:

    length: float = 0.0

    width: float = 0.0

    y_offset: float = 0.0

    orientation: float = 0.0


@dataclass
class MovingHeadData:
    """
    xLights Moving Head implementation details.

    This is deliberately separate from the canonical
    comparison engine.
    """

    colour_wheel: ColourWheel = field(default_factory=ColourWheel)

    pan_motor: Motor = field(default_factory=Motor)

    tilt_motor: Motor = field(default_factory=Motor)

    beam: Beam = field(default_factory=Beam)

    dimmer_channel: int = 0

    shutter_channel: int = 0

    shutter_open_value: int = 0

    shutter_on_value: int = 0