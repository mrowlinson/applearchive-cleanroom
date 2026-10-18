# GATE-58f0cd5 sweep: PASS (rgram 1580/1580, T9W1 16x16)

- tip: lanes/encode-writer2 @58f0cd5 (parent 73cadd0 gated PASS). rgram.py
  +42/-0, cells to 13256, pins 1560->1580 (+20/-0).
- code read (ALL): _T9W1T 16 tabs + _T9W1B 16 block-words + _T9W1C consts
  (54 keys, unique; tab/block bytes excluded) + branch n<=13256 (off=
  n-13001, m=off&15, q=off>>4): m<=15 (16 tabs), q<=15 (16 blocks),
  contiguous after T9V1Q (13001 follows 13000), paylen 68, b5 0x65 + steps
  @55/183 matches message. ordering verified.
- NIT (no FAIL, persistent class): message "(1582 pins)" counts 2 csv
  comments; data rows 1580 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-58f0cd5-s4): HYGIENE/CONTAM clean,
  RGRAM n=1580, PINS-RGRAM set-eq 1580/1580, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 126/126 (NOTE-092 baseline + 19), ZERO holds.
