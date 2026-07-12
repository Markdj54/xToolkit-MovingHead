"""
unknown_function_registry.py

Stores unknown fixture functions discovered during imports.
"""


class UnknownFunctionRegistry:

    def __init__(self):

        self._unknown = set()

    def add(self, name: str):

        if name:
            self._unknown.add(name.strip())

    def all(self):

        return sorted(self._unknown)

    def count(self):

        return len(self._unknown)

    def clear(self):

        self._unknown.clear()