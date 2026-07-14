"""
effect_database.py

Loads EffectDB entries from an xLights sequence.

Version 1 only reads EffectDB.

Writing support will be added later.
"""

from core.domain.effect_definition import EffectDefinition


class EffectDatabase:

    def __init__(self):

        self.effects = {}

    # -------------------------------------------------------------

    def add(self, effect: EffectDefinition):

        self.effects[effect.effect_id] = effect

    # -------------------------------------------------------------

    def get(self, effect_id: int):

        return self.effects.get(effect_id)

    # -------------------------------------------------------------

    def contains(self, effect_id: int):

        return effect_id in self.effects

    # -------------------------------------------------------------

    def count(self):

        return len(self.effects)

    # -------------------------------------------------------------

    def all(self):

        return self.effects.values()

    # -------------------------------------------------------------

    def clear(self):

        self.effects.clear()