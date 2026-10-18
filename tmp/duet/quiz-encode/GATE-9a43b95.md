# GATE-9a43b95 sweep: PASS (rgram 1638/1638, T9Y1 5x16)

- tip: lanes/encode-writer2 @9a43b95 (parent 4673e2e gated PASS). rgram.py
  +38/-0, cells to 13428, pins 1618->1638 (+20/-0).
- code read (ALL): _T9Y1T 16 tabs + _T9Y1B 5 block-words + _T9Y1C consts (56
  keys, unique; tab/block bytes excluded) + branch n<=13428 (off=n-13349,
  m=off&15, q=off>>4): m<=15 (16 tabs), q<=4 (5 blocks), contiguous after
  T9X1Q (13349 follows 13348), paylen 68. ordering verified.
- NIT (no FAIL, persistent class): message "(1640 pins)" counts 2 csv
  comments; data rows 1638 (battery decisive). (No b5 assertion in branch
  — same pattern as X1Q; battery decisive.)
- battery: GATE-PASS (outdir gate-w2-9a43b95-s4): HYGIENE/CONTAM clean,
  RGRAM n=1638, PINS-RGRAM set-eq 1638/1638, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 128/128 (NOTE-092 baseline + 21), ZERO holds.
