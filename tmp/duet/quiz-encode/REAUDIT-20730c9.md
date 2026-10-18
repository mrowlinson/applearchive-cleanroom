# REAUDIT-20730c9 (viewer4 r6): band179 T10R129 (n<=62672, 830 tiers) — PASS

Interim turf-starved re-confirm (GATE+VERIFY on file).
First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-20730c9/tree (detached HEAD
20730c9, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1878536
bytes; PINS 7954 + 2 header).

- PYID (RGRAMC=own C, corpus seeded own-seat b184
  cache 8076 files, 0 regen): RGRAMC-PYID 3977/3977
  covered=3977/3977, RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 7954 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z62672.
- PYBAT (python impl, same suite, fresh oracle): 7954
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail g-z62672.
- PINS-RGRAM set-eq 7954/7954 (csv g-z rows 7954,
  both legs all-PASS, tails x2/leg).
- Own-loop fresh-oracle 62417..62672: pass=256 fail=0
  pins=12 pinfail=0, OWN-GREEN, rc=0.
- Tables-EQ own script r4: NEW 3/3 EQ
  (_T10R129C/_T10R129M/_T10R129QH); FULL 2224/2224 0-skip.
- Wall-grep PARENT-032 scope on band diff vs bdee89b
  (src/c/rgramc.c only, +1187/-1026,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; VERIFY stands).
