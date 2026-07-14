"""
parameter_rewriter.py

Rewrites xLights DMX parameter names to use a different
DMX channel.

Example

E_SLIDER_DMX1

↓

E_SLIDER_DMX6
"""

import re


class ParameterRewriter:

    # ---------------------------------------------------------

    def rewrite(
        self,
        parameter_name: str,
        destination_channel: int,
    ) -> str:

        if destination_channel is None:
            return parameter_name

        return re.sub(
            r"DMX\d+",
            f"DMX{destination_channel}",
            parameter_name,
        )