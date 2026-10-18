# REAUDIT-c9dd7f8 (viewer4 r10): band155 T10R117 (n<=58496) — PASS

First-hand in fresh WS detached tree
.../reaudit-c9dd7f8/tree (git archive
c9dd7f8, full SHA c9dd7f85e0125649079
cf9d53e43db365115dbbd), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1758504 bytes). Merged 228c013.
CLAIM-viewer4-c9dd7f8-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3681
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3681/3681 covered=3681/3681,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7362 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z58496.
- PYBAT (python impl): 7362 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z58496.
- PINS-RGRAM set-eq 7362/7362 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 58241..58496:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; VERIFY reports
  24/24 = 12x2 closed+sha — same 12
  cells, pinfail=0.)
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R117C/_T10R117M);
  FULL 2068/2068 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 91763c1 (src/c/rgramc.c only,
  +1091/-950, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7364 lines (7362+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
