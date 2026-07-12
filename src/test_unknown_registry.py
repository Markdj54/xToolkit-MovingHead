from core.services.unknown_function_registry import UnknownFunctionRegistry

registry = UnknownFunctionRegistry()

registry.add("Pan")
registry.add("Tilt")
registry.add("Pan")
registry.add("Color")

print("Count:", registry.count())

for name in registry.all():
    print(name)