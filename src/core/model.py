"""
model.py

Represents a single xLights model.

Every model in rgbeffects.xml (Mega Tree, Arch, Moving Head,
Matrix, etc.) becomes one Model object.
"""


class Model:
    """Represents one xLights model."""

    def __init__(self, attributes: dict):

        # Store every XML attribute
        self.attributes = dict(attributes)

        # Frequently used properties
        self.name = attributes.get("name", "")

        self.display_as = attributes.get("DisplayAs", "")

        self.controller = attributes.get("Controller", "")

        self.start_channel = attributes.get("StartChannel", "")

        self.layout_group = attributes.get("LayoutGroup", "")

    def get(self, key, default=""):
        """Return any XML attribute."""

        return self.attributes.get(key, default)

    def keys(self):
        """Return all attribute names."""

        return self.attributes.keys()

    def items(self):
        """Return (key, value) pairs."""

        return self.attributes.items()

    def is_moving_head(self):
        """True if this is a Moving Head."""

        return self.display_as == "DmxMovingHeadAdv"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Model {self.name}>"