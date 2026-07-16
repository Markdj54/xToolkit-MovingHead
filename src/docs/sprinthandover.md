"Continue xToolkit Sprint 15 from this handover. Assume all items below are current and do not redesign the architecture unless a defect requires it."

xToolkit Sprint 15 Handover
Project Vision

Make any moving-head sequence work on your lighting rig.

xToolkit analyses moving-head fixtures, compares their capabilities and translates xLights sequences so they can be played on different lighting hardware with the closest possible visual match.

The goal is not identical DMX.

The goal is identical visual performance.

Current Status
Translation Engine

Working.

Successfully tested with a commercial xLights sequence.

Results:

620 effects loaded

100 effects translated

Translated XSQ written successfully

Translation Map example:

PAN      10 -> 1

TILT     12 -> 3

DIMMER    2 -> 6

SHUTTER   3 -> 7

COLOR     1 -> 8

The translated XSQ imports correctly into xLights.

Architecture

Current pipeline

RGBEffectsReader

↓

XLightsImporter

↓

CanonicalFixture

↓

TranslationBuilder

↓

TranslationMap

↓

ParameterTranslator

↓

EffectTranslator

↓

SequenceTranslator

↓

XSQWriter

This pipeline is working.

Do not redesign it.

Current Design Philosophy

Separate:

What the fixture can do

from

How xLights implements it

CanonicalFixture remains DMX-independent.

MovingHeadData stores xLights implementation details.

Current Domain Objects

CanonicalFixture

capabilities
channel lookup
translation engine

MovingHeadData

pan motor
tilt motor
beam
colour wheel
shutter
xLights-specific geometry

FixtureProfile

Represents fixture capabilities independent of DMX.

ImportedFixture

NEW

Contains:

CanonicalFixture

MovingHeadData

This file has just been created and committed.

Sprint 15

Current task

Enhance XLightsImporter.

Instead of returning

CanonicalFixture

it will return

ImportedFixture

without breaking the existing translation engine.

After that:

Populate

Pan motor

Tilt motor

Beam

Colour wheel

Shutter

using

DmxPanChannel

DmxPanDegOfRot

DmxPanOrient

DmxTiltChannel

DmxTiltDegOfRot

DmxTiltOrient

etc.
Real-world Testing

Testing has already proved:

✔ Pan translates correctly.

Tilt movement is physically different.

This is NOT a channel mapping problem.

It is caused by fixture geometry differences.

Current fixture values include examples such as:

Vendor:

Tilt rotation 270°

Orientation 345°

Mine:

Tilt rotation 180°

Orientation 90°

Geometry correction is a future sprint.

Do not modify the translation engine yet.

Important Rules
Full files only when editing Python.
Small commits.
No architecture rewrites unless necessary.
Protect the existing working translation pipeline.
Real-world testing after every milestone.
Last Commit
feat: add ImportedFixture domain model

Next task:

Modify XLightsImporter to build and return ImportedFixture.