from core.services.xsq_reader import XSQReader

reader = XSQReader()

effects = reader.read(
    "Knife Party - Internet Friends HD Layout.xsq"
)

print()

print("Effects Loaded:", len(effects))

print()

first = next(iter(effects.values()))

print(first)