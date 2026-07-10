from core.xml_reader import XMLReader

reader = XMLReader()

reader.load("K:/Xlights Shows/Halloween 24/xlights_rgbeffects.xml")

print(reader.count())

print()

for model in reader.get_moving_heads():

    print(model.name, model.display_as)