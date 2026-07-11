from core.domain.function_catalog import FunctionCatalog
from core.domain.standard_functions import COLOR, DIMMER
from core.services.alias_service import AliasService

catalog = FunctionCatalog()
catalog.load_defaults()

alias = AliasService(catalog)

alias.add_alias("Colour Wheel", COLOR)
alias.add_alias("Intensity", DIMMER)

print("Pan:", alias.lookup("Pan"))
print("Colour Wheel:", alias.lookup("Colour Wheel"))
print("Intensity:", alias.lookup("Intensity"))
print("Unknown:", alias.lookup("Unknown"))

print("Alias Count:", alias.count())