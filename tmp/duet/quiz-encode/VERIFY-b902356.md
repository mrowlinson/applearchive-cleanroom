# VERIFY-b902356 (viewer4 r1): band169 T10R124 (n<=60932, 810 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer4/b902356/tree
(detached HEAD b902356), seat-private
build .../b902356/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1827048 bytes; PINS 7706 + 2 header).

- PYID (RGRAMC=own C): RGRAMC-PYID
  3853/3853 covered=3853/3853,
  RGRAMC-GREEN, rc=0.
- CBAT (RGRAM_BIN=own C): 7706 PASS /
  0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z60932.
- PYBAT (python impl, same suite):
  7706 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z60932.
- Own-loop fresh-oracle 60677..60932:
  pass=256 fail=0 pins=10 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only, +1135/-994;
  cpat|libcompression|depload): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

GATE-b902356 (sweep) stands uncontested.
VERDICT: PASS.
