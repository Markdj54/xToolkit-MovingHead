"""
sequence.py

Represents an xLights sequence inside xToolkit.

A Sequence owns every EffectDefinition contained within
the sequence.

Future versions will also include timing tracks,
display elements and sequence metadata.
"""

from dataclasses import dataclass, field

from core.domain.effect_definition import EffectDefinition


@dataclass
class Sequence:

    _effects: dict[int, EffectDefinition] = field(
        default_factory=dict
    )

    # ---------------------------------------------------------

    def add_effect(
        self,
        effect: EffectDefinition,
    ):

        self._effects[effect.effect_id] = effect

    # ---------------------------------------------------------

    def effect(
        self,
        effect_id: int,
    ):

        return self._effects.get(effect_id)

    # ---------------------------------------------------------

    def effects(self):

        return self._effects.values()

    # ---------------------------------------------------------

    def effect_count(self):

        return len(self._effects)

    # ---------------------------------------------------------

    def replace_effect(
        self,
        effect: EffectDefinition,
    ):

        self._effects[effect.effect_id] = effect