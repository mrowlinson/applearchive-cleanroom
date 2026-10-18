# GATE-b25a422 sweep: PASS-individual (rgram 2206/2206; RANGE still HELD)

- tip: lanes/encode-writer2 @b25a422 (parent b375c71 gated PASS). rgram.py
  +150/-0, cells to 16480 (= 68-tier end per NOTE-231b), pins 2166->2206
  (+40/-0, append-only).
- code read (ALL): P1 branch (A 16384-88 5-row + singles {16389,16390,
  16391} 68B each + B 16392-406 15-row + C fall-through 16407-16 10-row,
  10B tab) + Q branch (m=off&15, q=off>>4, tab=QT[m] 6B, b1=(Q1H[m]<<4)|
  Q1Q[q] if m<15 else Q1Q[q], b0=Q0[q], blk=QB[q] 7B). AST: S1-S3 68B,
  AT/BT/CT 5/15/10, QT/QB 16/4, Q1H/Q1Q/Q0 15/4/4 (Q1H[m] guarded by m<15
  short-circuit — m=15 never indexes it — SAFE). all indices in-range,
  contiguous after T9O2Q (16384 follows 16383). no imports/OSS/disasm.
- battery: GATE-PASS shipped legs (outdir gate-w2-b25a422-s4): HYGIENE/
  CONTAM clean, RGRAM n=2206, PINS-RGRAM set-eq 2206/2206, OSS none,
  LIBCOMP zero, ADOPT match. PLUS manual RED-cell re-verification @tip:
  N=15752 fresh bytes => CLOSED T9L1Q rc=0 (fix holds).
- verdict: PASS for THIS tip's code. FLAG-48ebfe0-hold STILL BLOCKS the
  range (15752 not restored — verified absent in this tip).
- NIT (no FAIL, persistent class): message "(2208 pins)" counts 2 csv
  comments; data rows 2206 (battery decisive).
- coverage: 147/148 PASS + 1 RED-held (48ebfe0; 992e514 RED-orphan).
