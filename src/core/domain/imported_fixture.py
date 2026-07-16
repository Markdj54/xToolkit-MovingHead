"""
imported_fixture.py

Represents one imported fixture.

Contains both the canonical representation used by the
translation engine and the original xLights implementation
details.
"""

from dataclasses import dataclass

from core.domain.canonical_fixture import CanonicalFixture
from core.domain.moving_head_data import MovingHeadData


@dataclass
class ImportedFixture:

    canonical: CanonicalFixture

    moving_head: MovingHeadData