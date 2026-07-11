"""
comparison_report.py

Contains the complete comparison report.
"""

from core.comparison_statistics import ComparisonStatistics


class ComparisonReport:

    def __init__(self):

        self.results = []

        self.statistics = ComparisonStatistics()

    def add(self, result):

        self.results.append(result)

    def __len__(self):

        return len(self.results)

    def __iter__(self):

        return iter(self.results)