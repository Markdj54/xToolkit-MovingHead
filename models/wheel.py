from dataclasses import dataclass, field


@dataclass
class WheelSlot:
    start: int
    end: int
    label: str
    metadata: dict = field(default_factory=dict)


@dataclass
class Wheel:
    wheel_type: str
    slots: list[WheelSlot] = field(default_factory=list)