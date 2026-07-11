from enum import Enum


class FixtureCategory(Enum):

    MOVEMENT = "Movement"

    BEAM = "Beam"

    COLOR = "Color"

    GOBO = "Gobo"

    EFFECT = "Effect"

    CONTROL = "Control"

    OTHER = "Other"

    def __str__(self):
        return self.value