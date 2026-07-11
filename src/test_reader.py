from core.xml_reader import XMLReader

reader = XMLReader()

reader.load("K:/Xlights Shows/Halloween 24/xlights_rgbeffects.xml")

print(reader.count())

print()

for model in reader.get_moving_heads():

    print(model.name, model.display_as)

    print()
print("DMX Channels")
print("----------------")

mh = reader.get_model("MH1")

for channel in range(1, mh.channel_count + 1):

    print(channel, "-", mh.get_channel_name(channel))

print()
print("Fixture Summary")
print("----------------")

summary = mh.get_summary()

for key, value in summary.items():
    print(f"{key:15} : {value}")