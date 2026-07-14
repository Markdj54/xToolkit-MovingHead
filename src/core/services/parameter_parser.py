"""
parameter_parser.py

Parses xLights effect parameter strings.

Example input:

E_SLIDER_DMX1=85,E_CHECKBOX_INVDMX1=0

Returns:

{
    "E_SLIDER_DMX1": "85",
    "E_CHECKBOX_INVDMX1": "0",
}
"""


class ParameterParser:

    def parse(self, text: str) -> dict[str, str]:

        parameters = {}

        if not text:
            return parameters

        entries = text.split(",")

        for entry in entries:

            entry = entry.strip()

            if "=" not in entry:
                continue

            key, value = entry.split("=", 1)

            parameters[key] = value

        return parameters