# REAUDIT-04cafeb (viewer4 r10): band145 T10R112 (n<=56756) — PASS

First-hand in fresh WS detached tree
.../reaudit-04cafeb/tree (git archive
04cafeb, full SHA 04cafeb85d5655dee33
e490f35cb5d4bf8422a1e), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1707096 bytes). Merged 8fedc13.
CLAIM-viewer4-04cafeb-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3558
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3558/3558 covered=3558/3558,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7116 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z56756.
- PYBAT (python impl): 7116 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z56756.
- PINS-RGRAM set-eq 7116/7116 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 56501..56756:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R112C/_T10R112M);
  FULL 2001/2001 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 64e8a0e (src/c/rgramc.c only,
  +1055/-914, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7118 lines (7116+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
