# xToolkit Product Vision

## Vision

# xToolkit

## Vision

Make any moving-head sequence work on your lighting rig.

xToolkit analyses moving-head fixture personalities, compares their capabilities, and translates xLights sequences so they can be played on different lighting hardware with the closest possible visual match.

The goal is **not** to reproduce identical DMX data.

The goal is to reproduce the **same visual performance**.

xToolkit exists to solve one problem exceptionally well:

**Translate imported xLights moving head sequences from one fixture type to another without requiring users to manually edit hundreds of DMX parameters.**
or
**Translate imported xLights moving head sequences from one fixture type to another without requiring users to manually edit hundreds of DMX parameters.**

The application is not intended to replace xLights.

Instead, xToolkit complements the existing xLights workflow by performing intelligent DMX parameter translation after a sequence has been successfully imported.

---

# The Problem

Commercial xLights sequences are typically programmed using the author's own moving head fixtures.

Although xLights can import a purchased sequence and map props, models and layout elements, it cannot automatically translate the internal DMX programming when the destination moving heads use different channel layouts.

As a result, imported moving head effects often behave incorrectly.

Typical problems include:

* Pan and Tilt reversed
* Colour wheels incorrect
* Gobos not matching
* Prisms and Frost on incorrect channels
* Focus and Zoom mapped incorrectly
* Fixtures requiring extensive manual editing

Correcting these issues manually can take many hours for a single sequence.

---

# The Solution

xToolkit analyses an imported xLights sequence, understands the capabilities of both the vendor fixtures and the user's fixtures, then automatically remaps the DMX programming while preserving the original artistic intent.

The application translates fixture capabilities rather than DMX channel numbers.

This allows programming created for one moving head to be adapted intelligently for another.

---

# Intended Workflow

1. Purchase a commercial xLights sequence.
2. Import the sequence into xLights using the normal import process.
3. Map props, models and display elements using xLights.
4. Save the imported sequence.
5. Open the imported sequence in xToolkit.
6. Select replacement fixtures where required.
7. Translate the sequence.
8. Save the translated sequence.
9. Open the translated sequence in xLights.

The user continues working inside xLights exactly as they do today.

xToolkit becomes a specialised translation step between importing a sequence and programming final adjustments.

---

# Core Design Principles

## Preserve Artistic Intent

xToolkit never attempts to redesign a sequence.

Timing, choreography, movement paths, colours, effects and creative decisions remain untouched wherever possible.

Only the DMX parameter mapping is translated.

---

## Work With xLights

xToolkit enhances xLights rather than replacing it.

xLights remains responsible for:

* Importing purchased sequences
* Model mapping
* Prop mapping
* Layout management
* Media management
* Sequence editing

xToolkit is responsible only for moving head DMX translation.

---

## Capability-Based Translation

Internal translation is performed using fixture capabilities rather than physical DMX channel numbers.

For example:

Pan

↓

Capability

↓

Pan

rather than

Channel 6

↓

Channel 3

This architecture allows fixtures from different manufacturers to be translated using a common internal language.

---

## Preserve the Original Sequence

Where possible, the original XSQ document is preserved.

Only translated EffectDB parameter data is modified.

Timeline information, sequence structure and artistic programming remain unchanged.

---

# Version 1 Goals

Version 1 focuses exclusively on moving head translation.

Included:

* XSQ sequence reading
* Fixture comparison
* Capability mapping
* DMX parameter translation
* XSQ writing
* Fixture replacement selection
* Translation summary

---

# Out of Scope

Version 1 will not attempt to:

* Replace xLights importing
* Edit sequence timing
* Modify choreography
* Generate lighting effects
* Optimise programming
* Edit media
* Edit props or models
* Replace xLights as a sequence editor

---

# Future Vision

Future versions may include:

* Automatic fixture matching
* Fixture compatibility scoring
* Batch sequence translation
* Fixture library updates
* Translation reports
* Plug-in architecture
* Additional DMX device support

These enhancements build upon the Version 1 architecture without changing its core purpose.

---

# Mission Statement

