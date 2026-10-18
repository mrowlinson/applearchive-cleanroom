# GATE-d80c7a8 sweep: PASS (rgram 1314/1314, T8D1 storm + Q 3x16)

- tip: lanes/encode-writer2 @d80c7a8 (parent bb54325 gated PASS). rgram.py
  +115/-0, cells to 11593, pins 1276->1314 (+38/-0).
- code read (ALL): D1 dispatch (dict-lit 5 + A 11520-34 15-row + B 11536-44
  9-row + gap-trap) + Q branch (m=(off-2811)&15, q=(off-2811)>>4, k15
  early-edge exp=QB[q]/QB[q+1]/QN, b5 m-cycle rule, b31 edge @11593).
  AST-verified: dict keys exactly {11517,11518,11519,11535,11545} (the 5
  gaps), AT/BT/QT/QB lens 15/9/16/3 match ranges, QN LIVE (q=2&m=15 last
  row; cf B1's dead QN nit). all indices in-range, contiguous after C1
  (11517 follows 11516). no imports/OSS/disasm markers.
- NIT (no FAIL, persistent class): message "(1316 pins)" counts 2 csv
  comments; data rows 1314 (battery decisive).
- battery: GATE-PASS (outdir gate-w2-d80c7a8-s4): HYGIENE/CONTAM clean,
  RGRAM n=1314, PINS-RGRAM set-eq 1314/1314, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 114/114 (NOTE-092 baseline + 7), ZERO holds.
