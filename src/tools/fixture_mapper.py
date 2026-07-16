"""
fixture_mapper.py

Reads two xLights moving head fixtures and displays the
translation map between them.

Sprint 13
"""

from core.services.rgbeffects_reader import RGBEffectsReader
from core.services.xlights_importer import XLightsImporter
from core.services.translation_builder import TranslationBuilder

from core.services.function_resolver import FunctionResolver
from core.services.alias_service import AliasService
from core.services.unknown_function_registry import (
    UnknownFunctionRegistry,
)

from core.domain.function_catalog import FunctionCatalog


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

VENDOR_RGBEFFECTS = (
    r"C:\Users\User\xlightsMHConvertor\test_data\xlights_rgbeffects_Darkness.xml"
)

MY_RGBEFFECTS = (
    r"C:\Users\User\xlightsMHConvertor\test_data\xlights_rgbeffects Copy.xml"
)

SOURCE_MODEL = (
    "MOVING HEAD 1 - YPS 350W"
)

DESTINATION_MODEL = (
    "MH1"
)


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def find_model(models, name):

    for model in models:

        if model.name == name:
            return model

    raise RuntimeError(
        f"Model '{name}' not found."
    )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print()
    print("--------------------------------")
    print("xToolkit Fixture Mapper")
    print("--------------------------------")
    print()

    #
    # Build resolver
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
    # Vendor fixture
    #

    vendor_models = RGBEffectsReader().load(
        VENDOR_RGBEFFECTS
    )

    vendor_model = find_model(
        vendor_models,
        SOURCE_MODEL,
    )

    vendor_fixture = importer.import_model(
        vendor_model,
    )

    print()
    print("Vendor Capabilities")
    print("-------------------")

    for capability in vendor_fixture.capabilities:

        print(
            capability.channel,
            capability.function.id,
        )

    #
    # My fixture
    #

    my_models = RGBEffectsReader().load(
        MY_RGBEFFECTS
    )

    my_model = find_model(
        my_models,
        DESTINATION_MODEL,
    )

    my_fixture = importer.import_model(
        my_model,
    )

    print()
    print("My Capabilities")
    print("----------------")

    for capability in my_fixture.capabilities:

        print(
            capability.channel,
            capability.function.id,
        )

    #
    # Build translation
    #

    translation = TranslationBuilder().build(
        vendor_fixture,
        my_fixture,
    )

    print()
    print("--------------------------------")
    print("Translation Map")
    print("--------------------------------")
    print()

    for entry in translation:

        status = "OK"

        if not entry.translated:
            status = "Missing"

        print(
            f"{entry.function.id:<20}"
            f"{entry.source_channel:>2}"
            f" -> "
            f"{entry.destination_channel:>2}   "
            f"{status}"
        )

    print()

    print("--------------------------------")
    print(f"Translated : {translation.translated_count()}")
    print(f"Total      : {len(translation)}")
    print(f"Unknown    : {unknown.count()}")
    print("--------------------------------")


if __name__ == "__main__":

    main()