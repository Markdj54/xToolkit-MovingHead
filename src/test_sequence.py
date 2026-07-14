"""
test_sequence.py

Unit tests for Sequence.
"""

from core.domain.sequence import Sequence
from core.domain.effect_definition import EffectDefinition


sequence = Sequence()

print()
print("=" * 60)
print("SEQUENCE TEST")
print("=" * 60)
print()

for effect_id in (10, 20, 30):

    effect = EffectDefinition(
        effect_id=effect_id,
        effect_type="DMX",
    )

    sequence.add_effect(effect)

print("Effects Stored :", sequence.effect_count())

print()

print("Effect IDs")

for effect in sequence.effects():

    print(effect.effect_id)