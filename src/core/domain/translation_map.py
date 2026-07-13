"""
translation_map.py

Stores the channel translation required to convert one
fixture into another.
"""

from dataclasses import dataclass, field

from core.domain.fixture_function import FixtureFunction
from core.domain.translation_entry import TranslationEntry


@dataclass
class TranslationMap:

    source_fixture: str

    destination_fixture: str

    entries: list[TranslationEntry] = field(default_factory=list)

    def add(self, entry: TranslationEntry):

        self.entries.append(entry)

    def find(self, function: FixtureFunction):

        for entry in self.entries:

            if entry.function.id == function.id:
                return entry

        return None

    def destination_channel(self, function: FixtureFunction):

        entry = self.find(function)

        if entry:
            return entry.destination_channel

        return None

    def translated_count(self):

        return sum(
            1
            for entry in self.entries
            if entry.translated
        )

    def __len__(self):

        return len(self.entries)

    def __iter__(self):

        return iter(self.entries)