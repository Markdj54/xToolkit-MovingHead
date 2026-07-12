"""
xlights_importer.py

Converts xLights models into CanonicalFixture objects.
"""

from core.domain.canonical_fixture import CanonicalFixture
from core.domain.fixture_capability import FixtureCapability
from core.services.alias_service import AliasService


class XLightsImporter:

    def __init__(self, alias_service: AliasService):
        self.alias_service = alias_service

    def import_model(self, model) -> CanonicalFixture:

        fixture = CanonicalFixture(
            name=model.name
        )

        # Walk every DMX channel
        for channel in range(1, model.channel_count + 1):

            channel_name = model.get_channel_name(channel)

            function = self.alias_service.lookup(channel_name)

            if function is None:
                print(
                    f"Unknown Channel {channel}: "
                    f"'{channel_name}'"
         )
            continue

            capability = FixtureCapability(
                function=function,
                channel=channel
            )

            fixture.add_capability(capability)

        return fixture