"""
xToolkit v0.3.1

Test the Fixture Comparison Engine
"""

from core.xml_reader import XMLReader
from core.comparer import FixtureComparer


def main():

    reader = XMLReader()

    filename = input("Path to rgbeffects.xml: ")

    if not reader.load(filename):
        print("Unable to load XML")
        return

    source_name = input("Source fixture: ")
    destination_name = input("Destination fixture: ")

    source = reader.get_model(source_name)
    destination = reader.get_model(destination_name)

    if source is None:
        print(f"Source fixture '{source_name}' not found.")
        return

    if destination is None:
        print(f"Destination fixture '{destination_name}' not found.")
        return

    comparer = FixtureComparer()

    result = comparer.compare(source, destination)

    print()
    print("=" * 50)
    print("xToolkit Fixture Comparison")
    print("=" * 50)
    print()

    print(f"Source      : {source.name}")
    print(f"Destination : {destination.name}")
    print()
    print(f"Compatibility : {result.score}%")
    print()

    print("Matching Functions")
    print("------------------")

    for item in sorted(result.matches):
        print(f"  ✓ {item}")

    print()

    print("Missing From Destination")
    print("------------------------")

    if result.missing:
        for item in sorted(result.missing):
            print(f"  ✗ {item}")
    else:
        print("  None")

    print()

    print("Extra Functions")
    print("----------------")

    if result.extra:
        for item in sorted(result.extra):
            print(f"  + {item}")
    else:
        print("  None")


if __name__ == "__main__":
    main()