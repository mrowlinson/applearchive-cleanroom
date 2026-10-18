# GATE-028cc25 sweep: PASS-individual (rgram 2352/2352; RANGE still HELD)

- tip: lanes/encode-writer2 @028cc25 (parent 1ceaac9 gated PASS). rgram
  +162/-0 (pure addition), for-list +8 cells, pins +16 rows append-only.
- code read (ALL 5 branches, P2-mirror): D81 singleton 68B dip (17781,
  follows R end contiguously) + P30 singleton (17782) + P3A 16-row
  (17783-98, off0-15, P3A 16x8B) + P3B 10-row (17799-808, off0-9, P3B
  10x9B) + P3Q 4x16 (17809-72: m0-15 P3M 16x5B, q0-3 P3Q 4x9B).
  AST-verified all table rows/lens + offsets. no imports/OSS markers.
- battery: GATE-PASS shipped legs (outdir gate-w2-028cc25-s4): RGRAM
  n=2352, PINS-RGRAM set-eq 2352/2352; all other legs green incl
  OSS/LIBCOMP/ADOPT.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (14 descendants, all individually-closed).
- coverage: 155/156 PASS + 1 RED-held (48ebfe0).
