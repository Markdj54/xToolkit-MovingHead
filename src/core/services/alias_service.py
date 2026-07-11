"""
xToolkit-MovingHead

alias_service.py

Translates manufacturer-specific function names into
canonical FixtureFunctions.
"""

from core.domain.function_catalog import FunctionCatalog


class AliasService:

    def __init__(self, catalog: FunctionCatalog):

        self.catalog = catalog

    def lookup(self, name: str):

        if not name:
            return None

        return self.catalog.lookup(name)

    def has_alias(self, name: str):

        return self.lookup(name) is not None

    def add_alias(self, alias: str, function):

        self.catalog.register_alias(alias, function)

    def count(self):

        return self.catalog.alias_count()