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