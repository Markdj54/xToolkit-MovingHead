"""
function_keywords.py

Keyword mappings used by the FunctionResolver.
"""

from core.domain.canonical_functions import (
    PAN,
    TILT,
    DIMMER,
    SHUTTER,
    COLOR,
)

FUNCTION_KEYWORDS = {

    "pan": PAN,

    "tilt": TILT,

    "dimmer": DIMMER,

    "intensity": DIMMER,

    "shutter": SHUTTER,

    "strobe": SHUTTER,

    "color": COLOR,

    "colour": COLOR,

}