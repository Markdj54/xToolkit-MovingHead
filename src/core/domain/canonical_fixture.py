"""
canonical_fixture.py

The internal representation of a lighting fixture.

All importers convert their native fixture format into this
canonical representation before comparison.
"""

from dataclasses import dataclass, field

from core.domain.fixture_capability import FixtureCapability


@dataclass
class CanonicalFixture:

    name: str

    manufacturer: str = ""

    model: str = ""

    mode: str = ""

    capabilities: list[FixtureCapability] = field(default_factory=list)

    # ---------------------------------------------------------

    def add_capability(
        self,
        capability: FixtureCapability,
    ):

        self.capabilities.append(capability)

    # ---------------------------------------------------------

    def has(self, function):

        return any(
            c.function.id == function.id
            for c in self.capabilities
        )

    # ---------------------------------------------------------

    def capability(self, function):

        for capability in self.capabilities:

            if capability.function.id == function.id:
                return capability

        return None

    # ---------------------------------------------------------

    def capability_by_channel(self, channel):

        for capability in self.capabilities:

            if capability.channel == channel:
                return capability

        return None

    # ---------------------------------------------------------

    def channel_of(self, function):

        capability = self.capability(function)

        if capability:
            return capability.channel

        return None