# GATE-f7d7ecf sweep: PASS (rgram 1478/1478, T9S1 16x16)

- tip: lanes/encode-writer2 @f7d7ecf (parent c9441d4 gated PASS). rgram.py
  +44/-0, cells to 12560, pins 1458->1478 (+20/-0).
- code read (ALL): _T9S1T 16 tabs + _T9S1B 16 block-words + _T9S1C consts
  (52 keys, unique; tab/block bytes correctly excluded) + branch n<=12560
  (off=n-12305 new epoch, m=off&15, q=off>>4): m<=15 (16 tabs), q<=15 (16
  blocks), contiguous after T9D2 (12305 follows 12304), paylen 68 (back to
  68-tier after 64B dip band), b5 0x60 + steps @111/239 matches message.
  ordering verified.
- NIT (no FAIL, persistent class): message "(1480 pins)" counts 2 csv
  comments; data rows 1478 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-f7d7ecf-s4): HYGIENE/CONTAM clean,
  RGRAM n=1478, PINS-RGRAM set-eq 1478/1478, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 120/120 (NOTE-092 baseline + 13), ZERO holds.
