# GATE-a0e16b3 sweep: PASS-individual (rgram 3752/3752; T10P42 ->31444)

- tip: lanes/encode-writer2 @a0e16b3 (parent 497b4f4 gated).
  rgram +202/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P42 5 tiers xor-lencode — P420/P421 singletons
  76/76B + P42A 16x6B b16,17,68-71 + P42B 10x16B b2,12-15,17-23,
  72-75 + P42Q 4x16 (P42M 16x6B b22,23,72-75 + P42Q-tab 4x9B
  b16-20,68-71 + NEW b21 subtractive rule: pay[21]=MB[m]-(q==1),
  MB 16 ints). AST-verified (16/10/16/4, hex widths 12/32/12/18;
  consts 74/74/68/58/58 sorted no-dups; const-vs-tab disjoint +
  FULL cover every tier: 68+6+2/58+16+2/58+16+2). dispatch
  continuous 31353->31444, no neighbor edits. for-list +10
  straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-a0e16b3-s12):
  all green incl OUTER2 284 + RGRAM 3752 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, b21 rule BOTH ways: 31362 P42A, 31376 P42B,
  31390 off9/q0 no-sub, 31400 off19/q1 sub, 31430 off49/q3 no-sub.
- boundaries: 31353 P420 + 31444 P42Q-off63 CLOSED; 31445 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 235/235 PASS-individual (w2) + cport 38 PASS-functional.
