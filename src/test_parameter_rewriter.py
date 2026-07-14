"""
test_parameter_rewriter.py

Unit tests for ParameterRewriter.
"""

from core.services.parameter_rewriter import (
    ParameterRewriter,
)

rewriter = ParameterRewriter()

tests = [

    ("E_SLIDER_DMX1", 6),

    ("E_SLIDER_DMX2", 8),

    ("E_CHECKBOX_INVDMX3", 14),

    ("E_SLIDER_DMX16", 1),

]

print()
print("=" * 60)
print("PARAMETER REWRITER TEST")
print("=" * 60)
print()

for parameter, destination in tests:

    rewritten = rewriter.rewrite(
        parameter,
        destination,
    )

    print(parameter)

    print("↓")

    print(rewritten)

    print()