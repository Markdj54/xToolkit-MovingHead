"""
parameter_translator.py

Translates a single xLights DMX parameter from one fixture
to another.

Example

E_SLIDER_DMX1

↓

E_SLIDER_DMX6
"""

from core.domain.translation_map import TranslationMap

from core.services.dmx_parameter_mapper import (
    DMXParameterMapper,
)

from core.services.parameter_rewriter import (
    ParameterRewriter,
)


class ParameterTranslator:

    def __init__(
        self,
        mapper: DMXParameterMapper,
        translation_map: TranslationMap,
    ):

        self.mapper = mapper
        self.translation_map = translation_map

        self.rewriter = ParameterRewriter()

    # ---------------------------------------------------------

    def translate(
        self,
        parameter_name: str,
    ) -> str:

        capability = self.mapper.get_capability(
            parameter_name
        )

        if capability is None:
            return parameter_name

        destination_channel = (
            self.translation_map.destination_channel(
                capability.function
            )
        )

        if destination_channel is None:
            return parameter_name

        return self.rewriter.rewrite(
            parameter_name,
            destination_channel,
        )