"""
fixture_report.py

Produces a human-readable report for a fixture.
"""

from core.domain.canonical_functions import *


class FixtureReport:

    ALL_FUNCTIONS = [

        PAN,
        PAN_FINE,

        TILT,
        TILT_FINE,

        PAN_TILT_SPEED,

        DIMMER,

        SHUTTER,

        COLOR,

        PRISM,

        PRISM_ROTATE,

        FOCUS,

        ZOOM,

        FROST,

        IRIS,

        GOBO,

        GOBO_ROTATE,
    ]

    def build(self, fixture):

        lines = []

        lines.append("=" * 40)
        lines.append("Fixture Report")
        lines.append("=" * 40)
        lines.append("")

        lines.append(f"Name : {fixture.name}")
        lines.append("")

        lines.append("Capabilities")
        lines.append("------------")

        for function in self.ALL_FUNCTIONS:

            if fixture.has(function):

                lines.append(f"✓ {function.display_name}")

        lines.append("")
        lines.append("Missing")
        lines.append("-------")

        missing = 0

        for function in self.ALL_FUNCTIONS:

            if not fixture.has(function):

                missing += 1

                lines.append(f"• {function.display_name}")

        recognised = len(self.ALL_FUNCTIONS) - missing

        coverage = recognised / len(self.ALL_FUNCTIONS) * 100

        lines.append("")
        lines.append(f"Coverage : {coverage:.1f}%")

        return "\n".join(lines)