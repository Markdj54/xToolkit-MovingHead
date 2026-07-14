"""
test_parameter_translator.py

Integration test for ParameterTranslator.
"""

from core.domain.canonical_fixture import CanonicalFixture
from core.domain.fixture_capability import FixtureCapability

from core.domain.canonical_functions import (
    PAN,
    TILT,
    DIMMER,
)

from core.domain.translation_map import TranslationMap
from core.domain.translation_entry import TranslationEntry

from core.services.dmx_parameter_mapper import (
    DMXParameterMapper,
)

from core.services.parameter_translator import (
    ParameterTranslator,
)

#
# ----------------------------------------------------------
# Build source fixture
# ----------------------------------------------------------
#

fixture = CanonicalFixture("Source Fixture")

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

#
# ----------------------------------------------------------
# Build translation map
# ----------------------------------------------------------
#

translation = TranslationMap(
    "Source",
    "Destination",
)

translation.add(

    TranslationEntry(

        function=PAN,

        source_channel=1,

        destination_channel=6,

        translated=True,
    )
)

translation.add(

    TranslationEntry(

        function=TILT,

        source_channel=2,

        destination_channel=7,

        translated=True,
    )
)

translation.add(

    TranslationEntry(

        function=DIMMER,

        source_channel=8,

        destination_channel=3,

        translated=True,
    )
)

#
# ----------------------------------------------------------
# Translator
# ----------------------------------------------------------
#

mapper = DMXParameterMapper(fixture)

translator = ParameterTranslator(
    mapper,
    translation,
)

tests = [

    "E_SLIDER_DMX1",

    "E_SLIDER_DMX2",

    "E_SLIDER_DMX8",

    "E_SLIDER_DMX99",
]

print()
print("=" * 60)
print("PARAMETER TRANSLATOR TEST")
print("=" * 60)
print()

for parameter in tests:

    translated = translator.translate(parameter)

    print(parameter)

    print("↓")

    print(translated)

    print()