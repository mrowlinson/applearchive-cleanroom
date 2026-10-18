# REAUDIT-ab7eb30 (viewer4 r10): band135 T10R107 (n<=55016) — PASS

First-hand in fresh WS detached tree
.../reaudit-ab7eb30/tree (git archive
ab7eb30, full SHA ab7eb300478dbddc39e
bb52c89f907ecc7ce30f3), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1639272 bytes). Merged 986b3cc.
CLAIM-viewer4-ab7eb30-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3436
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3436/3436 covered=3436/3436,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 6872 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z55016.
- PYBAT (python impl): 6872 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z55016.
- PINS-RGRAM set-eq 6872/6872 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 54761..55016:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R107C/_T10R107M);
  FULL 1937/1937 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 90ae088 (src/c/rgramc.c only,
  +1024/-883, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 6874 lines (6872+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
