"""
comparison_status.py

Defines all comparison result states.
"""

from enum import Enum


class ComparisonStatus(Enum):

    MATCH = "Match"

    DIFFERENT = "Different Channel"

    MISSING = "Missing"

    EXTRA = "Extra"

    UNKNOWN = "Unknown"

    def __str__(self):

        return self.value