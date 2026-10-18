# GATE-f242a57 sweep: PASS-individual (rgram 2896/2896; T10R18 ->23696)

- tip: lanes/encode-writer2 @f242a57 (parent ecbdd2b gated).
  rgram +42/-0 pure addition, for-list +8, pins +16 rows
  append-only.
- code read (FULL): _T10R18M 16-tab 7B (b45-47,68-71) +
  q-tab reuses _T10PJM[q] (7B values, read at b40-42,64-67
  — value-reuse at new positions vs PJQ's b40-42,68-71) +
  _T10R18C 60 consts + dispatch (paylen 76, lencode, b5
  0xb7+(off>=111)+(off>=239) dbl-carry). counts AST-verified
  (16/16/60, widths 14/14 hex; const idx sorted, no dups,
  maxidx 75). const-vs-tab disjoint. PJM width 14hex = 7B
  matches q-check byte count. dispatch after PJQ, chain
  continuous, no neighbor edits. for-list straddles both
  carry edges (110/111, 238/239).
- battery: GATE-PASS shipped legs (outdir gate-w2-f242a57-s10):
  all green incl PINS set-eq 284/47/181; RGRAM n=2896
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 23481 (off40), 23591 (off150),
  23621 (off180), 23641 (off200), 23691 (off250).
  unpinned-ness grepped vs PINS first.
- boundaries: 23440 pinned PJQ still GREEN in RGRAM run;
  23697 rc=2 out of scope own bytes.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 190/191 PASS-individual + 1 RED-cleared
  (48ebfe0 history) + 1 flake-cleared (ndp2 test-side).
  ZERO holds vs NOTE-092 baseline.
