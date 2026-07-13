"""
translation_builder.py

Builds a TranslationMap between two CanonicalFixtures.
"""

from core.domain.translation_map import TranslationMap
from core.domain.translation_entry import TranslationEntry


class TranslationBuilder:

    """
    Creates the channel translation required to convert
    one fixture into another.
    """

    def build(
        self,
        source_fixture,
        destination_fixture,
    ):

        translation = TranslationMap(
            source_fixture=source_fixture.name,
            destination_fixture=destination_fixture.name,
        )

        #
        # Walk every capability in the imported fixture.
        #

        for source in source_fixture.capabilities:

            destination = destination_fixture.capability(
                source.function
            )

            #
            # Function exists in both fixtures.
            #

            if destination:

                translation.add(

                    TranslationEntry(

                        function=source.function,

                        source_channel=source.channel,

                        destination_channel=destination.channel,

                        translated=True,

                    )

                )

            #
            # Destination fixture does not support it.
            #

            else:

                translation.add(

                    TranslationEntry(

                        function=source.function,

                        source_channel=source.channel,

                        destination_channel=-1,

                        translated=False,

                        notes="Function not available",

                    )

                )

        return translation