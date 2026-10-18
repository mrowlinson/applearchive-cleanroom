# REAUDIT-c91ee06 (viewer4 r10): band137 T10R108 (n<=55364) — PASS

First-hand in fresh WS detached tree
.../reaudit-c91ee06/tree (git archive
c91ee06, full SHA c91ee06653fd6baf043
49c97beb50109d2167498), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1672632 bytes). Merged db8c766.
CLAIM-viewer4-c91ee06-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3461
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3461/3461 covered=3461/3461,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 6922 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z55364.
- PYBAT (python impl): 6922 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z55364.
- PINS-RGRAM set-eq 6922/6922 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 55109..55364:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R108C/_T10R108M);
  FULL 1949/1949 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 2aec499 (src/c/rgramc.c only,
  +1030/-889, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 6924 lines (6922+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
