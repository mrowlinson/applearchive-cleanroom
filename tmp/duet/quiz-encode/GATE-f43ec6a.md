# GATE-f43ec6a sweep: PASS-individual (rgram 3552/3552; T10P37 ->29704)

- tip: lanes/encode-writer2 @f43ec6a (parent 965f4dd gated).
  rgram +198/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P37 5 tiers, NEW raw-lencode regime (l16 =
  ((n<<1)|1)&0xFFFF, NO ^0x8000 flip) — P370/P371 singletons 76/76B
  + P37A 16x6B b21,22,68-71 + P37B 10x11B b0,20-25,72-75 (b0-tabbed)
  + P37Q 4x16 (P37M 16x7B b28-30,68-71 + P37Q-tab 4x11B b14,20-25,
  72-75). AST-verified (16/10/16/4, hex widths 12/22/14/22; consts
  74/74/68/63/56 sorted no-dups; const-vs-tab disjoint + FULL
  cover every tier: 68+6+2/63+11+2/56+18+2). dispatch continuous
  29613->29704, no neighbor edits. for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-f43ec6a-s12):
  all green incl OUTER2 284 + RGRAM 3552 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 29622 P37A, 29636 P37B, 29650/29680/29695 P37Q.
- boundaries: 29613 P370 + 29704 P37Q-off63 CLOSED; 29705 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 225/225 PASS-individual (w2) + cport 30 PASS-functional.
