"""
Tests the ParameterParser.
"""

from core.services.parameter_parser import ParameterParser


parser = ParameterParser()

text = (
    "E_CHECKBOX_INVDMX1=0,"
    "E_CHECKBOX_INVDMX2=0,"
    "E_NOTEBOOK1=Channels 1-16,"
    "E_SLIDER_DMX1=85,"
    "E_SLIDER_DMX2=0"
)

parameters = parser.parse(text)

print()

print("Parameters Found:", len(parameters))

print()

for key, value in parameters.items():
    print(f"{key:<30} {value}")