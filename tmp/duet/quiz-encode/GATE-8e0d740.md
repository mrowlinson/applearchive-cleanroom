# GATE-8e0d740 sweep: PASS-individual (rgram 3332/3332; T10R30 ->27872)

- tip: lanes/encode-writer2 @8e0d740 (parent c406622 gated).
  rgram +47/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): T10R30 16x16 76B (m-tab 16x6B b21,22,72-75 NEW +
  qhead 16x2B b17,18 NEW + qtab = _T10PVM[q][4:] SUFFIX 4B b68-71 +
  NEW 2-byte lencode l16=(((n<<1)|1)^0x8000)&0xFFFF across b4+b5).
  counts AST-verified (16/16/62; hex widths 12/4; PVM suffix width
  8 confirmed; const idx sorted, no dups, max 67). const-vs-tab
  disjoint + FULL cover (62+12+2=76). dispatch after PVQ, chain
  continuous, no neighbor edits. for-list dense: 10 cells incl
  off14/15, off30/31, off158/159, off254/255 pairs.
- battery: GATE-PASS shipped legs (outdir gate-w2-8e0d740-s12):
  all green incl PINS set-eq 284/47/181/3332; RGRAM n=3332
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 27660, 27700, 27800, 27840, 27865.
- boundaries: 27616 pinned PVQ still GREEN; 27873 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 214/215 PASS-individual (w2) + cport 21 PASS-functional.
