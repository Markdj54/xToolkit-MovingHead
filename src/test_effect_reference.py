"""
test_effect_reference.py

Proves the relationship between ElementEffects and EffectDB.
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

effect_db = root.find("EffectDB")
element_effects = root.find("ElementEffects")

TARGET_REF = 79

print()
print("=" * 70)
print("EFFECT REFERENCE INVESTIGATION")
print("=" * 70)
print()

#
# Locate the timeline reference
#

found = False

for element in element_effects:

    element_name = element.attrib.get("name", "")

    for layer in element.findall("EffectLayer"):

        for effect in layer.findall("Effect"):

            ref = int(effect.attrib.get("ref", -1))

            if ref == TARGET_REF:

                print("Timeline Reference")
                print("-" * 40)

                print(f"Element     : {element_name}")
                print(f"Effect Name : {effect.attrib.get('name')}")
                print(f"Start Time  : {effect.attrib.get('startTime')}")
                print(f"End Time    : {effect.attrib.get('endTime')}")
                print(f"Reference   : {ref}")

                found = True
                break

        if found:
            break

    if found:
        break

#
# Display the EffectDB entry
#

print()
print("=" * 70)
print("EFFECTDB ENTRY")
print("=" * 70)
print()

effect_xml = effect_db[TARGET_REF]

print(effect_xml.text.strip())