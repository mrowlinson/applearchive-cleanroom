# GATE-dc6d821 sweep: PASS (rgram 1974/1974, T9J1 5s+A15+B8 + Q 4x16)

- tip: lanes/encode-writer2 @dc6d821 (parent 66c84ba gated PASS). rgram.py
  +126/-0, cells to 15088, pins 1936->1974 (+38/-0).
- code read (ALL): J1 branch (singles {14997,14998,14999,15015,15016} 68B
  each + A 15000-14 15-row + B fall-through 15017-24 8-row) + Q branch
  (m=off&15, q=off>>4, b2=Q2[m], tab=QT[m], b47=Q7E/Q7O[m] by q-parity,
  blk=QB[q]). AST: S1-S5 68B, AT/BT 15/8 (m0-14/0-7), QT/Q2/Q7E/Q7O 16
  (m0-15), QB 4 (q0-3). coverage 3+15+2+8+64=92 cells. contiguous after
  T9I1 (14997 follows 14996). no imports/OSS/disasm markers.
- NIT (no FAIL, persistent class): message "(1976 pins)" counts 2 csv
  comments; data rows 1974 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-dc6d821-s4): HYGIENE/CONTAM clean,
  RGRAM n=1974, PINS-RGRAM set-eq 1974/1974, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 139/139 (NOTE-092 baseline + 32), ZERO holds.
