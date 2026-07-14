# Changelog

## v0.5.1 - Moving Head Data Foundation

### Added
- MovingHeadData class
- ColourWheel data structure
- ColourSlot data structure
- Beam data structure
- Motor data structure

### Changed
- Model now supports optional MovingHeadData.
- RGBEffectsReader now reads moving head information.

### Notes
- No GUI changes.
- No comparison engine changes.
- Foundation laid for colour wheel and moving head conversion.

## Sprint 8.0

### Added
- TranslationEntry domain class.
- TranslationMap domain class.
- TranslationBuilder service.
- Initial translation architecture for moving head conversion.

### Improved
- Completed end-to-end backend pipeline:
  XMLReader → Importer → CanonicalFixture → ComparisonEngine.

### Discovered
- Translation architecture is sound.
- Primary remaining work is improving fixture function recognition.
- Importer now identified as the critical component for Version 1.0.

## v0.9.0-alpha

### Added

- ParameterParser
- DMXParameterMapper
- ParameterRewriter
- ParameterTranslator

### Changed

- CanonicalFixture now supports capability lookup by channel.

### Milestone

First successful capability-based translation of an xLights DMX parameter.

Example:

E_SLIDER_DMX1

↓

E_SLIDER_DMX6

Added
ParameterParser
DMXParameterMapper
ParameterRewriter
ParameterTranslator
EffectTranslator
Sequence
Improved
CanonicalFixture
Added capability_by_channel()
Tests Added
test_parameter_parser.py
test_dmx_parameter_mapper.py
test_parameter_rewriter.py
test_parameter_translator.py
test_effect_translator.py
test_sequence.py

All passing.