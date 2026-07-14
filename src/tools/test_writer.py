"""
test_writer.py

Development tool.

Reads an XSQ file and immediately writes it back out.

No translation is performed.

If the output file opens correctly in xLights,
XSQReader, EffectSerializer and XSQWriter have
successfully completed a round-trip.
"""

from core.services.xsq_reader import XSQReader
from core.services.xsq_writer import XSQWriter


INPUT_FILE = (
    r"K:\Xlights Shows\Halloween 24\When the darkness comes 26V2.xsq"
)

OUTPUT_FILE = (
    r"K:\Xlights Shows\Halloween 24\When the darkness comes 26V2_RoundTrip.xsq"
)


def main():

    print("--------------------------------")
    print("xToolkit Writer Validation")
    print("--------------------------------")
    print()

    #
    # Read sequence.
    #
    reader = XSQReader()

    sequence = reader.read(INPUT_FILE)

    #
    # Write sequence.
    #
    writer = XSQWriter()

    writer.load(INPUT_FILE)

    changed = writer.write(sequence)

    writer.save(OUTPUT_FILE)

    print()

    print("--------------------------------")
    print("Validation Complete")
    print("--------------------------------")
    print(f"Effects Loaded : {sequence.effect_count()}")
    print(f"Effects Changed: {changed}")
    print(f"Output File    : {OUTPUT_FILE}")


if __name__ == "__main__":

    main()