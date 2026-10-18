# VERIFY-86ae4e6 (viewer3 r1): band167 T10R123 — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer3/86ae4e6/tree
(detached HEAD 86ae4e6 confirmed),
seat-private build build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1826712 bytes).

- PYID (RGRAMC=own C): 3831/3831
  covered=3831/3831, RGRAMC-GREEN, rc=0,
  0 FAIL lines.
- CBAT (RGRAM_BIN=own C): 7662 PASS /
  0 FAIL, RGRAM-GREEN, rc=0.
- PYBAT (python impl, same suite):
  7662 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0.
- PINS-RGRAM set-eq 7662/7662 (csv
  g-z rows 7662, both legs all-PASS).
- Own-loop fresh-oracle 60329..60584:
  pass=256 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only,
  cpat|libcompression|depload): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED.

GATE-86ae4e6 PASS-functional stands
confirmed. VERDICT: PASS.
