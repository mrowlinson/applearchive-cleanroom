# VERIFY-ae7c8dd (viewer4 r1): band172 T10P128 (n<=61372, 816 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer4/ae7c8dd/tree
(detached HEAD ae7c8dd), seat-private
build .../ae7c8dd/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1844280 bytes; PINS 7780 + 2 header).

- PYID (RGRAMC=own C): RGRAMC-PYID
  3890/3890 covered=3890/3890,
  RGRAMC-GREEN, rc=0.
- CBAT (RGRAM_BIN=own C): 7780 PASS /
  0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z61372.
- PYBAT (python impl, same suite):
  7780 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z61372.
- Own-loop fresh-oracle 61117..61372:
  pass=256 fail=0 pins=20 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only, +1481/-1001;
  cpat|libcompression|depload): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

VERDICT: PASS.
