"""
fixture_category.py

Categories used to group fixture functions.
"""

from enum import Enum


class FixtureCategory(Enum):
    """High-level groups of fixture capabilities."""

    MOVEMENT = "Movement"

    BEAM = "Beam"

    COLOR = "Color"

    GOBO = "Gobo"

    EFFECT = "Effect"

    CONTROL = "Control"