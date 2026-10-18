# REAUDIT-c1cd305 (viewer4 r10): band153 T10R116 (n<=58148) — PASS

First-hand in fresh WS detached tree
.../reaudit-c1cd305/tree (git archive
c1cd305, full SHA c1cd305964f5ff3e283
4168edd7d5f06cce2d5e1), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1758136 bytes). Merged a6e18c4.
CLAIM-viewer4-c1cd305-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3656
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3656/3656 covered=3656/3656,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7312 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z58148.
- PYBAT (python impl): 7312 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z58148.
- PINS-RGRAM set-eq 7312/7312 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 57893..58148:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R116C/_T10R116M);
  FULL 2055/2055 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs bfa3762 (src/c/rgramc.c only,
  +1084/-943, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7314 lines (7312+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
