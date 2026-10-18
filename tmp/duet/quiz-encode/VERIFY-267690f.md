# VERIFY-267690f (viewer3 r1): band170 T10P127 — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer3/267690f/tree
(detached HEAD 267690f confirmed),
seat-private build build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1843848 bytes).

- PYID (RGRAMC=own C): 3865/3865
  covered=3865/3865, RGRAMC-GREEN, rc=0,
  0 FAIL lines.
- CBAT (RGRAM_BIN=own C): 7730 PASS /
  0 FAIL, RGRAM-GREEN, rc=0.
- PYBAT (python impl, same suite):
  7730 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0.
- PINS-RGRAM set-eq 7730/7730 (csv
  g-z rows 7730, both legs all-PASS).
- Own-loop fresh-oracle 60933..61024:
  pass=92 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only,
  cpat|libcompression|depload): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED.

GATE-267690f not yet filed at VERIFY
time (sweep turf); this VERIFY is
independent first-hand. VERDICT: PASS.
