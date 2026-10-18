# PARENT-011 lzmesh owned elsewhere (encode)

lzmesh is out of scope here: sibling project lzmesh-cleanroom
owns its cleanroom decompile + C port (byte-exactness gated
2026-09-27, perf in progress). Rules:

1. NEVER implement lzmesh in this repo (no port, no proto).
2. Consume ONLY via /Users/mrowlinson/Projects/LZMESH shared
   deliverables (core/, docs, tests). NEVER read
   lzmesh-cleanroom/ working scratch (their wall runs both
   ways; our seats stay out entirely).
3. Link needs PARENT-003-style gates: pinned commit + sweep
   byte-verify vs APPLE oracle (never vs lzmesh port alone —
   that proves self-consistency, not correctness). Oracle for
   all identity claims stays the Apple binary.
4. Viewers: confirm whether/where AppleArchive references
   lzmesh; file finding + link plan when first needed, not
   before. No speculative integration.
