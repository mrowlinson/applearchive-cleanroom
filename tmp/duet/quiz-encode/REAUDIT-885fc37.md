# REAUDIT-885fc37 (viewer4 r10): band151 T10R115 (n<=57800) — PASS

First-hand in fresh WS detached tree
.../reaudit-885fc37/tree (git archive
885fc37, full SHA 885fc378f2dc6e1c62b
0058139f34c900ca9b3cb), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1741272 bytes). Merged 3c4652d.
CLAIM-viewer4-885fc37-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3631
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3631/3631 covered=3631/3631,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7262 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z57800.
- PYBAT (python impl): 7262 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z57800.
- PINS-RGRAM set-eq 7262/7262 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 57545..57800:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R115C/_T10R115M);
  FULL 2042/2042 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs a4866a6 (src/c/rgramc.c only,
  +1077/-936, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7264 lines (7262+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
