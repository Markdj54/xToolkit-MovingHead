"""
test_translation.py

Integration test for TranslationBuilder.
"""

from core.xml_reader import XMLReader

from core.domain.function_catalog import FunctionCatalog

from core.services.alias_service import AliasService
from core.services.function_resolver import FunctionResolver
from core.services.unknown_function_registry import (
    UnknownFunctionRegistry,
)

from core.services.xlights_importer import XLightsImporter
from core.services.translation_builder import (
    TranslationBuilder,
)


def choose_fixture(models):

    print()

    for index, model in enumerate(models, start=1):
        print(f"{index:2}. {model.name}")

    print()

    while True:

        try:

            choice = int(input("Select fixture: "))

            if 1 <= choice <= len(models):
                return models[choice - 1]

        except ValueError:
            pass

        print("Invalid selection.")


def main():

    filename = input("Path to rgbeffects.xml: ")

    reader = XMLReader()

    if not reader.load(filename):
        print("Unable to load XML.")
        return

    catalog = FunctionCatalog()
    catalog.load_defaults()

    alias_service = AliasService(catalog)

    resolver = FunctionResolver(alias_service)

    registry = UnknownFunctionRegistry()

    importer = XLightsImporter(
        resolver,
        registry,
    )

    builder = TranslationBuilder()

    moving_heads = reader.get_moving_heads()

    print()
    print("Source Fixture")
    source_model = choose_fixture(moving_heads)

    print()
    print("Destination Fixture")
    destination_model = choose_fixture(moving_heads)

    source_fixture = importer.import_model(source_model)

    destination_fixture = importer.import_model(destination_model)

    print()
print("Source Capabilities")
print("-------------------")

for capability in source_fixture.capabilities:
    print(
        capability.function.display_name,
        capability.channel,
    )

print()

print("Destination Capabilities")
print("------------------------")

for capability in destination_fixture.capabilities:
    print(
        capability.function.display_name,
        capability.channel,
    )

    translation = builder.build(
        source_fixture,
        destination_fixture,
    )

    print()
    print("=" * 60)
    print("Translation Map")
    print("=" * 60)

    print(
        f"{translation.source_fixture}"
        f" -> "
        f"{translation.destination_fixture}"
    )

    print()

    print(
        f"{'Function':20}"
        f"{'Source':>8}"
        f"{'Dest':>8}"
        f"{'Status':>12}"
    )

    print("-" * 60)

    for entry in translation:

        status = "OK" if entry.translated else "Missing"

        print(
            f"{entry.function.display_name:20}"
            f"{entry.source_channel:>8}"
            f"{entry.destination_channel:>8}"
            f"{status:>12}"
        )


if __name__ == "__main__":
    main()