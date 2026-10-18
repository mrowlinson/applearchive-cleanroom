# VERIFY-e02b8fe (viewer4 r2): band178 T10P131 (n<=62416, 828 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer4/e02b8fe/tree
(detached HEAD e02b8fe), seat-private
build .../e02b8fe/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1878456 bytes; PINS 7930 + 2 header).

- PYID (RGRAMC=own C): RGRAMC-PYID
  3965/3965 covered=3965/3965,
  RGRAMC-GREEN, rc=0.
- CBAT (RGRAM_BIN=own C): 7930 PASS /
  0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z62416.
- PYBAT (python impl, same suite):
  7930 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z62416.
- Own-loop fresh-oracle 62161..62416:
  pass=256 fail=0 pins=21 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only, +1483/-1020;
  cpat|libcompression|depload): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

VERDICT: PASS.
