"""
function_resolver.py

Resolves fixture function names into canonical functions.
"""

from core.knowledge.function_keywords import (
    FUNCTION_KEYWORDS,
)

from core.services.alias_service import AliasService
from core.services.resolution_result import ResolutionResult


class FunctionResolver:

    def __init__(self, alias_service: AliasService):

        self.alias_service = alias_service

    def resolve(self, channel_name: str) -> ResolutionResult:

        result = self._exact_match(channel_name)

        if result.matched:
            return result

        result = self._keyword_match(channel_name)

        if result.matched:
            return result

        return self._unknown()

    def _exact_match(self, channel_name):

        function = self.alias_service.lookup(channel_name)

        if function:

            return ResolutionResult(
                matched=True,
                function=function,
                confidence=100,
                method="exact",
            )

        return self._unknown()

    def _keyword_match(self, channel_name):

        text = channel_name.lower()

        if "speed" in text:
            return self._unknown()

        for keyword, function in FUNCTION_KEYWORDS.items():

            if keyword in text:

                return ResolutionResult(
                    matched=True,
                    function=function,
                    confidence=85,
                    method="keyword",
                )

        return self._unknown()

    def _unknown(self):

        return ResolutionResult(
            matched=False,
            function=None,
            confidence=0,
            method="unknown",
        )