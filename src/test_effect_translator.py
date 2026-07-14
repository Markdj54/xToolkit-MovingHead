"""
test_effect_translator.py

Integration test for EffectTranslator.
"""

from core.domain.effect_definition import EffectDefinition

from core.domain.canonical_fixture import CanonicalFixture
from core.domain.fixture_capability import FixtureCapability

from core.domain.canonical_functions import (
    PAN,
    TILT,
    DIMMER,
)

from core.domain.translation_map import TranslationMap
from core.domain.translation_entry import TranslationEntry

from core.services.dmx_parameter_mapper import DMXParameterMapper
from core.services.parameter_translator import ParameterTranslator
from core.services.effect_translator import EffectTranslator


# ---------------------------------------------------------
# Source Fixture
# ---------------------------------------------------------

fixture = CanonicalFixture("Source")

fixture.add_capability(
    FixtureCapability(PAN, 1)
)

fixture.add_capability(
    FixtureCapability(TILT, 2)
)

fixture.add_capability(
    FixtureCapability(DIMMER, 8)
)

# ---------------------------------------------------------
# Translation Map
# ---------------------------------------------------------

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

# ---------------------------------------------------------
# Translator
# ---------------------------------------------------------

mapper = DMXParameterMapper(fixture)

parameter_translator = ParameterTranslator(
    mapper,
    translation,
)

translator = EffectTranslator(
    parameter_translator,
)

# ---------------------------------------------------------
# Build Effect
# ---------------------------------------------------------

effect = EffectDefinition(
    effect_id=1,
    effect_type="DMX",
)

effect.set("E_SLIDER_DMX1", "85")
effect.set("E_SLIDER_DMX2", "120")
effect.set("E_SLIDER_DMX8", "255")
effect.set("E_CHECKBOX_INVDMX1", "0")
effect.set("E_NOTEBOOK1", "Channels 1-16")

translated = translator.translate(effect)

print()
print("=" * 60)
print("EFFECT TRANSLATOR TEST")
print("=" * 60)
print()

for key in sorted(translated.parameters):

    print(f"{key:<28} {translated.parameters[key]}")