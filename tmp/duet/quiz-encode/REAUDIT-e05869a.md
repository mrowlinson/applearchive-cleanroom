# REAUDIT-e05869a: band117 T10R98 (n<=51884, 706 tiers) — PASS

First-hand re-battery by encode-viewer4-r12
in fresh WS detached tree .../r12/reaudit-
e05869a/tree (git archive e05869a, full SHA
e05869af038c5e3b965e5ad0bf6c0bcaca92c72b),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1553592 bytes).

- PYID (RGRAMC=own r12, corpus 3288 own-
  seat hardlinks ex r12 b123 cbat .rav,
  regen-missing, py+C freshly executed
  per pin): RGRAMC-PYID 3211/3211
  covered=3211/3211, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own r12, fresh oracle):
  6422 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z51884.
- PYBAT (python impl, fresh oracle): 6422
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z51884.
- PINS-RGRAM set-eq 6422/6422 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 51629..51884:
  pass=256 fail=0 pins=13 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; VERIFY reports
  26/26 = 13x2 closed+sha — same 13
  cells, pinfail=0.)
- Tables-EQ own script r12: NEW 3/3 EQ
  (_T10R98C/M/Q — 3-table band); FULL
  1826/1826 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band diff
  vs 0563d71 (src/c/rgramc.c only,
  +987/-828 == VERIFY, cpat|libcompression|
  depload|dlopen|dylib): 0 hits. py+PINS+
  tests cmp-SAME 0563d71. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands;
agrees with GATE/VERIFY on every leg).
Quiz diff 0 at file. No commits, no push.
