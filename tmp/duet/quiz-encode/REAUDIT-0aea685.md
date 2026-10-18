# REAUDIT-0aea685: band119 T10R99 (n<=52232, 710 tiers) — PASS

First-hand re-battery by encode-viewer4-r12
in fresh WS detached tree .../r12/reaudit-
0aea685/tree (git archive 0aea685, full SHA
0aea6857601cc4577ad9dba50804fe370f651895),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1570440 bytes).

- PYID (RGRAMC=own r12, corpus 3288 own-
  seat hardlinks ex r12 b123 cbat .rav,
  regen-missing, py+C freshly executed
  per pin): RGRAMC-PYID 3238/3238
  covered=3238/3238, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own r12, fresh oracle):
  6476 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z52232.
- PYBAT (python impl, fresh oracle): 6476
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z52232.
- PINS-RGRAM set-eq 6476/6476 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 51977..52232:
  pass=256 fail=0 pins=13 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; VERIFY reports
  26/26 = 13x2 closed+sha — same 13
  cells, pinfail=0.)
- Tables-EQ own script r12: NEW 2/2 EQ
  (_T10R99C/M); FULL 1838/1838 0-skip
  0-mismatch.
- Wall-grep PARENT-032 scope on band diff
  vs 0323580 (src/c/rgramc.c only,
  +975/-834 == VERIFY, cpat|libcompression|
  depload|dlopen|dylib): 0 hits. py+PINS+
  tests cmp-SAME 0323580. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands;
agrees with GATE/VERIFY on every leg).
Quiz diff 0 at file. No commits, no push.
