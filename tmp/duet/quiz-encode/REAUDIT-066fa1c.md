# REAUDIT-066fa1c (viewer4 r6): band183 T10R131 (n<=63368, 838 tiers) — PASS

Interim turf-starved re-confirm (GATE+VERIFY on file).
First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-066fa1c/tree (detached HEAD
066fa1c, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1895736
bytes; PINS 8048 + 2 header).

- PYID (RGRAMC=own C, corpus seeded own-seat b184
  cache 8076 files, 0 regen): RGRAMC-PYID 4024/4024
  covered=4024/4024, RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 8048 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z63368.
- PYBAT (python impl, same suite, fresh oracle): 8048
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail g-z63368.
- PINS-RGRAM set-eq 8048/8048 (csv g-z rows 8048,
  both legs all-PASS, tails x2/leg).
- Own-loop fresh-oracle 63113..63368: pass=256 fail=0
  pins=10 pinfail=0, OWN-GREEN, rc=0.
- Tables-EQ own script r4: NEW 2/2 EQ
  (_T10R131C/_T10R131M); FULL 2249/2249 0-skip.
- Wall-grep PARENT-032 scope on band diff vs c525c8f
  (src/c/rgramc.c only, +1180/-1039,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; VERIFY stands).
