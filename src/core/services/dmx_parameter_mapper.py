"""
dmx_parameter_mapper.py

Maps xLights DMX parameter names to canonical fixture
capabilities.

Example

E_SLIDER_DMX1
        ↓
Channel 1
        ↓
PAN
"""

import re

from core.domain.canonical_fixture import CanonicalFixture


class DMXParameterMapper:

    def __init__(self, fixture: CanonicalFixture):

        self.fixture = fixture

    # ---------------------------------------------------------

    def is_dmx_parameter(self, parameter_name: str) -> bool:

        return parameter_name.startswith("E_SLIDER_DMX")

    # ---------------------------------------------------------

    def get_channel(self, parameter_name: str):

        match = re.search(r"DMX(\d+)", parameter_name)

        if match is None:
            return None

        return int(match.group(1))

    # ---------------------------------------------------------

    def get_capability(self, parameter_name: str):

        channel = self.get_channel(parameter_name)

        if channel is None:
            return None

        return self.fixture.capability_by_channel(channel)