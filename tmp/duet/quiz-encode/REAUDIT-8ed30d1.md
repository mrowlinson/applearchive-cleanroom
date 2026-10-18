# REAUDIT-8ed30d1 (viewer4 r10): band157 T10R118 (n<=58844) — PASS

First-hand in fresh WS detached tree
.../reaudit-8ed30d1/tree (git archive
8ed30d1, full SHA 8ed30d1eccf0b46c5c3
1ecd8582b38ca09be368c), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1775464 bytes). Merged 72f8ee5.
CLAIM-viewer4-8ed30d1-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3706
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3706/3706 covered=3706/3706,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7412 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z58844.
- PYBAT (python impl): 7412 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z58844.
- PINS-RGRAM set-eq 7412/7412 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 58589..58844:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 3/3 EQ (_T10R118C/_T10R118M/
  _T10R118QH); FULL 2083/2083 0-skip
  0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs b0e6ca5 (src/c/rgramc.c only,
  +1118/-957, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7414 lines (7412+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
