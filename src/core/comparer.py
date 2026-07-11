"""
xToolkit v0.3.1

Fixture Comparison Engine
"""

from core.fixture_dictionary import normalise_function


class ComparisonResult:

    def __init__(self):

        self.score = 0

        self.matches = []

        self.missing = []

        self.extra = []


class FixtureComparer:

    def compare(self, source, destination):

        result = ComparisonResult()

        source_functions = []
        destination_functions = []

        # -----------------------------
        # Read source fixture
        # -----------------------------

        for channel in range(1, source.channel_count + 1):

            function = normalise_function(
                source.get_channel_name(channel)
            )

            source_functions.append(function)

        # -----------------------------
        # Read destination fixture
        # -----------------------------

        for channel in range(1, destination.channel_count + 1):

            function = normalise_function(
                destination.get_channel_name(channel)
            )

            destination_functions.append(function)

        # -----------------------------
        # Find matches
        # -----------------------------

        for function in source_functions:

            if function in destination_functions:

                result.matches.append(function)

            else:

                result.missing.append(function)

        # -----------------------------
        # Find extra functions
        # -----------------------------

        for function in destination_functions:

            if function not in source_functions:

                result.extra.append(function)

        # -----------------------------
        # Compatibility score
        # -----------------------------

        total = max(
            len(source_functions),
            len(destination_functions)
        )

        if total > 0:

            result.score = round(
                len(result.matches) / total * 100
            )

        return result