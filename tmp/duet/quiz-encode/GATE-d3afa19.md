# GATE-d3afa19 sweep: PASS-individual (rgram 3076/3076; T10R23 ->25436)

- tip: lanes/encode-writer2 @d3afa19 (parent 875a127 gated).
  rgram +50/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R23 16x16 76B (m-tab 16x8B b40-43,56-59 NEW +
  q-tab 16x6B b36,37,72-75 NEW + b5 0xc4+(off>=35)+(off>=163)
  dbl-carry). counts AST-verified (16/16/60; hex widths 16/12;
  const idx sorted, no dups, max 71). const-vs-tab disjoint +
  FULL cover (60+14+2=76). dispatch after POQ, chain continuous,
  no neighbor edits. for-list straddles BOTH carry edges (34/35,
  162/163) + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-d3afa19-s12):
  all green incl PINS set-eq 284/47/181/3076; RGRAM n=3076
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3077 pins" but csv + battery = 3076 (3060+16). off-by-one
  (8th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 25200, 25250, 25300, 25380, 25420.
- boundaries: 25180 pinned POQ still GREEN; 25437 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 200/201 PASS-individual (w2) + cport 0/11-held.
