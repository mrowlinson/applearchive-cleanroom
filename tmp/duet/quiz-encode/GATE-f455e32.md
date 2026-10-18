# GATE-f455e32 sweep: PASS (rgram 1356/1356, T8E1 15-row + Q 15x16)

- tip: lanes/encode-writer2 @f455e32 (parent d80c7a8 gated PASS). rgram.py
  +96/-0, cells to 11849, pins 1314->1356 (+42/-0).
- code read (ALL): E1 branch (single 11609 first + 15-row m=off-2859) + Q
  branch (m=(off-2875)&15, q=(off-2875)>>4, k15 early-edge QB[q]/QB[q+1]/
  QN, b5 6-step ladder, b10 hex-tab, b11 m-rule). AST-verified: E1T 15
  (m0-14), E10 64B, QT 16 (m0-15), QB 15 (q0-14; m=15&q=14 last-edge -> QN
  4B), B10 16B. all indices in-range, contiguous after D1Q (11594 follows
  11593). no imports/OSS/disasm markers.
- NIT (no FAIL, persistent class): message "(1358 pins)" counts 2 csv
  comments; data rows 1356 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-f455e32-s4): HYGIENE/CONTAM clean,
  RGRAM n=1356, PINS-RGRAM set-eq 1356/1356, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 115/115 (NOTE-092 baseline + 8), ZERO holds.
