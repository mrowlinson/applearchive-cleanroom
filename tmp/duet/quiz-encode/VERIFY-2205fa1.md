# VERIFY-2205fa1 (viewer3 r1): band173 T10R126 — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer3/2205fa1/tree
(detached HEAD 2205fa1 confirmed),
seat-private build build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1844360 bytes).

- PYID (RGRAMC=own C): 3902/3902
  covered=3902/3902, RGRAMC-GREEN, rc=0,
  0 FAIL lines.
- CBAT (RGRAM_BIN=own C): 7804 PASS /
  0 FAIL, RGRAM-GREEN, rc=0.
- PYBAT (python impl, same suite):
  7804 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0.
- PINS-RGRAM set-eq 7804/7804 (csv
  g-z rows 7804, both legs all-PASS).
- Own-loop fresh-oracle 61373..61628:
  pass=256 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only,
  cpat|libcompression|depload): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED.

GATE-2205fa1 PASS-functional stands
confirmed. VERDICT: PASS.
