"""
test_compare.py

Integration test for the xToolkit comparison pipeline.

Pipeline:

XMLReader
    ↓
Model
    ↓
XLightsImporter
    ↓
CanonicalFixture
    ↓
ComparisonEngine
    ↓
ComparisonReport
"""

from core.xml_reader import XMLReader
from core.comparison_engine import ComparisonEngine

from core.domain.function_catalog import FunctionCatalog

from core.services.alias_service import AliasService
from core.services.function_resolver import FunctionResolver
from core.services.unknown_function_registry import (
    UnknownFunctionRegistry,
)

from core.services.xlights_importer import XLightsImporter


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

    print("=" * 60)
    print("xToolkit Backend Integration Test")
    print("=" * 60)
    print()

    filename = input("Path to rgbeffects.xml: ")

    reader = XMLReader()

    if not reader.load(filename):

        print("Unable to load XML.")
        return

    #
    # Build canonical pipeline
    #

    catalog = FunctionCatalog()
    catalog.load_defaults()

    alias_service = AliasService(catalog)

    resolver = FunctionResolver(alias_service)

    registry = UnknownFunctionRegistry()

    importer = XLightsImporter(
        resolver,
        registry,
    )

    engine = ComparisonEngine()

    moving_heads = reader.get_moving_heads()

    print(f"Moving Heads Found: {len(moving_heads)}")

    for mh in moving_heads:
        print(f"  {mh.name}")

    if len(moving_heads) < 2:

        print("Less than two moving heads found.")
        return

    print()
    print("Source Fixture")
    print("--------------")

    source_model = choose_fixture(moving_heads)

    print()
    print("Destination Fixture")
    print("-------------------")

    destination_model = choose_fixture(moving_heads)

    #
    # Import
    #

    source_fixture = importer.import_model(source_model)

    destination_fixture = importer.import_model(destination_model)

    #
    # Compare
    #

    report = engine.compare(
        source_fixture,
        destination_fixture,
    )

    #
    # Results
    #

    print()
    print("=" * 60)
    print("Comparison Report")
    print("=" * 60)

    print()
    print(f"Source      : {source_fixture.name}")
    print(f"Destination : {destination_fixture.name}")

    print()

    print(
        f"Compatibility : "
        f"{report.statistics.compatibility}%"
    )

    print()

    print(
        f"Matches     : {report.statistics.matches}"
    )

    print(
        f"Different   : {report.statistics.different}"
    )

    print(
        f"Missing     : {report.statistics.missing}"
    )

    print(
        f"Extra       : {report.statistics.extra}"
    )

    print()

    print("Functions")
    print("-" * 60)

    for result in report:

        print(
            f"{result.function:<20}"
            f"{str(result.status):<18}"
            f"{str(result.source_channel):>4}"
            f" -> "
            f"{str(result.destination_channel):<4}"
        )

    print()

    if registry.count():

        print("Unknown Functions")
        print("-" * 60)

        for name in registry.all():
            print(name)


if __name__ == "__main__":
    main()