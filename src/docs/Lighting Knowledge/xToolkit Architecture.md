# xToolkit Architecture

## Purpose

xToolkit is a capability-based translation engine for xLights moving-head fixtures.

Its purpose is **not** to remap DMX channels.

Its purpose is to understand the lighting designer's intent and translate that intent between different fixture personalities.

---

# Core Philosophy

Translate capabilities.

Never channels.

Example

Source Fixture

Pan = Channel 6

Target Fixture

Pan = Channel 1

The toolkit does **not** translate

6 → 1

It translates

PAN → Target PAN Channel

This distinction is the foundation of the entire project.

---

# Project Layers

```
GUI
    │
    ▼
Services
    │
    ▼
Domain
    │
    ▼
Knowledge
```

---

## GUI

Responsible for presentation only.

The GUI never contains lighting knowledge or business logic.

The GUI asks services for information and displays the results.

---

## Services

Services perform work.

Examples

- FunctionResolver
- ProfileBuilder
- ComparisonEngine
- TranslationBuilder
- SequenceTranslator

Every service should have one responsibility.

---

## Domain

The domain layer represents lighting concepts.

Examples

- CanonicalFixture
- FixtureCapability
- FixtureProfile
- TranslationMap
- TranslationEntry
- TranslationSession

Domain objects describe data.

They do not perform business logic.

---

## Knowledge

Knowledge is data.

Examples

- aliases.yaml
- translation_rules.yaml
- fixture_categories.yaml

Lighting knowledge should be stored here whenever possible.

Adding support for new fixtures should normally require changing data rather than Python code.

---

# Architectural Laws

## Law 1

Knowledge never lives in code.

Wrong

if "Pan" in channel_name

Correct

aliases.yaml

↓

Resolver

↓

PAN

---

## Law 2

Only the resolver understands manufacturer channel names.

Everything else uses canonical functions.

---

## Law 3

Services own exactly one responsibility.

Builders build.

Resolvers resolve.

Comparers compare.

Translators translate.

---

## Law 4

Domain objects contain no business logic.

They describe information only.

---

## Law 5

Every stage receives one object.

Prefer

service.execute(session)

over

service.execute(
    fixture,
    profile,
    map,
    logger,
    ...
)

---

## Law 6

XML stops at the importer.

Importer

XML

↓

Domain Objects

Exporter

Domain Objects

↓

XML

Everything between those stages is independent of XML.

---

## Law 7

Translation always occurs through capabilities.

Never

Channel 8

↓

Channel 11

Always

PRISM_ROTATE

↓

Capability Mapping

↓

Target Channel

---

## Law 8

Reports never calculate.

Reports contain results.

The GUI displays them.

---

## Law 9

The GUI never makes decisions.

Business logic belongs in services.

---

## Law 10

Builders return complete objects.

Avoid incremental construction from outside the builder.

---

# Translation Pipeline

```
Read XML
    │
    ▼
Importer
    │
    ▼
Canonical Fixture
    │
    ▼
Profile Builder
    │
    ▼
Comparison Engine
    │
    ▼
Translation Builder
    │
    ▼
Translation Map
    │
    ▼
Sequence Translator
    │
    ▼
Sequence Writer
    │
    ▼
Translation Report
```

---

# Design Goals

The architecture should remain

- Simple
- Predictable
- Testable
- Data-driven
- Extensible

The toolkit should grow by expanding its knowledge base rather than increasing code complexity.

---

# Long-Term Vision

The long-term objective is to make any supported moving-head sequence portable between fixture manufacturers while preserving the original lighting design.

The project should eventually become a general-purpose lighting translation engine rather than a collection of fixture-specific rules.

# Final Reminder

When faced with a design decision, choose the solution that increases the toolkit's understanding of lighting concepts rather than one that solves a single fixture problem.

If a new feature requires adding manufacturer-specific code, reconsider the design.

Prefer extending the knowledge base over extending conditional logic.

Think in lighting concepts.

Not channels.

# Non-Goals

The following are intentionally outside the scope of xToolkit Version 1.

- Live DMX output
- Visualisation
- Lighting design
- Fixture editing
- Show scheduling
- Hardware control
- Audio playback
- Networking
- FPP integration
- xLights replacement

xToolkit complements xLights.


It does not compete with it.

# Coding Style

Use descriptive names.

Avoid abbreviations.

Avoid magic numbers.

Prefer dataclasses for domain objects.

Prefer enums over string constants.

Prefer immutable objects where practical.

Document public classes.

Document public methods.

Keep methods short.

Keep services focused.

Remove dead code rather than commenting it out.

Commit small, working changes frequently.

# The xToolkit Promise

Every design decision should move the project closer to understanding lighting rather than understanding fixtures.

Fixtures change.

Manufacturers change.

DMX implementations change.

Lighting concepts do not.

The software should grow by learning more about lighting, not by accumulating fixture-specific exceptions.

When in doubt, choose the design that increases understanding rather than complexity.

Sequence Translation Pipeline

Parameter String

↓

ParameterParser

↓

DMXParameterMapper

↓

Canonical Capability

↓

TranslationMap

↓

ParameterRewriter

↓

Translated Parameter

Readers create domain objects.

They never perform translation, validation, optimisation or business logic.

That rule now applies to:

XLightsImporter
XSQReader
Any future GDTF or QLC+ readers

It keeps the codebase predictable.