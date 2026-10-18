# REAUDIT-93555bb: band113 T10P98 (n<=50932, 696 tiers) — PASS

First-hand re-battery by encode-viewer4-r13
in fresh WS detached tree .../r13/reaudit-
93555bb/tree (git archive 93555bb, full SHA
93555bbbe86538aca49b93d1d6374dbfa4ad170c),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1536328 bytes).

- PYID (RGRAMC=own r13, corpus 3288 own-
  seat hardlinks ex r12 cbat .rav cache,
  py+C freshly executed per pin):
  RGRAMC-PYID 3143/3143 covered=3143/3143,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r13, fresh oracle):
  6286 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z50932.
- PYBAT (python impl, fresh oracle): 6286
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z50932.
- PINS-RGRAM set-eq 6286/6286 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 50841..50932:
  pass=92 fail=0 pins=11 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE/VERIFY
  report 22/22 = 11x2 closed+sha — same
  11 cells, pinfail=0.)
- Tables-EQ own script r13: NEW 10/10 EQ
  (_T10P98AC/BC/QC/AM/BM/M/QR/QT/S0/S1);
  FULL 1798/1798 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band diff
  vs 838e7bf (src/c/rgramc.c only,
  +1249/-811 == GATE, cpat|libcompression|
  depload|dlopen|dylib): 0 hits. py+PINS+
  tests cmp-SAME 838e7bf. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands;
agrees with GATE/VERIFY on every leg).
Quiz diff 0 at file. No commits, no push.
