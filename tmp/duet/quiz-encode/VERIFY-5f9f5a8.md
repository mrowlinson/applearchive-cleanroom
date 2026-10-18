# VERIFY-5f9f5a8 (viewer4 r1): band175 T10R127 (n<=61976, 822 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer4/5f9f5a8/tree
(detached HEAD 5f9f5a8), seat-private
build .../5f9f5a8/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1861240 bytes; PINS 7852 + 2 header).

- PYID (RGRAMC=own C): RGRAMC-PYID
  3926/3926 covered=3926/3926,
  RGRAMC-GREEN, rc=0.
- CBAT (RGRAM_BIN=own C): 7852 PASS /
  0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z61976.
- PYBAT (python impl, same suite):
  7852 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z61976.
- Own-loop fresh-oracle 61721..61976:
  pass=256 fail=0 pins=11 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff (src/c/rgramc.c only, +1154/-1013;
  cpat|libcompression|depload): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

VERDICT: PASS.
