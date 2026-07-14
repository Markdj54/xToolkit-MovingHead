Project Vision (never changes)
xToolkit

Make any moving-head sequence work on your lighting rig.

Version 1.0 converts imported xLights moving-head sequences
to the user's moving heads by rewriting rgbeffects.xml.

Version 1 Goal
Input

Imported rgbeffects.xml

User's rgbeffects.xml

Output

Translated rgbeffects.xml

Core principals
✓ We compare FUNCTIONS, not channel numbers.

✓ Canonical functions are the internal language.

✓ Pan, Tilt, Colour, Dimmer and Shutter are critical.

✓ Gobos, Prism and Focus are secondary.

✓ Complete files only.
Never edit snippets.

✓ Commit after every stable sprint.

✓ Build first.
GUI second.

Architecture

XML Reader

↓

Importer

↓

Canonical Fixture

↓

Translation Builder

↓

Translation Map

↓

RGB Rewriter

Current Status


Completed

✓ XML Reader

✓ Importer

✓ Comparison Engine

✓ Translation Builder

Current Sprint

Improve Importer recognition.

Next Sprint

Rewrite rgbeffects.xml

Future ideas

COMMUNITY FIXTURE PROFILES
aUTO FIXTURE RECOGNITION
LEARNING MODE
AI SUGGESTIONS
FIXTURE DATABASE
THESE ARE V2 IDEAS UNLESS THEY BECOME ESSENTIAL.