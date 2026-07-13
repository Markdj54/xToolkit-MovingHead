# xToolkit-MovingHead

# Coding Standards

Version 1.0

---

# Philosophy

The code should be easy to read.

Optimise for readability before cleverness.

If someone unfamiliar with the project can understand a class after five minutes, we've done a good job.

---

# File Names

Python files use snake_case.

Examples

canonical_fixture.py

fixture_capability.py

fixture_function.py

fixture_category.py

function_catalog.py

standard_functions.py

alias_service.py

xlights_importer.py

comparison_engine.py

xml_reader.py

---

# Classes

Classes use PascalCase.

Examples

CanonicalFixture

FixtureCapability

FixtureFunction

FixtureCategory

FunctionCatalog

AliasService

XMLReader

XLightsImporter

ComparisonEngine

---

# Functions and Methods

Use snake_case.

Examples

load()

lookup()

register_alias()

import_model()

channel_name()

get_models()

is_moving_head()

---

# Variables

Use descriptive snake_case names.

Good

channel_name

fixture_name

start_channel

layout_group

manufacturer

function

capability

Avoid

fn

cap

tmp

obj

x

---

# Private Members

Private attributes begin with an underscore.

Example

self._functions

self._aliases

self._models

---

# Constants

Constants use UPPER_CASE.

Examples

PAN

PAN_FINE

TILT

TILT_FINE

DIMMER

SHUTTER

COLOR

GOBO

PRISM

PRISM_ROTATE

FOCUS

ZOOM

FROST

---

# Canonical Function IDs

Canonical IDs are always uppercase.

Examples

PAN

PAN_FINE

COLOR

DIMMER

These IDs are the language spoken internally by xToolkit.

---

# Display Names

Display names are user friendly.

Examples

Pan

Pan Fine

Tilt

Tilt Fine

Color

Dimmer

Shutter

---

# XML

Never rename xLights XML attributes.

Examples

DisplayAs

NodeNames

DmxChannelCount

StartChannel

The importer is responsible for translating XML into the canonical model.

---

# Comments

Explain WHY.

Avoid comments that explain WHAT.

Good

# Ignore unused DMX channels

Poor

# Increment i

---

# Type Hints

Use type hints whenever they improve readability.

Example

def import_model(self, model) -> CanonicalFixture:

Type hints are recommended but not required during early development.

---

# Docstrings

Every public class should have a short docstring.

Example

"""
Represents one capability of a lighting fixture.
"""

Methods should have docstrings when their behaviour is not obvious.

---

# Single Responsibility

Each class should have one responsibility.

Examples

XMLReader

Reads XML.

AliasService

Resolves channel names.

XLightsImporter

Converts xLights models into CanonicalFixture objects.

ComparisonEngine

Compares two fixtures.

---

# Git Workflow

Every sprint follows the same process.

git status

git add .

git commit -m "Sprint X.X - Description"

git push

The repository should always be clean before starting a new sprint.

---

# Definition of Done

A sprint is complete when:

✓ Code builds

✓ Tests pass

✓ Git repository is clean

✓ Changes are committed

✓ Changes are pushed

---

# General Principles

Keep classes small.

Keep methods short.

Prefer composition over large classes.

Avoid duplicate code.

Make the code obvious rather than clever.

When in doubt, choose readability.

# Development Workflow

Before implementing a new feature:

1. Read PROJECT_STATUS.md
2. Read the current sprint goal.
3. Extend existing classes where practical.
4. Avoid introducing new domain objects unless a genuine gap exists.
5. Replace complete files rather than partial snippets.