# GATE-4673e2e sweep: PASS (rgram 1618/1618, T9X1 storm + Q 4x16)

- tip: lanes/encode-writer2 @4673e2e (parent 58f0cd5 gated PASS). rgram.py
  +121/-0, cells to 13348, pins 1580->1618 (+38/-0).
- code read (ALL): X1 dispatch (dip 13257 64B + dict-lit 4 + A 13260-74
  15-row + B 13276-84 9-row + gap-trap) + Q branch (m=(off-1329)&15,
  q=(off-1329)>>4, k15 early-edge QB[q]/QB[q+1], q1-m10..14 byte0 patch
  to 0x68). AST: dip 64B, dict keys exactly {13258,13259,13275,13285}
  (the 4 gaps), AT/BT/QT/QB lens 15/9/16/4 match ranges, QB[q+1] safe
  (m=15&q=3 needs off 1392 > max 1391, unreachable). coverage 1+4+15+9+
  63=92 cells. contiguous after T9W1 (13257 follows 13256). no imports/
  OSS/disasm markers.
- NITS (no FAIL): (1) _T9X1QN defined, never referenced (dead 11B const;
  3rd occurrence: B1, V1, X1 — pattern, still harmless). (2) Q branch has
  NO b5 assertion (weaker b5 verification on these cells; oracle-agreement
  on pinned cells still decisive). (3) message "(1620 pins)" counts 2 csv
  comments; data rows 1618 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-4673e2e-s4): HYGIENE/CONTAM clean,
  RGRAM n=1618, PINS-RGRAM set-eq 1618/1618, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 127/127 (NOTE-092 baseline + 20), ZERO holds.
