# xToolkit Project Status

## Version

v0.5.1

## Current Sprint

Sprint 7.1

## Current Goal

Replace the legacy comparer with ComparisonEngine.

The ComparisonEngine compares CanonicalFixture objects and produces a ComparisonReport.

## Current Architecture

rgbeffects.xml
    ↓
XMLReader
    ↓
Model
    ↓
XLightsImporter
    ↓
CanonicalFixture
    ↓
ComparisonEngine
    ↓
ComparisonReport
    ↓
Sequence Translation Engine
    ↓
XSQ Export

## Important Decisions

- Compare capabilities, not DMX channels.
- DMX channels are implementation details.
- Translation happens after comparison.
- XML knowledge remains inside XMLReader and XLightsImporter.
- CanonicalFixture is the language spoken internally by xToolkit.
- ComparisonReport is the single source of truth for fixture comparison.

## Current Work

Implement ComparisonEngine using the CanonicalFixture domain model.

## Next File

comparison_engine.py

Sequence Engine

Status:
IN PROGRESS

Completed

✔ Parameter parsing

✔ Parameter mapping

✔ Parameter rewriting

✔ Capability translation

Remaining

□ Effect translation

□ XSQ reader integration

□ XSQ writer

□ End-to-end sequence translation

# Current Project Status

## Phase

Integration

The core architecture has now been completed.

Development has transitioned from architectural design into production
integration.

---

## Completed

### Fixture Engine

Status: COMPLETE

Features:

- Canonical Fixture Model
- Function Resolver
- Alias Service
- Translation Maps
- Comparison Engine
- Import Pipeline

---

### Translation Engine

Status: COMPLETE

Features:

- ParameterParser
- DMXParameterMapper
- ParameterRewriter
- ParameterTranslator
- EffectTranslator
- SequenceTranslator

Fully tested.

---

### Sequence Engine

Status: IN PROGRESS

Completed:

✔ Sequence domain model

✔ XSQReader

✔ EffectDefinition parsing

✔ Moving Head detection

✔ Production sequence loading

Pending:

□ Validation against multiple production sequences

□ XSQWriter

□ End-to-end translation

---

### GUI

Status: PLANNED

Future work:

- Sequence selection
- Fixture selection
- Translation wizard
- Translation report
- Save translated sequence

---

## Current Architecture

Real XSQ

↓

XSQReader

↓

Sequence

↓

SequenceTranslator

↓

EffectTranslator

↓

ParameterTranslator

↓

DMXParameterMapper

↓

TranslationMap

↓

ParameterRewriter

↓

Translated Sequence

---

## Overall Progress

Fixture Engine ............. 100%

Translation Engine ......... 100%

Sequence Engine ............ 65%

XSQ Writer ................. 0%

GUI ....................... 5%

Overall Project ............ ~75%

---

## Current Focus

Validate the Translation Engine using real xLights sequences before
implementing XSQWriter.

The next milestone is producing a translated .xsq file that opens
correctly in xLights.