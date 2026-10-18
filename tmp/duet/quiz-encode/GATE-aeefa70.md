# GATE-aeefa70 sweep: PASS (rgram 1768/1768, T9C2 storm + Q 3x16)

- tip: lanes/encode-writer2 @aeefa70 (parent 007375f gated PASS). rgram.py
  +116/-0, cells to 14029, pins 1730->1768 (+38/-0).
- code read (ALL): C2 dispatch (dict-lit 5 + A 13956-70 15-row + B 13972-80
  9-row + gap-trap; b34 m-rule, b23 m==5 rule) + Q branch (m=(off-2025)&15,
  q=(off-2025)>>4, k15 early-edge QB[q]/QB[q+1]/QN, b24 edge @14029).
  AST: dict keys exactly {13953,13954,13955,13971,13981} (the 5 gaps),
  AT/BT/QT/QB lens 15/9/16/3 match ranges, QN LIVE (q=2&m=15 at last row
  off=2072; cf D1Q live vs B1/V1/X1 dead, A2 referenced-unreachable).
  coverage 5+15+9+48=77 cells. contiguous after T9B2 (13953 follows 13952).
  no imports/OSS/disasm markers.
- NIT (no FAIL, persistent class): message "(1770 pins)" counts 2 csv
  comments; data rows 1768 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-aeefa70-s4): HYGIENE/CONTAM clean,
  RGRAM n=1768, PINS-RGRAM set-eq 1768/1768, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 132/132 (NOTE-092 baseline + 25), ZERO holds.
