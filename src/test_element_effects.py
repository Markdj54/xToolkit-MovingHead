"""
test_element_effects.py

Locate the first Moving Head effect in the timeline and
show its relationship to EffectDB.
"""

from pathlib import Path
import xml.etree.ElementTree as ET


filename = (
    Path(__file__).parent.parent
    / "test_data"
    / "Knife Party - Internet Friends HD Layout.xsq"
)

tree = ET.parse(filename)
root = tree.getroot()

element_effects = root.find("ElementEffects")

print()
print("=" * 70)
print("SEARCHING FOR MOVING HEAD EFFECTS")
print("=" * 70)

found = False

for element in element_effects:

    element_name = element.attrib.get("name", "")

    for layer in element.findall("EffectLayer"):

        for effect in layer.findall("Effect"):

            name = effect.attrib.get("name", "")

            #
            # We don't know exactly what xLights calls it yet.
            #
            if (
                "DMX" in name
                or "Moving" in name
                or "Head" in name
            ):

                print()
                print(f"Element : {element_name}")
                print()

                print("Effect Attributes")

                for key, value in effect.attrib.items():

                    print(f"{key:<20} {value}")

                found = True
                raise SystemExit()

if not found:

    print()
    print("No Moving Head effect found.")