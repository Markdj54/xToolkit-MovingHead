"""
resolution_result.py

Represents the result of resolving a fixture function.
"""

from dataclasses import dataclass

from core.domain.fixture_function import FixtureFunction


@dataclass
class ResolutionResult:

    matched: bool

    function: FixtureFunction | None

    confidence: int

    method: str

    @property
    def is_unknown(self):

        return not self.matched