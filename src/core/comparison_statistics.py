"""
comparison_statistics.py

Stores comparison totals and compatibility score.
"""

from dataclasses import dataclass


@dataclass
class ComparisonStatistics:

    matches: int = 0

    different: int = 0

    missing: int = 0

    extra: int = 0

    compatibility: float = 0.0

    def total(self):

        return (
            self.matches +
            self.different +
            self.missing +
            self.extra
        )