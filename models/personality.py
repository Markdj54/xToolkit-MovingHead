from dataclasses import dataclass, field

from .channel import Channel


@dataclass
class Personality:
    channels: list[Channel] = field(default_factory=list)