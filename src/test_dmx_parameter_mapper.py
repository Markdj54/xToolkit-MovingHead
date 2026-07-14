"""
test_dmx_parameter_mapper.py

Unit test for DMXParameterMapper.

This test deliberately avoids XML and builds a small
CanonicalFixture manually.
"""

from core.domain.canonical_fixture import CanonicalFixture
from core.domain.fixture_capability import FixtureCapability

from core.domain.canonical_functions import (
    PAN,
    TILT,
    DIMMER,
)

from core.services.dmx_parameter_mapper import DMXParameterMapper


# ---------------------------------------------------------
# Build test fixture
# ---------------------------------------------------------

fixture = CanonicalFixture("Test Fixture")

fixture.add_capability(
    FixtureCapability(
        function=PAN,
        channel=1,
    )
)

fixture.add_capability(
    FixtureCapability(
        function=TILT,
        channel=2,
    )
)

fixture.add_capability(
    FixtureCapability(
        function=DIMMER,
        channel=8,
    )
)

# ---------------------------------------------------------
# Create mapper
# ---------------------------------------------------------

mapper = DMXParameterMapper(fixture)

print()
print("=" * 60)
print("DMX PARAMETER MAPPER TEST")
print("=" * 60)
print()

tests = [
    "E_SLIDER_DMX1",
    "E_SLIDER_DMX2",
    "E_SLIDER_DMX8",
    "E_SLIDER_DMX99",
]

for parameter in tests:

    print(f"Parameter : {parameter}")

    channel = mapper.get_channel(parameter)

    print(f"Channel   : {channel}")

    capability = mapper.get_capability(parameter)

    if capability is None:
        print("Capability: NOT FOUND")
    else:
        print(f"Capability: {capability.function.id}")

    print()