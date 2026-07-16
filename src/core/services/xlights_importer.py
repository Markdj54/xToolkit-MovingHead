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

    #
    # DmxMovingHead3D attribute -> canonical alias
    #

    DMX3D_CHANNELS = {
        "DmxPanChannel": "Pan",
        "DmxTiltChannel": "Tilt",
        "DmxDimmerChannel": "Dimmer",
        "DmxShutterChannel": "Shutter",
        "DmxColorWheelChannel": "Color",
    }

    # ---------------------------------------------------------

    def __init__(
        self,
        resolver: FunctionResolver,
        registry: UnknownFunctionRegistry,
    ):

        self.resolver = resolver
        self.registry = registry

    # ---------------------------------------------------------

    def import_model(self, model) -> CanonicalFixture:

        if model.display_as == "DmxMovingHead3D":
            return self._import_dmx_moving_head_3d(model)

        return self._import_dmx_moving_head_adv(model)

    # ---------------------------------------------------------

    def _import_dmx_moving_head_adv(
        self,
        model,
    ) -> CanonicalFixture:

        fixture = CanonicalFixture(
            name=model.name
        )

        for channel in range(1, model.channel_count + 1):

            channel_name = model.get_channel_name(channel)

            result = self.resolver.resolve(
                channel_name
            )

            if result.is_unknown:

                self.registry.add(channel_name)

                continue

            capability = FixtureCapability(
                function=result.function,
                channel=channel,
            )

            fixture.add_capability(
                capability
            )

        return fixture

    # ---------------------------------------------------------

    def _import_dmx_moving_head_3d(
        self,
        model,
    ) -> CanonicalFixture:

        fixture = CanonicalFixture(
            name=model.name
        )

        for attribute, alias in self.DMX3D_CHANNELS.items():

            value = model.get(attribute)

            if not value:
                continue

            try:

                channel = int(value)

            except ValueError:

                continue

            result = self.resolver.resolve(
                alias
            )

            if result.is_unknown:

                self.registry.add(alias)

                continue

            capability = FixtureCapability(
                function=result.function,
                channel=channel,
            )

            fixture.add_capability(
                capability
            )

        return fixture