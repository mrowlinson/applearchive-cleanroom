# GATE-bdc63f2 sweep: PASS (rgram 1808/1808, T9E2 15-row + Q 15x16)

- tip: lanes/encode-writer2 @bdc63f2 (parent aeefa70 gated PASS). rgram.py
  +89/-0, cells to 14285, pins 1768->1808 (+40/-0).
- code read (ALL): E2 branch (single 14045 first + 15-row tab[off]) + Q
  branch (m=off&15, q=off>>4, k15 early-edge QB[q]/QB[q+1]/QN, b5 ladder).
  AST: E20 68B (paylen-68-first branch), E2T 15 (off0-14), QT 16 (m0-15),
  QB 15 (q0-14; q+1<=14; q=14&m=15 at last row off=239 -> QN 8B, LIVE).
  all indices in-range, contiguous after T9C2Q (14030 follows 14029). no
  imports/OSS/disasm markers.
- NIT (no FAIL, persistent class): message "(1810 pins)" counts 2 csv
  comments; data rows 1808 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-bdc63f2-s4): HYGIENE/CONTAM clean,
  RGRAM n=1808, PINS-RGRAM set-eq 1808/1808, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 133/133 (NOTE-092 baseline + 26), ZERO holds.
