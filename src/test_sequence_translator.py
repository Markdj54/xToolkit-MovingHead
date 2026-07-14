"""
test_sequence_translator.py

Integration test for SequenceTranslator.
"""

from core.domain.sequence import Sequence
from core.domain.effect_definition import EffectDefinition

from core.domain.canonical_fixture import CanonicalFixture
from core.domain.fixture_capability import FixtureCapability

from core.domain.canonical_functions import (
    PAN,
    TILT,
)

from core.domain.translation_map import TranslationMap
from core.domain.translation_entry import TranslationEntry

from core.services.dmx_parameter_mapper import DMXParameterMapper
from core.services.parameter_translator import ParameterTranslator
from core.services.effect_translator import EffectTranslator
from core.services.sequence_translator import SequenceTranslator


#
# Source Fixture
#

fixture = CanonicalFixture("Source")

fixture.add_capability(
    FixtureCapability(PAN, 1)
)

fixture.add_capability(
    FixtureCapability(TILT, 2)
)

#
# Translation Map
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

#
# Build Sequence
#

sequence = Sequence()

#
# Moving Head Effect
#

effect = EffectDefinition(
    effect_id=1,
    effect_type="Unknown",
)

effect.set("E_SLIDER_DMX1", "85")
effect.set("E_SLIDER_DMX2", "120")

sequence.add_effect(effect)

#
# Normal xLights Effect
#

effect2 = EffectDefinition(
    effect_id=2,
    effect_type="Shockwave",
)

effect2.set(
    "E_SLIDER_Shockwave_Accel",
    "25",
)

sequence.add_effect(effect2)

#
# Translate
#

mapper = DMXParameterMapper(fixture)

parameter = ParameterTranslator(
    mapper,
    translation,
)

effect_translator = EffectTranslator(
    parameter,
)

translator = SequenceTranslator(
    effect_translator,
)

translated = translator.translate(sequence)

print()
print("=" * 60)
print("SEQUENCE TRANSLATOR TEST")
print("=" * 60)
print()

for effect in translated.effects():

    print()

    print(f"Effect {effect.effect_id}")

    for key in sorted(effect.parameters):

        print(f"  {key} = {effect.parameters[key]}")