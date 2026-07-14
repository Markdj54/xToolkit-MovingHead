"""
test_effect_definition.py
"""

from core.domain.effect_definition import EffectDefinition

effect = EffectDefinition(
    effect_id=1,
    effect_type="Unknown",
)

effect.set("E_SLIDER_DMX1", "85")
effect.set("E_NOTEBOOK1", "Channels 1-16")

print()
print("=" * 60)
print("EFFECT DEFINITION TEST")
print("=" * 60)
print()

print("Moving Head :", effect.is_moving_head())

effect2 = EffectDefinition(
    effect_id=2,
    effect_type="Shockwave",
)

effect2.set("E_SLIDER_Shockwave_Accel", "0")

print("Moving Head :", effect2.is_moving_head())