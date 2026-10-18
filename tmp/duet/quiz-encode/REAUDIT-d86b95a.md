# REAUDIT-d86b95a (viewer4 r10): band141 T10R110 (n<=56060) — PASS

First-hand in fresh WS detached tree
.../reaudit-d86b95a/tree (git archive
d86b95a, full SHA d86b95ac0d24769e1b5
d609aa68f7409149d3728), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1689864 bytes). Merged 4873497.
CLAIM-viewer4-d86b95a-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3510
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3510/3510 covered=3510/3510,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7020 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z56060.
- PYBAT (python impl): 7020 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z56060.
- PINS-RGRAM set-eq 7020/7020 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 55805..56060:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 3/3 EQ (_T10R110C/_T10R110M/
  _T10R110QH); FULL 1975/1975 0-skip
  0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs ef02d89 (src/c/rgramc.c only,
  +1062/-901, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7022 lines (7020+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
