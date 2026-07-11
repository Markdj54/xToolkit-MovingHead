"""
fixture_capability.py

Represents one capability of a lighting fixture.
"""

from dataclasses import dataclass

from core.domain.fixture_function import FixtureFunction


@dataclass
class FixtureCapability:

    function: FixtureFunction

    channel: int

    fine_channel: int | None = None

    default_value: int = 0

    supports_16bit: bool = False

    notes: str = ""