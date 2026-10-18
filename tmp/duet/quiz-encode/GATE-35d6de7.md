# GATE-35d6de7 sweep: PASS-individual (rgram 3632/3632; T10P39 ->30400)

- tip: lanes/encode-writer2 @35d6de7 (parent b1f4334 gated).
  rgram +202/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P39 5 tiers xor-lencode (^0x8000 back) EXCEPT
  P390 singleton raw ("b5 raw-high quirk") — P390/P391 76/76B +
  P39A 16x7B b13-15,60-63 + P39B 10x10B b0-2,11,16,17,72-75
  (b0-tabbed) + P39Q 4x16 (P39M 16x5B b18,68-71 + P39Q-tab 4x9B
  b0-2,11,16,72-75 + NEW b17 rule: pay[17]=QB[q]^(0x80 if m in
  {1,2,3,4,5,8,9,10}), QB=(0x4e,0x4c,0x4f,0x4e)). AST-verified
  (16/10/16/4, hex widths 14/20/10/18; consts 74/74/67/64/59
  sorted no-dups; const-vs-tab disjoint + FULL cover every tier:
  67+7+2/64+10+2/59+15+2). dispatch continuous 30309->30400,
  no neighbor edits. for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-35d6de7-s12):
  all green incl OUTER2 284 + RGRAM 3632 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, b17 rule BOTH ways: 30318 P39A, 30332 P39B,
  30338 off1/m1 IN, 30343 off6/m6 OUT, 30360 off23/m7 OUT.
- boundaries: 30309 P390 + 30400 P39Q-off63 CLOSED; 30401 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 229/229 PASS-individual (w2) + cport 33 PASS-functional.
