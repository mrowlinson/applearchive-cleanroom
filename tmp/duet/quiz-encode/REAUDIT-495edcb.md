# REAUDIT-495edcb (viewer4 r5): band181 T10R130 (n<=63020, 834 tiers) — PASS

Interim turf-starved re-confirm (GATE+VERIFY on file).
First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-495edcb/tree (detached HEAD
495edcb, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1895400
bytes; PINS 8004 + 2 header).

- PYID (RGRAMC=own C, corpus seeded own-seat b184
  cache 8076 files, 0 regen): RGRAMC-PYID 4002/4002
  covered=4002/4002, RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 8004 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z63020.
- PYBAT (python impl, same suite, fresh oracle): 8004
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail g-z63020.
- PINS-RGRAM set-eq 8004/8004 (csv g-z rows 8004,
  both legs all-PASS, tails x2/leg).
- Own-loop fresh-oracle 62765..63020: pass=256 fail=0
  pins=12 pinfail=0, OWN-GREEN, rc=0.
- Tables-EQ own script v3: NEW 2/2 EQ
  (_T10R130C/_T10R130M; diff adds exactly 2 tables +
  1 _N scalar, grep-verified); FULL 2237/2237 0-skip.
- Wall-grep PARENT-032 scope on band diff vs aef8ee6
  (src/c/rgramc.c only, +1174/-1033,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; VERIFY stands).
