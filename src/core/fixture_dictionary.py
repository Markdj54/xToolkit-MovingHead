"""
xToolkit v0.3.1

fixture_dictionary.py

This file contains the standard moving head functions used by
xToolkit.

Every manufacturer uses different names.

This dictionary converts them into one common language.
"""


FUNCTIONS = {

    "Pan": {
        "category": "Movement",
        "aliases": [
            "Pan",
            "Pan / X-axis / Horizontal",
            "Horizontal",
            "X-axis",
            "Pan Movement",
        ]
    },

    "Pan Fine": {
        "category": "Movement",
        "aliases": [
            "Pan Fine",
            "Fine Pan",
        ]
    },

    "Tilt": {
        "category": "Movement",
        "aliases": [
            "Tilt",
            "Tilt / Y-axis / Vertical",
            "Vertical",
            "Y-axis",
            "Tilt Movement",
        ]
    },

    "Tilt Fine": {
        "category": "Movement",
        "aliases": [
            "Tilt Fine",
            "Fine Tilt",
        ]
    },

    "Speed": {
        "category": "Movement",
        "aliases": [
            "Pan & Tilt Speed",
            "Movement Speed",
            "Speed",
            "PT Speed",
        ]
    },

    "Dimmer": {
        "category": "Intensity",
        "aliases": [
            "Dimmer",
            "Intensity",
            "Master Dimmer",
            "Brightness",
        ]
    },

    "Shutter": {
        "category": "Intensity",
        "aliases": [
            "Shutter",
            "Shutter / Strobe",
            "Strobe",
        ]
    },

    "Color": {
        "category": "Colour",
        "aliases": [
            "Color",
            "Colour",
            "Color Wheel",
            "Colour Wheel",
        ]
    },

    "Color Fine": {
        "category": "Colour",
        "aliases": [
            "Color Fine",
            "Colour Fine",
        ]
    },

    "Gobo": {
        "category": "Optics",
        "aliases": [
            "Gobo",
            "Gobo Wheel",
            "Pattern",
        ]
    },

    "Gobo Rotate": {
        "category": "Optics",
        "aliases": [
            "Gobo Rotate",
            "Rotating Gobo",
        ]
    },

    "Prism": {
        "category": "Optics",
        "aliases": [
            "Prism",
            "Prism 1",
            "Prism 2",
        ]
    },

    "Prism Rotate": {
        "category": "Optics",
        "aliases": [
            "Prism Rotate",
            "Prism Rotate 1",
            "Prism Rotate 2",
        ]
    },

    "Focus": {
        "category": "Optics",
        "aliases": [
            "Focus",
        ]
    },

    "Zoom": {
        "category": "Optics",
        "aliases": [
            "Zoom",
        ]
    },

    "Frost": {
        "category": "Optics",
        "aliases": [
            "Frost",
        ]
    },

    "Iris": {
        "category": "Optics",
        "aliases": [
            "Iris",
        ]
    },

    "Reset": {
        "category": "System",
        "aliases": [
            "Reset",
            "Fixture Reset",
        ]
    },

    "Lamp": {
        "category": "System",
        "aliases": [
            "Lamp",
            "Lamp On",
            "Lamp Off",
        ]
    }

}


def normalise_function(channel_name):
    """
    Convert a manufacturer channel name into the
    xToolkit standard function name.

    Example:

        "Pan / X-axis / Horizontal"

    becomes

        "Pan"
    """

    if not channel_name:
        return "Unknown"

    text = channel_name.strip().lower()

    for standard_name, data in FUNCTIONS.items():

        for alias in data["aliases"]:

            if text == alias.lower():

                return standard_name

    return channel_name