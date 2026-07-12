from core.domain.function_catalog import FunctionCatalog

from core.services.alias_service import AliasService
from core.services.function_resolver import FunctionResolver


catalog = FunctionCatalog()
catalog.load_defaults()

alias_service = AliasService(catalog)

resolver = FunctionResolver(alias_service)

tests = [

    "Pan",

    "Pan Fine",

    "Color",

    "Pan / X-axis / Horizontal",

    "Tilt / Y-axis / Vertical",

    "Dimmer / Intensity",

    "Shutter / Strobe",

    "Pan & Tilt Speed",

    "Unknown",

]

for name in tests:

    result = resolver.resolve(name)

    print("--------------------------------")

    print(name)

    print("Matched:", result.matched)

    print("Method:", result.method)

    print("Confidence:", result.confidence)

    if result.function:

        print("Function:", result.function.display_name)

    else:

        print("Function: None")