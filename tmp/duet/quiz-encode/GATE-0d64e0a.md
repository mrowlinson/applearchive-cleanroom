# GATE-0d64e0a sweep: PASS-individual (rgram 2844/2844; T10P18 ->23092)

- tip: lanes/encode-writer2 @0d64e0a (parent a04cb82 gated).
  rgram +171/-0 pure addition, for-list +11, pins +22 rows
  append-only.
- code read (FULL): PI0/PI1 singleton const tables (72B) +
  PIA 16-tab 6B (b20,21,72-75; 76B mixed) + PIB 10-tab 9B
  (b16-20,68-71; 72B) + PIQ 4x16 (m-tab 6B b21,22,56-59
  + q-tab 9B b2,3,13-15,68-71 + b20 col -(q==3) + b5
  0xb3+(off>=11)). counts AST-verified (PIA16/PIB10/PIM16/
  PIQ4, widths 12/18/12/18 hex; consts 71/71/69/62/54,
  idx sorted, no dups, maxidx in-paylen). const-vs-tab
  bytes disjoint all 5 sections. dispatch chain continuous
  23000->23001..23092, then out-of-scope. no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-0d64e0a-s10):
  HYGIENE/CONTAM/SMOKE n=6/OUTER2 n=284/RB2 n=47/
  RAVFRAME n=181/PINS set-eq 284/47/181/OSS/LIBCOMPRESSION/
  ADOPT all green; RGRAM n=2844 rc=0 zero FAIL (tip tree,
  NVME workdir). OUTER2 green, no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 23010 (PIA off7), 23023 (PIB off4),
  23054 (PIQ off25 q1), 23064 (PIQ off35 q2), 23084 (PIQ
  off55 q3, b20-adjust path). unpinned-ness grepped first.
- boundaries: 23000 pinned T10R16 still GREEN in RGRAM run
  (no neighbor drift); 23093 rc=2 out of scope own bytes.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 187/188 PASS-individual + 1 RED-cleared
  (48ebfe0 history) + 1 flake-cleared (ndp2 test-side).
  ZERO holds vs NOTE-092 baseline.
