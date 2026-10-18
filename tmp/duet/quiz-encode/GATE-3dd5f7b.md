# GATE-3dd5f7b sweep: PASS-individual (rgram 3472/3472; T10P35 ->29008)

- tip: lanes/encode-writer2 @3dd5f7b (parent 2c07079 gated).
  rgram +198/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P35 5 tiers plain-l16 — PZ0/PZ1 singletons 76/76B
  + PZA 16x6B b33,34,68-71 + PZB 10x10B b25,33-37,72-75 +
  PZQ 4x16 (PZM 16x7B b37-39,68-71 + PZQ-tab 4x9B b28,32-35,72-75).
  AST-verified (16/10/16/4, hex widths 12/20/14/18; consts
  74/74/68/64/58 sorted no-dups; const-vs-tab disjoint + FULL
  cover every tier: 68+6+2/64+10+2/58+16+2). dispatch continuous
  28917->29008, no neighbor edits. for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-3dd5f7b-s12):
  all green incl RGRAM 3472 + PINS set-eq 3472 (tip tree). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 28926 PZA, 28940 PZB, 28955/28980/29000 PZQ.
- boundaries: 28917 PZ0 + 29008 PZQ-off63 CLOSED; 29009 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 221/221 PASS-individual (w2) + cport 26 PASS-functional.
