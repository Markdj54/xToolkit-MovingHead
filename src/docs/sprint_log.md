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

## Sprint 10.3

### Objective

Validate the Translation Engine using real production xLights
sequences and complete reverse engineering of the XSQ file
structure prior to implementing XSQWriter.

---

### Validation Tools

Created development validation tools capable of analysing
production xLights sequences.

Validation now reports:

- Total effects
- DMX effect count
- Total parameters
- DMX parameter usage
- Parameter families

Validation successfully processed a production sequence
containing 529 EffectDB entries.

---

### XSQ Reverse Engineering

Completed investigation of the relationship between:

- EffectDB
- ElementEffects
- DisplayElements

Confirmed the sequence hierarchy.

Sequence

↓

ElementEffects

↓

Element

↓

EffectLayer

↓

Effect

↓

EffectDB Reference

↓

EffectDB Entry

---

### Effect References

Confirmed that timeline effects do not contain parameter data.

Timeline effects reference EffectDB using the "ref" attribute.

Example:

Element

DMX - Wristband 1-2 (Controller)

↓

Effect

ref="79"

↓

EffectDB[79]

↓

DMX Parameters

This confirms that EffectDB is the authoritative source
for effect parameters.

---

### Architecture Discovery

Determined that XSQWriter does not need to rebuild the
sequence timeline.

Only EffectDB entries require modification.

ElementEffects, DisplayElements, timing information and
timeline relationships can remain unchanged.

This significantly reduces implementation complexity and
risk.

---

### Domain Knowledge

Confirmed that the xLights DMX effect is generic and is
used for many DMX devices including:

- Moving Heads
- Wristband Controllers
- Other DMX equipment

The Translation Engine therefore operates on DMX parameter
references rather than assuming Moving Head effects.

---

### Future Enhancements

Identified support requirements for:

- Value Curve parameters
- Additional DMX parameter families
- Element Mapping
- Model Mapping

These are Version 2 features and do not impact the
Sprint 11 implementation.

---

### Sprint Outcome

The read side of the XSQ format is now considered fully
understood.

Sprint 11 can begin implementation of XSQWriter with
high confidence.

Sprint 11 Milestone

Successfully performed the first lossless round-trip of a production xLights sequence.

A production .xsq was read into the xToolkit domain model and written back to disk. The generated sequence opened successfully in xLights without modification, validating the Reader, Serializer and Writer architecture.