"""
model.py

Represents a single xLights model.

Every model in rgbeffects.xml (Mega Tree, Arch, Moving Head,
Matrix, etc.) becomes one Model object.
"""

from core.domain.moving_head_data import MovingHeadData


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

        self.channel_count = int(
            attributes.get("DmxChannelCount", "0")
        )

        self.node_names = []

        node_string = attributes.get("NodeNames", "")

        if node_string:
            self.node_names = [
                name.strip()
                for name in node_string.split(",")
            ]

        # Moving Head information
        self.moving_head = None

        if self.is_moving_head():
            self.moving_head = MovingHeadData()

    def get(self, key, default=""):
        """Return any XML attribute."""
        return self.attributes.get(key, default)

    def keys(self):
        """Return all attribute names."""
        return self.attributes.keys()

    def items(self):
        """Return (key, value) pairs."""
        return self.attributes.items()

    def get_channel_name(self, channel):

        if channel < 1:
            return "Invalid"

        if channel > len(self.node_names):
            return "Unknown"

        return self.node_names[channel - 1]

    def get_summary(self):

        return {
            "Name": self.name,
            "Type": self.display_as,
            "Controller": self.controller,
            "Channels": self.channel_count,
            "Start Channel": self.start_channel,
            "Layout Group": self.layout_group,
        }

    def is_moving_head(self):
        """True if this is a Moving Head."""
        return self.display_as == "DmxMovingHeadAdv"

    def has_moving_head_data(self):
        return self.moving_head is not None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Model {self.name}>"