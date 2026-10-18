# REAUDIT-c56c1e6 (viewer4 r10): band139 T10R109 (n<=55712) — PASS

First-hand in fresh WS detached tree
.../reaudit-c56c1e6/tree (git archive
c56c1e6, full SHA c56c1e6dab49e477bb89
9b41a65e2fff71a9dd9b), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1689480 bytes). Merged 71afeb0.
CLAIM-viewer4-c56c1e6-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3486
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3486/3486 covered=3486/3486,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 6972 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z55712.
- PYBAT (python impl): 6972 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z55712.
- PINS-RGRAM set-eq 6972/6972 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 55457..55712:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R109C/_T10R109M);
  FULL 1961/1961 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs c3a7a9b (src/c/rgramc.c only,
  +1036/-895, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 6974 lines (6972+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
