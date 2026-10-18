# GATE-39ef22c sweep: PASS (rgram 1114/1114, T8V storm)

- tip: lanes/encode-writer2 @39ef22c (parent 87d9a4f gated PASS). rgram.py
  +173/-0 (3 lits + V1-15 + V2S + V2-9 + V3S + V3-15 + V4 3x16), cells to
  10216, pins 1086->1114 (+28/-0).
- code read (ALL): 9 tables (V0 3, V1T 15, V2T 9, V3T 15, V4T 16, V4B 3 +
  consts) + 7 branches monotone contiguous (off 1390..1481: V0 10127/V1/
  V2S 10143/V2/V3S 10153/V3/V4 10216). every index hand-bounded in-range
  (V1 15, V2 9, V3 15, V4 m16/q3). no imports/OSS/disasm markers.
- battery: GATE-PASS (outdir gate-w2-39ef22c-s4): HYGIENE/CONTAM clean,
  RGRAM n=1114, PINS-RGRAM set-eq 1114/1114, OSS none, LIBCOMP zero, ADOPT
  match (zero FAIL lines).
- coverage: 89/89 writer tips gated (89 battery-PASS, ZERO holds).
