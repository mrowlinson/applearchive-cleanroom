# GATE-4278aac sweep: PASS (rgram 1710/1710, T9A2 storm + Q 4x16)

- tip: lanes/encode-writer2 @4278aac (parent 14a3807 gated PASS). rgram.py
  +125/-0, cells to 13696, pins 1668->1710 (+42/-0).
- code read (ALL): A2 dispatch (dip 13605 64B + dict-lit 5 + A 13608-22
  15-row + B 13625-32 8-row + gap-trap) + Q branch (m=(off-1677)&15,
  q=(off-1677)>>4, k15 early-edge QB[q]/QB[q+1]/QN, b5 tail @13696 only,
  b13 m-rule). AST: dip 64B, dict keys exactly {13606,13607,13623,13624,
  13633} (the 5 gaps), AT/BT/QT/QB lens 15/8/16/4 match ranges, QB[q+1]
  safe (m=15&q=3 needs off 1740 > max 1739, unreachable). coverage 1+5+
  15+8+63=92 cells. contiguous after T9Z1 (13605 follows 13604). no
  imports/OSS/disasm markers.
- NITS (no FAIL): (1) _T9A2QN referenced but its arm (m=15&q=3) is
  unreachable — effectively dead fallback (4th QN occurrence: B1/V1/X1
  def-only, A2 referenced-unreachable). (2) message "(1712 pins)" counts
  2 csv comments; data rows 1710 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-4278aac-s4): HYGIENE/CONTAM clean,
  RGRAM n=1710, PINS-RGRAM set-eq 1710/1710, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 130/130 (NOTE-092 baseline + 23), ZERO holds.
