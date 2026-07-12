"""
xlights_importer.py

Converts xLights models into CanonicalFixture objects.
"""

from core.domain.canonical_fixture import CanonicalFixture
from core.domain.fixture_capability import FixtureCapability

from core.services.function_resolver import FunctionResolver
from core.services.unknown_function_registry import (
    UnknownFunctionRegistry,
)


class XLightsImporter:

    def __init__(
        self,
        resolver: FunctionResolver,
        registry: UnknownFunctionRegistry,
    ):

        self.resolver = resolver
        self.registry = registry

    def import_model(self, model) -> CanonicalFixture:

        fixture = CanonicalFixture(
            name=model.name
        )

        for channel in range(1, model.channel_count + 1):

            channel_name = model.get_channel_name(channel)

            result = self.resolver.resolve(channel_name)

            if result.is_unknown:

                self.registry.add(channel_name)

                continue

            capability = FixtureCapability(
                function=result.function,
                channel=channel,
            )

            fixture.add_capability(capability)

        return fixture