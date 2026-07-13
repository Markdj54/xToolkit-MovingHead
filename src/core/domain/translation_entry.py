"""
translation_entry.py

Represents one translated lighting function between
an imported fixture and a destination fixture.
"""

from dataclasses import dataclass

from core.domain.fixture_function import FixtureFunction


@dataclass
class TranslationEntry:

    function: FixtureFunction

    source_channel: int

    destination_channel: int

    translated: bool = True

    notes: str = ""

    def __str__(self):

        return (
            f"{self.function.display_name}: "
            f"{self.source_channel} -> "
            f"{self.destination_channel}"
        )