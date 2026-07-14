🍺 I think this is one of the best things we can do before continuing development. A new chat has no memory of why we made our architectural decisions, and that's the most valuable part of the project.

Below is the roadmap I would hand to a new developer joining the project.

xToolkit Development Roadmap
Current Status: v0.5.0 – Canonical Lighting Foundation
Project Vision

Goal

Create a tool that can take an xLights moving-head sequence written for one manufacturer's fixtures and automatically convert it to another manufacturer's fixtures while preserving the lighting designer's intent.

Not

A DMX channel remapper.

Instead

A capability translator.

Core Philosophy

We discovered one fundamental principle:

Translate capabilities, not channels.

Every manufacturer exposes features differently.

For example:

Fixture A

Channel 9 = Prism
Channel 10 = Prism Rotate

Fixture B

Channel 10

0-127 Prism

128-255 Prism Rotate

Both fixtures have identical capabilities despite different DMX implementations.

xToolkit therefore translates:

Sequence

↓

Fixture Capabilities

↓

Canonical Lighting Language

↓

Target Fixture Capabilities

↓

Translated Sequence

NOT

Channel 8

↓

Channel 12
Current Architecture
xLights XML

↓

XML Reader

↓

Model Objects

↓

Importer

↓

Canonical Fixture

↓

Fixture Report

Future:

Canonical Fixture

↓

Fixture Profile

↓

Compatibility Engine

↓

Sequence Translator
Major Components Completed
XML Reader

Reads:

rgbeffects.xml

Extracts:

Models
Attributes
NodeNames
DMX channels

Status

✅ Stable

Model Class

Represents one xLights model.

Provides:

model.name

model.channel_count

model.get_channel_name(channel)

model.is_moving_head()

Status

✅ Stable

Canonical Function Library

Created:

canonical_functions.py

Current functions include:

Movement

Pan
Pan Fine
Tilt
Tilt Fine
Pan/Tilt Speed

Beam

Dimmer
Shutter
Focus
Zoom
Frost
Iris

Colour

Color

Gobo

Gobo
Gobo Rotate

Effects

Prism
Prism Rotate

Control

Reset
Macro
Unused

Status

✅ Version 1 Complete

Fixture Categories

Created:

fixture_category.py

Categories

Movement

Beam

Color

Gobo

Effect

Control

Status

✅ Complete

Function Resolver

Purpose

Convert manufacturer channel names into canonical functions.

Example

Pan / X-axis / Horizontal

↓

PAN

Uses:

exact matches
keyword matches

Returns

ResolutionResult

with

Matched

Confidence

Method

Status

✅ Working

Knowledge Builder

Developer tool.

Purpose

Analyse fixtures.

Output

Moving Heads : 4

Unique Names : 11

Pan

Tilt

Dimmer

...

Used to discover real-world channel names.

Status

✅ Working

Fixture Report

Outputs

Fixture Report

Capabilities

✓ Pan

✓ Tilt

✓ Dimmer

✓ Shutter

...

Missing

Prism

Prism Rotate

...

Current Recognition

Pan

Pan Fine

Tilt

Tilt Fine

Dimmer

Shutter

Color

Unknown

Blank

Pan & Tilt Speed

Prism 1

Prism Rotate 1

Status

✅ Working

Unknown Function Registry

Collects unresolved channel names.

Purpose

Grow xToolkit's lighting knowledge.

Status

✅ Working

Important Architectural Decisions
Decision 1

Capabilities are canonical.

DMX channels are manufacturer implementation details.

Decision 2

The importer should understand fixtures.

Not simply copy XML.

Decision 3

Knowledge grows from real fixtures.

Not guesses.

This is why Knowledge Builder exists.

Decision 4

The Advanced Moving Head effect in xLights already thinks in capabilities.

xToolkit should too.

Fixture Capability Model

Eventually every fixture becomes:

Fixture Definition

Capabilities

✓ Pan

✓ Tilt

✓ Prism

✓ Color

✓ Dimmer

✓ Reset

instead of

Channel 1

Channel 2

Channel 3
Lighting Knowledge Learned

Your SHEHDS fixtures taught us:

Prism Rotate

can share a channel with

Prism

Meaning

One DMX channel

↓

Multiple capabilities

depending on DMX value.

This became one of the biggest architectural discoveries.

Scope Decisions

Version 1 focuses on

✅ Moving Heads

Not yet

Smoke
Haze
Bubble machines
Snow machines

Reason

These are usually venue-specific devices.

Testing Status

Passing

✅ XML Reader

✅ Importer

✅ Function Resolver

✅ Knowledge Builder

✅ Fixture Report

Remaining work

Teach resolver:

Blank

↓

UNUSED
Pan & Tilt Speed

↓

PAN_TILT_SPEED
Prism 1

↓

PRISM
Prism Rotate 1

↓

PRISM_ROTATE

Goal

Unknown Function Count : 0
Future Roadmap
Sprint 6

Knowledge Expansion

Expand resolver
Reach 100% recognition on test fixtures
Improve alias handling
Sprint 7

Fixture Profiles

Generate:

Fixture Profile

Capabilities

Compatibility
Sprint 8

Fixture Comparison Engine

Compare

Source Fixture

↓

Target Fixture

Output

Missing

Extra

Compatible
Sprint 9

Sequence Translation

Convert

Source Sequence

↓

Canonical

↓

Target Sequence
Sprint 10

Advanced DMX Mapping

Support

Shared channels
Range-based capabilities
GDTF-inspired mapping
Multiple DMX modes
Long-Term Vision

The ultimate goal is:

Make any xLights moving-head sequence work on your lighting rig.

Not by matching channel numbers, but by understanding what the lighting designer intended each fixture to do.

Development Standards

These are the rules we settled on:

Provide complete replacement files, not snippets.
Commit after every stable milestone.
Let real fixtures drive the design.
Think in lighting concepts, not programming shortcuts.
Keep the architecture simple enough that hobbyists can contribute.
🍺 My final note to Future Us

If I had to summarize the entire project in one paragraph, I'd write:

xToolkit is a capability-based translation engine for xLights moving-head fixtures. Rather than mapping DMX channels directly, it builds a canonical understanding of what each fixture can do, allowing sequences to be translated between different manufacturers while preserving the original lighting design. Real-world fixture data drives the evolution of the knowledge base, ensuring the software grows from practical experience rather than assumptions.

Fixture Engine
████████████████████████████ 100%

Sequence Engine
███████████░░░░░░░░░░░░░░░░░ 35%

GUI
██░░░░░░░░░░░░░░░░░░░░░░░░░░░ 5%