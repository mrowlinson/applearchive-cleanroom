# REAUDIT-49f108c (viewer4 r10): band149 T10R114 (n<=57452) — PASS

First-hand in fresh WS detached tree
.../reaudit-49f108c/tree (git archive
49f108c, full SHA 49f108cd373759bdb5d
addcc28cdf8f07a98eab2), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1740904 bytes). Merged 277108a.
CLAIM-viewer4-49f108c-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3607
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3607/3607 covered=3607/3607,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7214 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z57452.
- PYBAT (python impl): 7214 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z57452.
- PINS-RGRAM set-eq 7214/7214 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 57197..57452:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R114C/_T10R114M);
  FULL 2029/2029 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 47e94d0 (src/c/rgramc.c only,
  +1070/-929, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7216 lines (7214+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
