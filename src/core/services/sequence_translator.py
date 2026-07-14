"""
sequence_translator.py

Translates every moving head effect contained within
a Sequence.
"""

from core.domain.sequence import Sequence
from core.services.effect_translator import EffectTranslator


class SequenceTranslator:

    def __init__(
        self,
        effect_translator: EffectTranslator,
    ):

        self.effect_translator = effect_translator

    # ---------------------------------------------------------

    def translate(
        self,
        sequence: Sequence,
    ) -> Sequence:

        translated = Sequence()

        for effect in sequence.effects():

            if effect.is_moving_head():

                translated.add_effect(
                    self.effect_translator.translate(effect)
                )

            else:

                translated.add_effect(effect)

        return translated