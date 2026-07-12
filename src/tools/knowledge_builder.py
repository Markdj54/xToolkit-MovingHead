"""
knowledge_builder.py

Developer tool for analysing xLights moving head fixtures.
"""

from pathlib import Path
import sys
from collections import Counter

# -------------------------------------------------
# Allow imports from the src directory
# -------------------------------------------------

SRC_DIR = Path(__file__).resolve().parent.parent

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# -------------------------------------------------

from core.xml_reader import XMLReader


def main():

    xml_file = SRC_DIR / "xlights_rgbeffects.xml"

    if not xml_file.exists():
        print(f"Could not find {xml_file}")
        return

    reader = XMLReader()

    if not reader.load(str(xml_file)):
        print("Unable to read rgbeffects.xml")
        return

    counter = Counter()

    fixture_count = 0

    for model in reader.get_models():

        if not model.is_moving_head():
            continue

        fixture_count += 1

        for channel in range(1, model.channel_count + 1):

            name = model.get_channel_name(channel).strip()

            if not name:
                name = "<Blank>"

            counter[name] += 1

    print()
    print("----------------------------------------")
    print("Knowledge Builder")
    print("----------------------------------------")
    print()

    print(f"Moving Heads : {fixture_count}")
    print(f"Unique Names : {len(counter)}")

    print()
    print("----------------------------------------")
    print("Channel Frequency")
    print("----------------------------------------")

    for name, count in counter.most_common():

        print(f"{count:4}  {name}")


if __name__ == "__main__":
    main()