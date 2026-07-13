from dataclasses import dataclass, field
from typing import Optional

from .personality import Personality


@dataclass
class MovingHead:
    name: str
    vendor: str = ""
    channel_count: int = 0
    personality: Optional[Personality] = None