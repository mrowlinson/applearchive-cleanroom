# GATE-8e4f4f2 sweep: PASS-individual (rgram 3352/3352; T10P32 ->27964)

- tip: lanes/encode-writer2 @8e4f4f2 (parent 8e0d740 gated).
  rgram +198/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): PW0/PW1 singletons (76/76B) + PWA 16x7B
  b28-30,68-71 + PWB 10x10B b28-33,72-75 + PWQ 4x16 76B (PWM 16x6B
  b33,34,72-75 + PWQ-tab 4x10B b0,1,25-27,32,68-71 b0-tabbed; b5
  in l16, no separate rule). l16 2-byte lencode regime throughout.
  counts AST-verified (74/74/16/67/10/64/16/4/58; hex widths
  14/20/12/20; const idx sorted, no dups). const-vs-tab disjoint
  + FULL cover every tier (74+2/74+2/67+7+2/64+10+2/58+6+10+2).
  dispatch continuous 27872->27964, no neighbor edits. for-list
  straddles all edges incl m15q0/m0q1 (off15/16).
- battery: GATE-PASS shipped legs (outdir gate-w2-8e4f4f2-s12):
  all green incl PINS set-eq 284/47/181/3352; RGRAM n=3352
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 27880 PWA, 27895 PWB, 27910/27940/27955 PWQ.
- boundaries: 27872 pinned R30 still GREEN; 27965 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 215/216 PASS-individual (w2) + cport 22 PASS-functional.
