from core.xml_reader import XMLReader
from core.domain.function_catalog import FunctionCatalog
from core.services.alias_service import AliasService
from core.importers.xlights_importer import XLightsImporter


reader = XMLReader()

reader.load("xlights_rgbeffects.xml")

catalog = FunctionCatalog()
catalog.load_defaults()

alias = AliasService(catalog)

importer = XLightsImporter(alias)

for model in reader.get_models():

    if model.is_moving_head():

        fixture = importer.import_model(model)

        print("--------------------------------")
        print(fixture.name)

        for capability in fixture.capabilities:
            print(
                capability.channel,
                capability.function.display_name
            )

        break