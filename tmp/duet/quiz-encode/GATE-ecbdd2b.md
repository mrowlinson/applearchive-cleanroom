# GATE-ecbdd2b sweep: PASS-individual (rgram 2880/2880; T10P19 ->23440)

- tip: lanes/encode-writer2 @ecbdd2b (parent 4efb7f7 gated).
  rgram +168/-0 pure addition, for-list +10, pins +20 rows
  append-only.
- code read (FULL): PJ0/PJ1 singleton const tables (72B) +
  PJA 16-tab 6B (b37,38,72-75; 76B mixed) + PJB 10-tab 10B
  (b17,32-36,68-71; 72B) + PJQ 4x16 76B (m-tab 7B
  b40-42,68-71 + q-tab 10B b28,29,36-39,72-75 + b5 0xb6+
  (off>=47)). counts AST-verified (PJA16/PJB10/PJM16/PJQ4,
  widths 12/20/14/20 hex; consts 71/71/69/61/57, idx
  sorted, no dups, maxidx in-paylen). const-vs-tab
  disjoint all 5 sections. dispatch chain continuous
  23348->23349..23440, then out-of-scope. for-list
  straddles b5 carry (46/47). no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-ecbdd2b-s10):
  all green incl PINS set-eq 284/47/181; RGRAM n=2880
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 23359 (PJA off8), 23372 (PJB off5),
  23397 (PJQ off20 q1), 23412 (PJQ off35 q2), 23432 (PJQ
  off55 q3). unpinned-ness grepped vs PINS first.
- boundaries: 23348 pinned R17 still GREEN in RGRAM run;
  23441 rc=2 out of scope own bytes.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 189/190 PASS-individual + 1 RED-cleared
  (48ebfe0 history) + 1 flake-cleared (ndp2 test-side).
  ZERO holds vs NOTE-092 baseline.
