"""
comparison_result.py

Represents the comparison of one fixture function.
"""

from dataclasses import dataclass


@dataclass
class ComparisonResult:
    """Represents one compared function."""

    function: str

    source_channel: int | None = None

    destination_channel: int | None = None

    status: str = "UNKNOWN"

    def is_match(self):
        return self.status == "MATCH"

    def is_different(self):
        return self.status == "DIFFERENT"

    def is_missing(self):
        return self.status == "MISSING"

    def is_extra(self):
        return self.status == "EXTRA"