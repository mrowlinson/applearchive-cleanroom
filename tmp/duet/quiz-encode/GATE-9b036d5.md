# GATE-9b036d5 sweep: PASS (rgram 1506/1506, T9T1 4x16)

- tip: lanes/encode-writer2 @9b036d5 (parent 7bd1121 gated PASS). rgram.py
  +38/-0, cells to 12652, pins 1490->1506 (+16/-0).
- code read (ALL): _T9T1T 16 tabs + _T9T1B 4 block-words + _T9T1C consts (53
  keys, unique; tab/block bytes excluded) + branch n<=12652 (off=n-12589,
  m=off&15, q=off>>4): m<=15 (16 tabs), q<=3 (4 blocks), contiguous after
  T9D4 (12589 follows 12588), paylen 68. ordering verified.
- NIT (no FAIL, persistent class): message "(1508 pins)" counts 2 csv
  comments; data rows 1506 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-9b036d5-s4): HYGIENE/CONTAM clean,
  RGRAM n=1506, PINS-RGRAM set-eq 1506/1506, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 123/123 (NOTE-092 baseline + 16), ZERO holds.
