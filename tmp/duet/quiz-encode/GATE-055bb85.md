# GATE-055bb85 sweep: PASS-individual (rgram 2968/2968; T10R20 ->24392)

- tip: lanes/encode-writer2 @055bb85 (parent 5d92e24 gated).
  rgram +51/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R20 16x16 76B (m-tab 16x6B b37,38,72-75 +
  q-tab 16x5B b32,68-71 NEW + b5 0xbc+(off>=55)+(off>=183)
  dbl-carry). counts AST-verified (16/16/63; hex widths 12/10;
  const idx sorted, no dups, max 67). const-vs-tab disjoint +
  FULL cover (63+11+2=76). dispatch after PLQ, chain continuous,
  no neighbor edits. for-list straddles BOTH carry edges (54/55,
  182/183) + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-055bb85-s12):
  all green incl PINS set-eq 284/47/181/2968; RGRAM n=2968
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "2969 pins" but csv + battery = 2968 (2952+16). off-by-one
  (same class as P21 "2953").
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 24150, 24200, 24250, 24300, 24350.
  unpinned-ness grepped vs PINS first.
- boundaries: 24136 pinned PLQ still GREEN in RGRAM run;
  24393 rc=2 out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 194/195 PASS-individual (w2) + cport 0/4-held.
