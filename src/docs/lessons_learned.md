Prism and Prism Rotate can share one DMX channel.
Canonical capabilities are more important than channel numbers.
xLights Advanced Moving Head already thinks in capabilities.
Real fixtures drive the design.

# Lessons Learned

## Capability First

The purpose of xToolkit is not to compare DMX channels.

It is to determine whether two fixtures provide the same lighting capabilities.

Channel differences are handled by the translation engine.

## Comparison vs Translation

Comparison answers:

"Can this fixture reproduce the original sequence?"

Translation answers:

"How should the sequence be rewritten?"

These are separate stages.

## Canonical Language

CanonicalFixture is the internal language of xToolkit.

Everything outside the importer should work with CanonicalFixture rather than raw xLights XML.