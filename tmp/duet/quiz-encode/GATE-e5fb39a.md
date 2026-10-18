# GATE-e5fb39a sweep: PASS-individual (rgram 3220/3220; T10R27 ->26828)

- tip: lanes/encode-writer2 @e5fb39a (parent 1492d3a gated).
  rgram +43/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R27 16x16 76B (m-tab 16x6B b18,19,68-71 NEW +
  q-tab = _T10PSM[q] REUSE 16x6B b13,14,64-67 + b5 0x4f+
  (off>=51)+(off>=179) dbl-carry). counts AST-verified (16/62;
  hex width 12; PSM width 12 confirmed; const idx sorted, no dups,
  max 75). const-vs-tab disjoint + FULL cover (62+12+2=76).
  dispatch after PSQ, chain continuous, no neighbor edits. for-list
  straddles BOTH carry edges (50/51, 178/179) + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-e5fb39a-s12):
  all green incl PINS set-eq 284/47/181/3220; RGRAM n=3220
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3221 pins" but csv + battery = 3220 (3204+16). off-by-one
  (16th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 26600, 26680, 26720, 26800, 26820.
- boundaries: 26572 pinned PSQ still GREEN; 26829 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 208/209 PASS-individual (w2) + cport 17 PASS-functional.
