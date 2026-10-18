# GATE-b1f4334 sweep: PASS-individual (rgram 3612/3612; T10R37 ->30308)

- tip: lanes/encode-writer2 @b1f4334 (parent 1b1e2f3 gated).
  rgram +49/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R37 16x16 76B-pay raw-lencode (off=n-30053,
  NEW b5 m-bit set {0,1,9,10,11,12,13,14} xor 0x80, m-tab b6,7,68-71
  16x6B + qhead b29,30 16x2B R37QH + qtab _T10P38M[q][2:] 6B
  @b42,43,64-67 + 60 consts). AST-verified (M16 w12, QH16 w4,
  C60 sorted no-dups, const-vs-tab disjoint + FULL cover 60+14+2).
  dispatch continuous 30053->30308, no neighbor edits. for-list +10
  straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-b1f4334-s12):
  all green incl OUTER2 284 + RGRAM 3612 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, b5 set BOTH ways: 30054 m1 IN, 30055 m2 OUT,
  30062 m9 IN, 30150 off97/m1 IN, 30200 off147/m3 OUT.
- boundaries: 30053 off0 + 30308 off255 CLOSED; 30309 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 228/228 PASS-individual (w2) + cport 32 PASS-functional.
