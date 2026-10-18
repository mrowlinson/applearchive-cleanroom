# GATE-25b36b0 sweep: PASS-individual (rgram 3792/3792; T10P43 ->31792)

- tip: lanes/encode-writer2 @25b36b0 (parent 0c7b7fe gated).
  rgram +198/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P43 5 tiers plain-xor-lencode — P430/P431
  singletons 76/76B + P43A 16x6B b32,33,68-71 + P43B 10x12B
  b28,29,32-37,72-75 + P43Q 4x16 (P43M 16x7B b37-39,72-75 +
  P43Q-tab 4x9B b32-36,68-71). AST-verified (16/10/16/4, hex
  widths 12/24/14/18; consts 74/74/68/62/58 sorted no-dups;
  const-vs-tab disjoint + FULL cover every tier: 68+6+2/62+12+2/
  58+16+2). dispatch continuous 31701->31792, no neighbor edits.
  for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-25b36b0-s12):
  all green incl OUTER2 284 + RGRAM 3792 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 31710 P43A, 31724 P43B, 31736/31760/31780 P43Q.
- boundaries: 31701 P430 + 31792 P43Q-off63 CLOSED; 31793 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 237/237 PASS-individual (w2) + cport 40 PASS-functional.
