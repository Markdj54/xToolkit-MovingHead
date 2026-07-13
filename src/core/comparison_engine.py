"""
comparison_engine.py

Compares two CanonicalFixture objects and produces a
ComparisonReport.
"""

from core.comparison_report import ComparisonReport
from core.comparison_result import ComparisonResult
from core.comparison_status import ComparisonStatus


class ComparisonEngine:
    """
    Compares two CanonicalFixture objects.

    The comparison is performed using canonical lighting
    functions rather than manufacturer channel names.
    """

    def compare(self, source, destination):

        report = ComparisonReport()

        #
        # Build lookup dictionaries
        #

        source_functions = {
            capability.function.id: capability
            for capability in source.capabilities
        }

        destination_functions = {
            capability.function.id: capability
            for capability in destination.capabilities
        }

        #
        # Compare every function found in either fixture
        #

        all_functions = sorted(
            set(source_functions.keys())
            | set(destination_functions.keys())
        )

        for function_id in all_functions:

            source_capability = source_functions.get(function_id)
            destination_capability = destination_functions.get(function_id)

            #
            # Determine comparison status
            #

            if source_capability and destination_capability:

                if (
                    source_capability.channel
                    == destination_capability.channel
                ):

                    status = ComparisonStatus.MATCH

                    report.statistics.matches += 1

                else:

                    status = ComparisonStatus.DIFFERENT

                    report.statistics.different += 1

                source_channel = source_capability.channel
                destination_channel = destination_capability.channel

            elif source_capability:

                status = ComparisonStatus.MISSING

                report.statistics.missing += 1

                source_channel = source_capability.channel
                destination_channel = None

            else:

                status = ComparisonStatus.EXTRA

                report.statistics.extra += 1

                source_channel = None
                destination_channel = destination_capability.channel

            report.add(

                ComparisonResult(

                    function=function_id,

                    source_channel=source_channel,

                    destination_channel=destination_channel,

                    status=status,

                )

            )

        #
        # Compatibility score
        #

        total = report.statistics.total()

        if total:

            report.statistics.compatibility = round(

                (
                    report.statistics.matches
                    / total
                )
                * 100,

                1,

            )

        return report