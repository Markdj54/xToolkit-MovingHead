"""
inspect_models.py

Lists every moving head model found in rgbeffects.xml.
"""

from core.services.rgbeffects_reader import RGBEffectsReader


RGBEFFECTS = (
    r"C:\Users\User\xlightsMHConvertor\test_data\xlights_rgbeffects Copy.xml"
)


def main():

    reader = RGBEffectsReader()

    models = reader.load(RGBEFFECTS)

    print()
    print("--------------------------------")
    print("Moving Head Models")
    print("--------------------------------")
    print()

    count = 0

    for model in models:

        if model.is_moving_head():

            print(f"Name      : {model.name}")
            print(f"Channels  : {model.channel_count}")

            print("Functions:")

            for channel in range(
                1,
                model.channel_count + 1,
            ):

                print(
                    f"  {channel:2d}  "
                    f"{model.get_channel_name(channel)}"
                )

            print()

            count += 1

    print(f"Models Found : {count}")


if __name__ == "__main__":

    main()