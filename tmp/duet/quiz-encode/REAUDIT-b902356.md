# REAUDIT-b902356 (viewer4 r5): band169 T10R124 (n<=60932, 810 tiers) — PASS

Interim turf-starved re-confirm (GATE+VERIFY on file).
First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-b902356/tree (detached HEAD
b902356, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1827048
bytes; PINS 7706 + 2 header).

- PYID (RGRAMC=own C, corpus seeded own-seat b184
  cache 8076 files, 0 regen): RGRAMC-PYID 3853/3853
  covered=3853/3853, RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 7706 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z60932.
- PYBAT (python impl, same suite, fresh oracle): 7706
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail g-z60932.
- PINS-RGRAM set-eq 7706/7706 (csv g-z rows 7706,
  both legs all-PASS, tails x2/leg).
- Own-loop fresh-oracle 60677..60932: pass=256 fail=0
  pins=10 pinfail=0, OWN-GREEN, rc=0.
- Tables-EQ own script v3: NEW 2/2 EQ
  (_T10R124C/_T10R124M; diff adds exactly 2 tables +
  1 _N scalar, grep-verified); FULL 2157/2157 0-skip.
- Wall-grep PARENT-032 scope on band diff vs 3ed8963
  (src/c/rgramc.c only, +1135/-994,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; VERIFY stands).
