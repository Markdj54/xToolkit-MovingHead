Sprint 8.0

Completed

✓ TranslationEntry

✓ TranslationMap

✓ TranslationBuilder

Discovered

Importer recognition is the current bottleneck.

Next Sprint

Recognise all channels in a 16-channel moving head.

# Sprint 9

## Objective

Begin development of the Sequence Engine.

## Completed

- Implemented ParameterParser.
- Implemented DMXParameterMapper.
- Refactored CanonicalFixture with capability_by_channel().
- Implemented ParameterRewriter.
- Implemented ParameterTranslator.
- Added comprehensive unit tests for all new components.

## Milestone

Successfully translated the first real xLights DMX parameter.

Example:

E_SLIDER_DMX1

↓

E_SLIDER_DMX6

using canonical lighting capabilities rather than channel numbers.

## Architecture

Sequence translation now follows the pipeline:

Effect Parameter
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

## Status

Sprint 9 completed successfully.

Core parameter translation engine operational.

Next Sprint:

Translate complete EffectDB entries before integrating with XSQ file reading and writing.

# Sprint 10

## Objective

Transition xToolkit from individual component testing to a complete
sequence translation engine capable of processing real xLights
sequence files.

---

## Completed

### Sequence Domain

- Introduced the Sequence aggregate root.
- Sequence now owns all EffectDefinition objects.
- Added support for:
  - add_effect()
  - effect()
  - effects()
  - effect_count()
  - replace_effect()

---

### XSQ Reader

Implemented the first production version of XSQReader.

Features:

- Opens a real .xsq file.
- Locates the EffectDB section.
- Builds a Sequence.
- Creates an EffectDefinition for every EffectDB entry.
- Uses ParameterParser to populate each EffectDefinition.
- Successfully loads all 529 effects from a production xLights sequence.

---

### EffectDefinition

Extended EffectDefinition with:

- is_moving_head()

This allows the domain model to determine whether an effect contains
moving head DMX data without understanding the effect type.

This became the foundation for selective translation.

---

### Translation Engine

Implemented:

- SequenceTranslator

SequenceTranslator processes an entire Sequence while preserving all
non-moving-head effects.

Translation pipeline:

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

---

## Testing

Successfully completed:

✔ test_sequence.py

✔ test_xsq_reader.py

✔ test_effect_definition.py

✔ test_sequence_translator.py

All tests passed.

---

## Milestones

Successfully loaded a real production xLights sequence.

529 EffectDefinition objects created.

Successfully translated an entire Sequence while preserving all
non-moving-head effects.

Translation Engine considered complete.

---

## Architecture Decisions

Major design decision:

xToolkit is NOT an xLights effect translator.

xToolkit is a Moving Head translator.

Only moving head parameters are translated.

Every other xLights effect is preserved exactly as created by xLights.

This dramatically simplifies the architecture and future maintenance.

---

## Next Sprint

Sprint 10.3

Validation Phase

Objectives:

- Run the translation engine against multiple real sequences.
- Measure:
    - total effects
    - moving head effects
    - translated parameters
    - unknown parameters
- Resolve edge cases.
- Begin implementation of XSQWriter after validation is complete.