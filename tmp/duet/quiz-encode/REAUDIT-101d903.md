# REAUDIT-101d903 (viewer4 r10): band129 T10R104 (n<=53972) — PASS

First-hand in fresh WS detached tree
.../reaudit-101d903/tree (git archive
101d903, full SHA 101d90354c93e707f5e
4ff89475b866d2b9c9c61), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1621720 bytes). Merged 6075169.
CLAIM-viewer4-101d903-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3362
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3362/3362 covered=3362/3362,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 6724 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z53972.
- PYBAT (python impl): 6724 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z53972.
- PINS-RGRAM set-eq 6724/6724 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 53717..53972:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R104C/_T10R104M);
  FULL 1901/1901 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 20df34c (src/c/rgramc.c only,
  +1006/-865, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 6726 lines (6724+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
