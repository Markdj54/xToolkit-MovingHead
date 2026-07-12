"""
test_fixture_report.py

Tests the Fixture Report.
"""

from core.xml_reader import XMLReader

from core.domain.function_catalog import FunctionCatalog

from core.services.alias_service import AliasService
from core.services.function_resolver import FunctionResolver
from core.services.unknown_function_registry import (
    UnknownFunctionRegistry,
)
from core.services.fixture_report import FixtureReport

from core.importers.xlights_importer import XLightsImporter


# -------------------------------------------------
# Build services
# -------------------------------------------------

catalog = FunctionCatalog()
catalog.load_defaults()

alias_service = AliasService(catalog)

resolver = FunctionResolver(alias_service)

registry = UnknownFunctionRegistry()

importer = XLightsImporter(
    resolver,
    registry,
)

report = FixtureReport()

# -------------------------------------------------
# Load xLights file
# -------------------------------------------------

reader = XMLReader()

reader.load("xlights_rgbeffects.xml")

# -------------------------------------------------
# Import first moving head
# -------------------------------------------------

for model in reader.get_models():

    if not model.is_moving_head():
        continue

    fixture = importer.import_model(model)

    print(report.build(fixture))

    break

# -------------------------------------------------
# Unknown functions
# -------------------------------------------------

print()
print("----------------------------------------")
print("Unknown Functions")
print("----------------------------------------")

for function in registry.all():

    print(function)

print()
print(f"Unknown Function Count : {registry.count()}")