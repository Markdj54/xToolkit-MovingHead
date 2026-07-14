"""
effect_database.py

Stores all EffectDefinition objects contained within
an xLights sequence.
"""

from core.domain.effect_definition import EffectDefinition


class EffectDatabase:

    def __init__(self):

        self._effects = {}

    # ---------------------------------------------------------

    def add(self, effect: EffectDefinition):

        self._effects[effect.effect_id] = effect

    # ---------------------------------------------------------

    def get(self, effect_id: int):

        return self._effects.get(effect_id)

    # ---------------------------------------------------------

    def all(self):

        return self._effects.values()

    # ---------------------------------------------------------

    def count(self):

        return len(self._effects)

    # ---------------------------------------------------------

    def replace(self, effect: EffectDefinition):

        self._effects[effect.effect_id] = effect

    # ---------------------------------------------------------

    def translate(self, translator):

        translated = EffectDatabase()

        for effect in self.all():

            translated.add(
                translator.translate(effect)
            )

        return translated