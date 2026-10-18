# GATE-ea1b509 sweep: PASS-individual (rgram 3832/3832; T10P44 ->32140)

- tip: lanes/encode-writer2 @ea1b509 (parent cf113e3 gated).
  rgram +205/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P44 5 tiers xor-lencode, THREE b5 mechanisms —
  P440/P441 singletons 76/76B + P44A 16x6B b6,7,68-71 + b5 off-set
  {0,9,14} + P44B 10x9B b6-10,72-75 + b5 off-set {1,2,3,4,5,6,7,9}
  (all but 0,8) + P44Q 4x16 (P44M 16x7B b0-2,68-71 b0-tabbed +
  P44Q-tab 4x9B b6-10,72-75 + b5-raw iff q>=1: pay[5] vs xor-high
  ^(0x80 if q>=1)). AST-verified (16/10/16/4, hex widths 12/18/14/
  18; consts 74/74/68/65/58 sorted no-dups; const-vs-tab disjoint
  + FULL cover every tier: 68+6+2/65+9+2/58+16+2). dispatch
  continuous 32049->32140, no neighbor edits. for-list +10
  straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-ea1b509-s12):
  all green incl OUTER2 284 + RGRAM 3832 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, ALL THREE b5 rules BOTH ways: 32052 A-off1
  OUT, 32060 A-off9 IN, 32068 B-off1 IN, 32080 Q-off3/q0 OUT,
  32100 Q-off23/q1 IN.
- boundaries: 32049 P440 + 32140 P44Q-off63 CLOSED; 32141 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 239/239 PASS-individual (w2) + cport 41 PASS-functional.
