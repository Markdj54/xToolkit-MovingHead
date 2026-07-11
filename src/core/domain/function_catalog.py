from core.domain.fixture_function import FixtureFunction
from core.domain.fixture_categories import FixtureCategory


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

COLOR = FixtureFunction(
    "COLOR",
    "Color",
    FixtureCategory.COLOR,
    8,
)

GOBO = FixtureFunction(
    "GOBO",
    "Gobo",
    FixtureCategory.GOBO,
    7,
)

PRISM = FixtureFunction(
    "PRISM",
    "Prism",
    FixtureCategory.EFFECT,
    6,
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