# GATE-55dcb98 sweep: PASS-individual (rgram 3672/3672; T10P40 ->30748)

- tip: lanes/encode-writer2 @55dcb98 (parent f6dfa38 gated).
  rgram +198/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P40 5 tiers plain-xor-lencode — P400/P401
  singletons 76/76B + P40A 16x7B b14,26,27,68-71 + P40B 10x18B
  b2,14,15,25-35,72-75 (widest B-tab so far) + P40Q 4x16 (P40M
  16x5B b32,68-71 + P40Q-tab 4x11B b14,15,25-29,72-75).
  AST-verified (16/10/16/4, hex widths 14/36/10/22; consts
  74/74/67/56/58 sorted no-dups; const-vs-tab disjoint + FULL
  cover every tier: 67+7+2/56+18+2/58+16+2). dispatch continuous
  30657->30748, no neighbor edits. for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-55dcb98-s12):
  all green incl OUTER2 284 + RGRAM 3672 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 30666 P40A, 30680 P40B, 30692/30720/30740 P40Q.
- boundaries: 30657 P400 + 30748 P40Q-off63 CLOSED; 30749 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 231/231 PASS-individual (w2) + cport 35 PASS-functional.
