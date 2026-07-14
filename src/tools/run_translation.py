"""
run_translation.py

Development tool for translating an imported xLights
sequence using xToolkit.

Sprint 11
"""

from core.services.xsq_reader import XSQReader
from core.services.xsq_writer import XSQWriter
from core.services.sequence_translator import SequenceTranslator

from core.translation.translation_map import TranslationMap


def main():

    #
    # Change these paths to suit your machine.
    #
    input_file = "ImportedSequence.xsq"

    output_file = "TranslatedSequence.xsq"

    #
    # Build translation map.
    #
    translation_map = TranslationMap()

    #
    # TODO
    #
    # Populate TranslationMap here.
    #
    # translation_map.add(...)
    #

    #
    # Read sequence.
    #
    reader = XSQReader()

    sequence = reader.read(
        input_file
    )

    #
    # Translate.
    #
    translator = SequenceTranslator(
        translation_map
    )

    translated_sequence = translator.translate(
        sequence
    )

    #
    # Write.
    #
    writer = XSQWriter()

    writer.load(
        input_file
    )

    changed = writer.write(
        translated_sequence
    )

    writer.save(
        output_file
    )

    print()

    print("---------------------------")

    print(
        f"Updated {changed} EffectDB entries."
    )

    print(
        f"Saved to {output_file}"
    )


if __name__ == "__main__":

    main()