"""
comparison_result.py

Represents one compared fixture function.
"""

from dataclasses import dataclass

from core.comparison_status import ComparisonStatus


@dataclass
class ComparisonResult:

    function: str

    source_channel: int | None = None

    destination_channel: int | None = None

    status: ComparisonStatus = ComparisonStatus.UNKNOWN

    def is_match(self):

        return self.status == ComparisonStatus.MATCH

    def is_different(self):

        return self.status == ComparisonStatus.DIFFERENT

    def is_missing(self):

        return self.status == ComparisonStatus.MISSING

    def is_extra(self):

        return self.status == ComparisonStatus.EXTRA

    def __str__(self):

        return (
            f"{self.function}: "
            f"{self.source_channel} -> "
            f"{self.destination_channel} "
            f"({self.status})"
        )