**xToolkit enables lighting enthusiasts to use commercial xLights sequences with their own moving head fixtures by automatically translating DMX programming while preserving the original creative intent.**

# Development Philosophy

## One Problem Solved Well

xToolkit deliberately focuses on one specific problem.

The application exists to translate moving head DMX programming between different fixture types after a sequence has been imported into xLights.

Features that do not contribute directly to this objective should be carefully evaluated before being added.

A smaller application with a clear purpose is preferable to a larger application attempting to solve every lighting problem.

---

## Respect Existing Workflows

Most users are already comfortable using xLights.

xToolkit should integrate naturally into that workflow rather than requiring users to learn an entirely new process.

Whenever possible, users should continue using xLights for tasks that xLights already performs well.

---

## Preserve User Creativity

The sequence designer has already made the artistic decisions.

The user has already designed their display.

xToolkit should avoid modifying either.

Its role is to translate technical implementation details while preserving creative intent.

---

## Predictable Before Clever

Reliable translation is more valuable than complex translation.

When there is uncertainty, xToolkit should favour predictable and explainable behaviour over hidden automation.

The user should always understand what changes have been made.

---

## Architecture First

The internal architecture should remain independent of any single fixture manufacturer.

Core translation is performed using fixture capabilities rather than vendor-specific DMX channel numbers.

This allows new fixtures to be supported by expanding the fixture library rather than rewriting the translation engine.

---

## Preserve Data

Whenever possible, xToolkit modifies the smallest amount of information required.

The application should preserve:

* Sequence timing
* Layout information
* Effect ordering
* XML structure
* Artistic programming

Only translated DMX parameter data should change.

---

## Build for the Future

Version 1 solves the current problem.

The architecture should make future enhancements straightforward without requiring major redesign.

Examples include:

* Automatic fixture matching
* Batch translation
* Additional DMX device types
* Fixture recommendation
* Translation confidence scoring

These features should build upon the existing architecture rather than replace it.

---

# Success Criteria

xToolkit is successful when a user can:

* Purchase a commercial sequence.
* Import it into xLights.
* Run xToolkit.
* Translate their moving head fixtures.
* Reopen the sequence in xLights.
* Continue programming immediately with correctly functioning moving heads.

If users spend less time manually editing DMX channels and more time creating great shows, xToolkit has achieved its purpose.

# Development Philosophy

## One Problem Solved Well

xToolkit deliberately focuses on one specific problem.

The application exists to translate moving head DMX programming between different fixture types after a sequence has been imported into xLights.

Features that do not contribute directly to this objective should be carefully evaluated before being added.

A smaller application with a clear purpose is preferable to a larger application attempting to solve every lighting problem.

---

## Respect Existing Workflows

Most users are already comfortable using xLights.

xToolkit should integrate naturally into that workflow rather than requiring users to learn an entirely new process.

Whenever possible, users should continue using xLights for tasks that xLights already performs well.

---

## Preserve User Creativity

The sequence designer has already made the artistic decisions.

The user has already designed their display.

xToolkit should avoid modifying either.

Its role is to translate technical implementation details while preserving creative intent.

---

## Predictable Before Clever

Reliable translation is more valuable than complex translation.

When there is uncertainty, xToolkit should favour predictable and explainable behaviour over hidden automation.

The user should always understand what changes have been made.

---

## Architecture First

The internal architecture should remain independent of any single fixture manufacturer.

Core translation is performed using fixture capabilities rather than vendor-specific DMX channel numbers.

This allows new fixtures to be supported by expanding the fixture library rather than rewriting the translation engine.

---

## Preserve Data

Whenever possible, xToolkit modifies the smallest amount of information required.

The application should preserve:

* Sequence timing
* Layout information
* Effect ordering
* XML structure
* Artistic programming

Only translated DMX parameter data should change.

---

## Build for the Future

Version 1 solves the current problem.

The architecture should make future enhancements straightforward without requiring major redesign.

Examples include:

* Automatic fixture matching
* Batch translation
* Additional DMX device types
* Fixture recommendation
* Translation confidence scoring

These features should build upon the existing architecture rather than replace it.

---

