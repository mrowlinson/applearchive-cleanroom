# GATE-ef80529 sweep: PASS-individual (rgram 3872/3872; T10P45 ->32488)

- tip: lanes/encode-writer2 @ef80529 (parent 9ac84d5 gated).
  rgram +205/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P45 5 tiers raw-lencode — P450/P451 singletons
  76/76B + P45A 16x7B b21-23,68-71 + P45B 10x12B b13,14,20-25,72-75
  + P45Q 4x16 (P45M 16x7B b15,26,27,64-67 + P45Q-tab 4x10B
  b13,20-24,72-75 + TWO single-head byte rules: b14=M14[m]^
  (0x04 if q>=2) xor-bit + b25=M25[m]|(0x01 if q>=2) or-bit,
  M14/M25 16 ints). AST-verified (16/10/16/4, hex widths 14/24/
  14/20; consts 74/74/67/62/55 sorted no-dups; const-vs-tab
  disjoint + FULL cover every tier: 67+7+2/62+12+2/55+19+2).
  dispatch continuous 32397->32488, no neighbor edits. for-list
  +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-ef80529-s12):
  all green incl OUTER2 284 + RGRAM 3872 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, q>=2-bit BOTH ways: 32406 P45A, 32420 P45B,
  32430 off5/q0 no-bit, 32450 off25/q1 no-bit, 32470 off45/q2 bit.
- boundaries: 32397 P450 + 32488 P45Q-off63 CLOSED; 32489 rc=1
  GRAMMAR-BREAK paylen 80 (NOT rc=2: global paylen gate line 9472
  admits only ..76; oracle emits 80B pay at 32489 = 76B->80B
  REGIME TRANSITION, later tips confirm 80B pays). exact + proven.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 241/241 PASS-individual (w2) + cport 43 PASS-functional.
