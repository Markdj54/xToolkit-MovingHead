from core.xml_reader import XMLReader

from core.domain.function_catalog import FunctionCatalog

from core.services.alias_service import AliasService
from core.services.function_resolver import FunctionResolver
from core.services.unknown_function_registry import (
    UnknownFunctionRegistry,
)

from core.importers.xlights_importer import XLightsImporter


# ------------------------------------------
# Build services
# ------------------------------------------

catalog = FunctionCatalog()
catalog.load_defaults()

alias_service = AliasService(catalog)

resolver = FunctionResolver(alias_service)

registry = UnknownFunctionRegistry()

importer = XLightsImporter(
    resolver,
    registry,
)

# ------------------------------------------
# Read xLights XML
# ------------------------------------------

reader = XMLReader()

reader.load("xlights_rgbeffects.xml")

# ------------------------------------------
# Import first moving head
# ------------------------------------------

for model in reader.get_models():

    if not model.is_moving_head():
        continue

    fixture = importer.import_model(model)

    print("--------------------------------")
    print("Fixture:", fixture.name)
    print("--------------------------------")

    for capability in fixture.capabilities:

        print(
            f"{capability.channel:2d}  "
            f"{capability.function.display_name}"
        )

    break

# ------------------------------------------
# Display unknown functions
# ------------------------------------------

print()

print("--------------------------------")
print("Unknown Functions")
print("--------------------------------")

for name in registry.all():

    print(name)

print()

print(
    f"Unknown Function Count: "
    f"{registry.count()}"
)