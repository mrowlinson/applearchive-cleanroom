# REAUDIT-fd438da (viewer4 r10): band147 T10R113 (n<=57104) — PASS

First-hand in fresh WS detached tree
.../reaudit-fd438da/tree (git archive
fd438da, full SHA fd438da88fe3a3575e7
554b7be8982146af5ab01), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1724040 bytes). Merged 0fc5df4.
CLAIM-viewer4-fd438da-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3583
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3583/3583 covered=3583/3583,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7166 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z57104.
- PYBAT (python impl): 7166 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z57104.
- PINS-RGRAM set-eq 7166/7166 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 56849..57104:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 3/3 EQ (_T10R113C/_T10R113M/
  _T10R113QH); FULL 2016/2016 0-skip
  0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs cddf1f3 (src/c/rgramc.c only,
  +1083/-922, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7168 lines (7166+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
