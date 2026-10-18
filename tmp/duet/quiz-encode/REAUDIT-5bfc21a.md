# REAUDIT-5bfc21a (viewer4 r7): band187 T10R133 (n<=64064, 846 tiers) — PASS

Interim turf-starved re-confirm (GATE+VERIFY on file).
First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-5bfc21a/tree (detached HEAD
5bfc21a, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1929512
bytes; PINS 8152 + 2 header).

- PYID (RGRAMC=own C, corpus seeded own-seat b183
  cache 8076 hardlinks + 38 new-N fresh-oracle regen,
  now 8152 files): RGRAMC-PYID 4076/4076
  covered=4076/4076, RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 8152 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z64064.
- PYBAT (python impl, same suite, fresh oracle): 8152
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail g-z64064.
- PINS-RGRAM set-eq 8152/8152 (csv g-z rows 8152,
  C/PY PASS-name sets cmp-equal, both all-PASS).
- Own-loop fresh-oracle 63809..64064: pass=256 fail=0
  pins=12 pinfail=0, OWN-GREEN, rc=0.
- Tables-EQ own script r4: NEW 2/2 EQ
  (_T10R133C/_T10R133M); FULL 2276/2276 0-skip.
- Wall-grep PARENT-032 scope on band diff vs 786f2a7
  (src/c/rgramc.c only, +1195/-1054,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; VERIFY stands).
