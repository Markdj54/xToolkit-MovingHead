"""
translate_sequence.py

Translates an imported xLights sequence from one moving
head fixture personality to another.

Sprint 13
"""

from core.services.rgbeffects_reader import RGBEffectsReader
from core.services.xlights_importer import XLightsImporter
from core.services.translation_builder import TranslationBuilder

from core.services.xsq_reader import XSQReader
from core.services.xsq_writer import XSQWriter

from core.services.sequence_translator import SequenceTranslator
from core.services.effect_translator import EffectTranslator
from core.services.parameter_translator import ParameterTranslator
from core.services.dmx_parameter_mapper import DMXParameterMapper

from core.services.function_resolver import FunctionResolver
from core.services.alias_service import AliasService
from core.services.unknown_function_registry import (
    UnknownFunctionRegistry,
)

from core.domain.function_catalog import FunctionCatalog


#
# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
#

VENDOR_RGBEFFECTS = (
    r"C:\Users\User\xlightsMHConvertor\test_data\xlights_rgbeffects_Darkness.xml"
)

MY_RGBEFFECTS = (
    r"C:\Users\User\xlightsMHConvertor\test_data\xlights_rgbeffects Copy.xml"
)

INPUT_XSQ = (
    r"C:\Users\User\xlightsMHConvertor\test_data\69 WHEN THE DARKNESS COMES.xsq"
)

OUTPUT_XSQ = (
    r"C:\Users\User\xlightsMHConvertor\test_data\69 WHEN THE DARKNESS COMES_Translated.xsq"
)

SOURCE_MODEL = (
    "MOVING HEAD 1 - YPS 350W"
)

DESTINATION_MODEL = (
    "MH1"
)


#
# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
#

def find_model(models, name):

    for model in models:

        if model.name == name:
            return model

    raise RuntimeError(
        f"Model '{name}' not found."
    )


#
# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
#

def main():

    print("--------------------------------")
    print("xToolkit Translation")
    print("--------------------------------")
    print()

    #
    # Build resolver.
    #

    catalog = FunctionCatalog()

    catalog.load_defaults()

    alias_service = AliasService(
        catalog,
    )

    resolver = FunctionResolver(
        alias_service,
    )

    unknown = UnknownFunctionRegistry()

    importer = XLightsImporter(
        resolver,
        unknown,
    )

    #
    # Read vendor fixtures.
    #

    vendor_reader = RGBEffectsReader()

    vendor_models = vendor_reader.load(
        VENDOR_RGBEFFECTS,
    )

    source_model = find_model(
        vendor_models,
        SOURCE_MODEL,
    )

    source_fixture = importer.import_model(
        source_model,
    )

    #
    # Read destination fixtures.
    #

    my_reader = RGBEffectsReader()

    my_models = my_reader.load(
        MY_RGBEFFECTS,
    )

    destination_model = find_model(
        my_models,
        DESTINATION_MODEL,
    )

    destination_fixture = importer.import_model(
        destination_model,
    )

    #
    # Build translation map.
    #

    translation = TranslationBuilder().build(
        source_fixture,
        destination_fixture,
    )

    #
    # Build translation pipeline.
    #

    mapper = DMXParameterMapper(
        source_fixture,
    )

    parameter_translator = ParameterTranslator(
        mapper,
        translation,
    )

    effect_translator = EffectTranslator(
        parameter_translator,
    )

    sequence_translator = SequenceTranslator(
        effect_translator,
    )

    sequence_translator = SequenceTranslator(
        effect_translator,
    )

    #
    # Read sequence.
    #

    xsq_reader = XSQReader()

    sequence = xsq_reader.read(
        INPUT_XSQ,
    )

    #
    # Translate.
    #

    translated = sequence_translator.translate(
        sequence,
    )

    #
    # Write sequence.
    #

    writer = XSQWriter()

    writer.load(INPUT_XSQ)

    changed = writer.write(
        translated,
    )

    writer.save(
        OUTPUT_XSQ,
    )

    print()

    print("--------------------------------")

    print("Translation Complete")

    print("--------------------------------")

    print(
        f"Effects Loaded : {sequence.effect_count()}"
    )

    print(
        f"Parameters Translated : {translation.translated_count()}"
    )

    print(
        f"Effects Changed : {changed}"
    )

    print()

    print(
        f"Unknown Functions : {unknown.count()}"
    )


if __name__ == "__main__":

    main()