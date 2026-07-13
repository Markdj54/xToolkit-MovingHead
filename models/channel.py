from dataclasses import dataclass
from typing import Optional

from .wheel import Wheel


@dataclass
class Channel:
    number: int
    name: str
    channel_type: str = "UNKNOWN"
    wheel: Optional[Wheel] = None