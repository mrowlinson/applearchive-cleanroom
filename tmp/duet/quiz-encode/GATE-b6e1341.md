# GATE-b6e1341 sweep: PASS (rgram 1990/1990, T9J2Q 16x16)

- tip: lanes/encode-writer2 @b6e1341 (parent dc6d821 gated PASS). rgram.py
  +49/-0, cells to 15344, pins 1974->1990 (+16/-0).
- code read (ALL): _T9J2QT 16 tabs (6B) + _T9J2B5 16 b5-vals + _T9J2QB 16
  block-words (6B) + _T9J2QC consts (52 keys, unique; tab/block bytes
  excluded) + branch n<=15344 (off=n-15089, m=off&15, q=off>>4): m<=15
  (16 tabs), q<=15 (B5/QB len 16 each), b5=B5[q]+(m==15&q in 0,8),
  blk=QB[q], tab=QT[m]. contiguous after T9J1Q (15089 follows 15088),
  paylen 68. ordering verified.
- NIT (no FAIL, persistent class): message "(1992 pins)" counts 2 csv
  comments; data rows 1990 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-b6e1341-s4): HYGIENE/CONTAM clean,
  RGRAM n=1990, PINS-RGRAM set-eq 1990/1990, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 140/140 (NOTE-092 baseline + 33), ZERO holds.
