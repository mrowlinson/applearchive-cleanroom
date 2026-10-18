# GATE-1ad2e66 sweep: PASS (rgram 1150/1150, T8X cluster5)

- tip: lanes/encode-writer2 @1ad2e66 (parent 44a5f94 gated PASS). rgram.py
  +176/-0 (3 lits + X1-15 + X2S + X2-9 + X3S + X3-15 + X4 3x16), cells to
  10564, pins 1122->1150 (+28/-0).
- code read (ALL): 9 tables (X0 3, X1T 15, X2T 9, X3T 15, X4T 16, X4B 3,
  counts AST-verified from tip file) + 7 branches monotone contiguous
  (off 1738..1829: X0 10475/X1/X2S 10491/X2/X3S 10501/X3/X4 10564). every
  index hand-bounded in-range (X1 15, X2 9, X3 15, X4 m16/q3). X4 tab
  quirk (pay55-1 when q1) read as-is. no imports/OSS/disasm markers.
- battery: GATE-PASS (outdir gate-w2-1ad2e66-s4): HYGIENE/CONTAM clean,
  RGRAM n=1150, PINS-RGRAM set-eq 1150/1150, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 108/108 (corrected NOTE-092 baseline 107 + 1), ZERO holds.
