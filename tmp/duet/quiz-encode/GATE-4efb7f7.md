# GATE-4efb7f7 sweep: PASS-individual (rgram 2860/2860; T10R17 ->23348)

- tip: lanes/encode-writer2 @4efb7f7 (parent 0d64e0a gated).
  rgram +51/-0 pure addition, for-list +8, pins +16 rows
  append-only.
- code read (FULL): _T10R17M 16-tab 6B (b29,30,72-75) +
  _T10R17Q 16-tab 7B (b24-26,60-63) + _T10R17C 61 consts
  + dispatch (paylen 76 enforced, lencode, b5 0xb4 +
  (off>=75)+(off>=203) dbl-carry). counts AST-verified
  (16/16/61, widths 12/14 hex; const idx sorted, no dups,
  maxidx 71). const-vs-tab disjoint. dispatch after PIQ,
  chain continuous, no neighbor edits. for-list straddles
  both carry edges (74/75, 202/203).
- battery: GATE-PASS shipped legs (outdir gate-w2-4efb7f7-s10):
  all green incl PINS set-eq 284/47/181; RGRAM n=2860
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 23123 (off30), 23193 (off100),
  23243 (off150), 23313 (off220), 23333 (off240).
  unpinned-ness grepped vs PINS first.
- boundaries: 23092 pinned PIQ still GREEN in RGRAM run;
  23349 rc=2 out of scope own bytes.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 188/189 PASS-individual + 1 RED-cleared
  (48ebfe0 history) + 1 flake-cleared (ndp2 test-side).
  ZERO holds vs NOTE-092 baseline.
