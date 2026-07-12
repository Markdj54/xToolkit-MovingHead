"""
canonical_functions.py

Canonical lighting functions understood by xToolkit.

These represent WHAT a fixture can do,
not HOW a manufacturer implements it.
"""

from core.domain.fixture_function import FixtureFunction
from core.domain.fixture_category import FixtureCategory


# ==========================================================
# MOVEMENT
# ==========================================================

PAN = FixtureFunction(
    "PAN",
    "Pan",
    FixtureCategory.MOVEMENT,
    10,
)

PAN_FINE = FixtureFunction(
    "PAN_FINE",
    "Pan Fine",
    FixtureCategory.MOVEMENT,
    9,
)

TILT = FixtureFunction(
    "TILT",
    "Tilt",
    FixtureCategory.MOVEMENT,
    10,
)

TILT_FINE = FixtureFunction(
    "TILT_FINE",
    "Tilt Fine",
    FixtureCategory.MOVEMENT,
    9,
)

PAN_TILT_SPEED = FixtureFunction(
    "PAN_TILT_SPEED",
    "Pan/Tilt Speed",
    FixtureCategory.MOVEMENT,
    6,
)


# ==========================================================
# BEAM
# ==========================================================

DIMMER = FixtureFunction(
    "DIMMER",
    "Dimmer",
    FixtureCategory.BEAM,
    10,
)

SHUTTER = FixtureFunction(
    "SHUTTER",
    "Shutter",
    FixtureCategory.BEAM,
    9,
)

FOCUS = FixtureFunction(
    "FOCUS",
    "Focus",
    FixtureCategory.BEAM,
    5,
)

ZOOM = FixtureFunction(
    "ZOOM",
    "Zoom",
    FixtureCategory.BEAM,
    5,
)

FROST = FixtureFunction(
    "FROST",
    "Frost",
    FixtureCategory.BEAM,
    2,
)

IRIS = FixtureFunction(
    "IRIS",
    "Iris",
    FixtureCategory.BEAM,
    4,
)


# ==========================================================
# COLOUR
# ==========================================================

COLOR = FixtureFunction(
    "COLOR",
    "Color",
    FixtureCategory.COLOR,
    8,
)


# ==========================================================
# GOBO
# ==========================================================

GOBO = FixtureFunction(
    "GOBO",
    "Gobo",
    FixtureCategory.GOBO,
    7,
)

GOBO_ROTATE = FixtureFunction(
    "GOBO_ROTATE",
    "Gobo Rotate",
    FixtureCategory.GOBO,
    5,
)


# ==========================================================
# EFFECTS
# ==========================================================

PRISM = FixtureFunction(
    "PRISM",
    "Prism",
    FixtureCategory.EFFECT,
    6,
)

PRISM_ROTATE = FixtureFunction(
    "PRISM_ROTATE",
    "Prism Rotate",
    FixtureCategory.EFFECT,
    5,
)


# ==========================================================
# CONTROL
# ==========================================================

RESET = FixtureFunction(
    "RESET",
    "Reset",
    FixtureCategory.CONTROL,
    1,
)

MACRO = FixtureFunction(
    "MACRO",
    "Macro",
    FixtureCategory.CONTROL,
    2,
)

UNUSED = FixtureFunction(
    "UNUSED",
    "Unused",
    FixtureCategory.CONTROL,
    0,
)