from dataclasses import dataclass

from core.domain.fixture_categories import FixtureCategory


@dataclass(frozen=True)
class FixtureFunction:

    id: str

    display_name: str

    category: FixtureCategory

    importance: int