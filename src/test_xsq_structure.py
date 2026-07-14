"""
test_xsq_structure.py

Searches the EffectDB for DMX effects.
"""

from pathlib import Path
import xml.etree.ElementTree as ET

filename = (
    Path(__file__).parent.parent
    / "test_data"
    / "Knife Party - Internet Friends HD Layout.xsq"
)

print(f"Opening:\n{filename}\n")

tree = ET.parse(filename)
root = tree.getroot()

effect_db = root.find("EffectDB")

if effect_db is None:
    raise RuntimeError("EffectDB not found.")

print(f"Searching {len(effect_db)} effects...\n")

found = False

for index, effect in enumerate(effect_db):

    text = effect.text or ""

    if "DMX" in text.upper():

        print("=" * 60)
        print(f"DMX EFFECT FOUND (Index {index})")
        print("=" * 60)
        print()
        print(text)
        print()
        found = True
        break

if not found:
    print("No DMX effects found.")