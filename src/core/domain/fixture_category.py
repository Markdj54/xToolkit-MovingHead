"""
fixture_category.py

Categories used to group fixture functions.
"""

from enum import Enum


class FixtureCategory(Enum):
    MOVEMENT = "Movement"
    BEAM = "Beam"
    COLOR = "Color"
    GOBO = "Gobo"
    EFFECT = "Effect"