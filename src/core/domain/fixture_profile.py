"""
fixture_profile.py

Represents what a fixture can do.

This is independent of DMX channel numbers.
"""

from dataclasses import dataclass, field

from core.domain.fixture_function import FixtureFunction


@dataclass
class FixtureProfile:

    name: str

    manufacturer: str = ""

    model: str = ""

    mode: str = ""

    capabilities: list[FixtureFunction] = field(default_factory=list)

    def add(self, function: FixtureFunction):

        if function not in self.capabilities:
            self.capabilities.append(function)

    def has(self, function: FixtureFunction):

        return function in self.capabilities

    def count(self):

        return len(self.capabilities)

    def sorted_capabilities(self):

        return sorted(
            self.capabilities,
            key=lambda f: (
                f.category.value,
                -f.importance,
                f.display_name
            )
        )