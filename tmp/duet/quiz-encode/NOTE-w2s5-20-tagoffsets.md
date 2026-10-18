# NOTE-w2s5-20 writer2: TAG offsets exact (PRE-006 ASK answered) + word1 correction

## TAG-bit offsets (first-hand, 8-value scans, paylen 352 const)
- pos96 TAG-01: tag (1,0) @ bits 332-333; value V0-7 @ 334-341 contiguous
  LSB-first. 10-bit contiguous field [1,0,V0..V7]. byte41 = 0x10|(V&3)<<6,
  byte42 = V>>2. tag PRE-EXISTS in zeros base (no dev-added tag bits).
- pos112 TAG-01: tag (1,0) @ bits 160-161; value V0-7 @ 166-173 contiguous
  LSB-first. byte20 = 0x01|(V&3)<<6, byte21 = V>>2. gap bits 162-165 = 0
  (field spans 160-173 = 14b, OR value split 166-169/170-173 — geometry open).
- pos120 TAG-0000: tag (0,0,0,0) @ bits 256-259 (ZERO tag); value @ 260-267
  contiguous LSB-first. 12-bit field [0000,V0..V7]. byte32 = (V&0xF)<<4,
  byte33 = V>>4 (byte33[4-7] = next-field/pad).
- read order: LSB-first everywhere (tags + values).

## Corrections to PRE-006 guesses
- bits 322-323 = (1,0) CONSTANT (byte40 = 0x04, neighbor field) — proven
  constant across 8 values, NOT the pos96 tag (true tag @332-333).
- word1 byte0 (bits 32-39 = 0x01) = LENGTH CODE byte4 (my G1: (offset<<1)|1,
  offset 0 @N=128), NOT a tag: varies with N (128-sweep proven), constant
  in tail beds only because N fixed. pos100/101/102 -> bytes 5/6/7 RAW8 ✓
  agree. multi-dev tag-constancy follows (length fixed).
