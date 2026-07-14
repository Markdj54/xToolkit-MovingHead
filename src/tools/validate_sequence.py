"""
validate_sequence.py

Validates a real xLights sequence.

Usage:

py -m tools.validate_sequence "test_data\\MySequence.xsq"
"""

from pathlib import Path
import sys

from core.services.xsq_reader import XSQReader


# ---------------------------------------------------------

if len(sys.argv) < 2:

    print()
    print("Usage:")
    print()
    print('py -m tools.validate_sequence "test_data\\MySequence.xsq"')
    print()

    raise SystemExit(1)

# ---------------------------------------------------------

project_root = Path(__file__).resolve().parent.parent.parent

filename = Path(sys.argv[1])

if not filename.is_absolute():

    filename = project_root / filename

if not filename.exists():

    print()
    print(f"File not found:\n{filename}")
    raise SystemExit(1)

# ---------------------------------------------------------

print()
print("=" * 60)
print("xToolkit Sequence Validation")
print("=" * 60)
print()

reader = XSQReader()

sequence = reader.read(filename)

total_effects = sequence.effect_count()

moving_head_effects = 0

total_parameters = 0

dmx_parameters = 0

parameter_names = {}

for effect in sequence.effects():

    total_parameters += effect.parameter_count()

    if effect.is_moving_head():

        moving_head_effects += 1

    for name in effect.parameters:

        parameter_names[name] = (
            parameter_names.get(name, 0) + 1
        )

        if "_DMX" in name:

            dmx_parameters += 1

print()
print(f"Sequence              : {filename.name}")
print(f"Total Effects         : {total_effects}")
print(f"Moving Head Effects   : {moving_head_effects}")
print(f"Total Parameters      : {total_parameters}")
print(f"DMX Parameters        : {dmx_parameters}")

print()
print("-" * 60)
print("DMX Parameters Found")
print("-" * 60)

for name in sorted(parameter_names):

    if "_DMX" in name:

        print(
            f"{name:<35}{parameter_names[name]}"
        )

print()
print("Validation Complete")