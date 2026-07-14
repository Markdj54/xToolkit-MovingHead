from core.domain.function_catalog import FunctionCatalog
from core.domain.canonical_functions import COLOR, DIMMER
from core.services.alias_service import AliasService

catalog = FunctionCatalog()
catalog.load_defaults()

alias = AliasService(catalog)

alias.add_alias("Colour Wheel", COLOR)
alias.add_alias("Intensity", DIMMER)

print(alias.lookup("Pan"))
print(alias.lookup("Colour Wheel"))
print(alias.lookup("Intensity"))
print(alias.lookup("Unknown"))

print(f"Alias count: {alias.count()}")