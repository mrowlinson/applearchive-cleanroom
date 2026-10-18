# GATE-c108d1e sweep: PASS-individual (rgram 3512/3512; T10P36 ->29356)

- tip: lanes/encode-writer2 @c108d1e (parent b490c4e gated).
  rgram +202/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P36 5 tiers — P360/P361 singletons 76/76B +
  P36A 16x6B b6,7,68-71 + NEW b5 off-set rule (off in
  {1,5,6,9,10,11,12,13,14,15} xor 0x80; off-based, not m/q-based) +
  P36B 10x9B b6-10,72-75 + P36Q 4x16 (P36M 16x6B b13,14,64-67 +
  P36Q-tab 4x9B b6-10,72-75, plain l16). AST-verified (16/10/16/4,
  hex widths 12/18/12/18; consts 74/74/68/65/59 sorted no-dups;
  const-vs-tab disjoint + FULL cover every tier: 68+6+2/65+9+2/
  59+15+2). dispatch continuous 29265->29356, no neighbor edits.
  for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-c108d1e-s12):
  all green incl RGRAM 3512 + PINS set-eq 3512 (tip tree). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, b5 rule BOTH ways: 29269 off2 OUT, 29272
  off5 IN, 29275 off8 OUT (P36A) + 29288 P36B + 29320 P36Q.
- boundaries: 29265 P360 + 29356 P36Q-off63 CLOSED; 29357 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 223/223 PASS-individual (w2) + cport 28 PASS-functional.
