# Cleanroom firewall

## Wall

Inside: public specs + black-box observation only.
Outside: everything else.

Allowed in:
- Apple public dev docs (link + brief summary).
- Fetch-verified third-party docs (link + brief summary).
- Black-box behavior: `aa`/`aea` CLI runs, byte I/O, timings.
- Derived notes: beds (behavior tables) + numbers (offsets, sizes, counts).

## Forbidden in

- Pasted spec text. Link it, summarize briefly, never quote at length.
- SDK headers. No excerpts.
- Reference code. No excerpts, no ports. Independent impl only.
- Binaries. No vendored frameworks, tools, or dumps.
- Transcribed answers. Answers derive; they never copy.

## Traffic rules

- Questions behavior-only. Cell + need + tried + exhibits (own bytes).
- Answers = beds + numbers + verdict. Derived, never transcribed.
- Uncertain claims marked UNRESOLVED. Never asserted.
- Every cited URL fetch-verified before citing. No guessed URLs.

## Posture note

Wall posture differs if source is open. Current state (2026-09-29):
AppleArchive source NOT open (`apple/apple-archive` = 404, verified).
Open parts: LZFSE codec (BSD), python-aea (MIT), man pages (local).
These are reusable per their licenses, but cleanroom lanes still
derive independently; licenses govern reuse, wall governs provenance.
If Apple publishes source, re-survey + record new posture here.
Anything unsure: mark UNRESOLVED.
