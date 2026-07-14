"""
test_xsq_reader.py

Integration test for XSQReader.

Version 2 loads real EffectDefinition objects.
"""

from pathlib import Path

from core.services.xsq_reader import XSQReader


filename = (
    Path(__file__).parent.parent
    / "test_data"
    / "Knife Party - Internet Friends HD Layout.xsq"
)

reader = XSQReader()

sequence = reader.read(filename)

print()

print("=" * 60)
print("XSQ READER TEST")
print("=" * 60)
print()

print("Effects Loaded :", sequence.effect_count())

print()

first = sequence.effect(0)

print("First Effect")

print(first)

print()

print("Parameter Count :", first.parameter_count())

print()

print("Parameters")

print("-" * 40)

for name, value in sorted(first.parameters.items()):

    print(f"{name:<35} {value}")