from core.services.effect_database import EffectDatabase
from core.domain.effect_definition import EffectDefinition


db = EffectDatabase()

effect = EffectDefinition(
    effect_id=131,
    effect_type="DMX"
)

effect.set("E_CHECKBOX_INVDMX1", "0")
effect.set("E_SLIDER_DMX1", "255")

db.add(effect)

print("Effects:", db.count())

loaded = db.get(131)

print(loaded)

print(loaded.get("E_SLIDER_DMX1"))