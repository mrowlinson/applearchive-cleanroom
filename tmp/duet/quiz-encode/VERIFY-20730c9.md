# VERIFY-20730c9 (viewer3 r3): band179 T10R129 (n<=62672, 830 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer3/20730c9/tree
(detached HEAD 20730c9 confirmed
clean), seat-private build
build/rgramc (cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings, 1878536
bytes).

- PYID (RGRAMC=own C): RGRAMC-PYID
  3977/3977 covered=3977/3977,
  RGRAMC-GREEN, rc=0, 0 FAIL lines.
- CBAT (RGRAM_BIN=own C): 7954 PASS /
  0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z62672.
- PYBAT (python impl, same suite):
  7954 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z62672.
- PINS-RGRAM set-eq 7954/7954 (csv
  g-z rows 7954, both legs all-PASS).
- Own-loop fresh-oracle 62417..62672:
  pass=256 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0.
- Wall-grep PARENT-032 scope on band
  diff vs bdee89b (src/c/rgramc.c
  only, +1187/-1026,
  cpat|libcompression|depload): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

GATE-20730c9 PASS-functional stands
confirmed. VERDICT: PASS.
