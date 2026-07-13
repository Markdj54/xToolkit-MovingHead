"""
function_catalog.py

Stores and looks up canonical fixture functions.
"""

from core.domain.canonical_functions import *


class FunctionCatalog:

    def __init__(self):

        self._functions = {}
        self._aliases = {}

    def register(self, function):

        self._functions[function.id] = function

        self.register_alias(
            function.display_name,
            function
        )

    def register_alias(self, alias, function):

        self._aliases[alias.strip().lower()] = function

    def lookup(self, text):

        if not text:
            return None

        return self._aliases.get(
            text.strip().lower()
        )

    def by_id(self, id):

        return self._functions.get(id)

    def exists(self, id):

        return id in self._functions

    def count(self):

        return len(self._functions)

    def all(self):

        return list(self._functions.values())

    def alias_count(self):

        return len(self._aliases)

    def load_defaults(self):

        # Movement
        self.register(PAN)
        self.register(PAN_FINE)
        self.register(TILT)
        self.register(TILT_FINE)
        self.register(PAN_TILT_SPEED)

        # Beam
        self.register(DIMMER)
        self.register(SHUTTER)
        self.register(FOCUS)
        self.register(ZOOM)
        self.register(FROST)
        self.register(IRIS)

        # Colour
        self.register(COLOR)

        # Gobos
        self.register(GOBO)
        self.register(GOBO_ROTATE)

        # Effects
        self.register(PRISM)
        self.register(PRISM_ROTATE)

        # Control
        self.register(RESET)
        self.register(MACRO)
        self.register(UNUSED)