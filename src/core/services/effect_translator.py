"""
effect_translator.py

Translates all DMX parameters contained within a single
EffectDefinition.
"""

from core.domain.effect_definition import EffectDefinition
from core.services.parameter_translator import ParameterTranslator


class EffectTranslator:

    def __init__(
        self,
        parameter_translator: ParameterTranslator,
    ):

        self.parameter_translator = parameter_translator

    # ---------------------------------------------------------

    def translate(
        self,
        effect: EffectDefinition,
    ) -> EffectDefinition:

        translated = EffectDefinition(
            effect_id=effect.effect_id,
            effect_type=effect.effect_type,
        )

        #
        # Preserve original XML node.
        #

        if effect.has_xml_element():

            translated.set_xml_element(
                effect.xml_element()
            )

        #
        # Translate every parameter name.
        #

        for parameter, value in effect.parameters.items():

            new_parameter = (
                self.parameter_translator.translate(
                    parameter
                )
            )

            translated.set(
                new_parameter,
                value,
            )

        return translated