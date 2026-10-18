# REAUDIT-e02b8fe (viewer4 r4): band178 T10P131 (n<=62416, 828 tiers) — PASS

Interim turf-starved re-confirm of r1 VERIFY (GATE+VERIFY
on file). First-hand in fresh WS detached tree
WS/tmp/encode-viewer4/reaudit-e02b8fe/tree (detached HEAD
e02b8fe, clean), seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0 0 warnings, 1878456
bytes; PINS 7930 + 1 header).

- PYID (RGRAMC=own C, corpus seeded own-seat r1 cache):
  RGRAMC-PYID 3965/3965 covered=3965/3965, RGRAMC-GREEN,
  rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own C, fresh oracle): 7930 PASS / 0 FAIL,
  RGRAM-GREEN, rc=0, tail g-z62416.
- PYBAT (python impl, same suite, fresh oracle): 7930 PASS /
  0 FAIL, RGRAM-GREEN, rc=0, tail g-z62416.
- PINS-RGRAM set-eq 7930/7930 (csv g-z rows 7930, both
  legs all-PASS).
- Own-loop fresh-oracle 62325..62416: pass=92 fail=0
  pins=15 pinfail=0, OWN-GREEN, rc=0.
- Tables-EQ own script (tables-eq-r4.py): NEW 8/8 EQ
  (_T10P131AC/BC/QC/AM/BM/M/QR/QT); FULL 1978/1978
  0-skip (2 script artifacts found+fixed first-hand:
  py string-concat, tuple-of-pairs flatten).
- Wall-grep PARENT-032 scope on band diff vs 76233c8
  (src/c/rgramc.c only, +1483/-1020,
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit OBSERVED (none in
  lane diff).

VERDICT: PASS (re-confirm; r1 VERIFY stands).
