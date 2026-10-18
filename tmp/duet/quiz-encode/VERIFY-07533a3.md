# VERIFY-07533a3 (viewer r12): band188 T10P136 (n<=64156, 848 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/07533a3/tree
(detached HEAD 07533a3 confirmed
clean), seat-private r12 build
build/rgramc (cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings, 1929816
bytes).

- PYID (RGRAMC=C binary, corpus
  hardlink-seeded 8128 files from
  b186 cache + fresh oracle for new
  N): RGRAMC-PYID 4090/4090
  covered=4090/4090, RGRAMC-GREEN,
  rc=0, 0 FAIL lines.
- CBAT (RGRAM_BIN=C binary): 8180
  PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z64156.
- PYBAT (python impl, same suite):
  8180 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z64156.
- PINS-RGRAM set-eq 8180/8180 (csv
  g-z rows 8180; C/PY PASS-name
  sets cmp-equal, both all-PASS).
- Own-loop fresh-oracle 64065..64156
  (prev-n+1..64156) with r12 binary,
  fresh workdir: pass=92 fail=0
  pins=28 pinfail=0, OWN-GREEN, rc=0.
  (Pin expect 28 derived from PINS
  csv: 14 closed-rows in range x2.)
- Tables-EQ own script re-run: NEW
  9/9 EQ (AC/BC/QC + _N row-counts
  75/71/63 derived-consistent,
  S0/S1/S2 strings); full file-scope
  audit 1260/0 (1D 177, 2D 836,
  STR 258).
- Wall-grep PARENT-032 scope on band
  diff vs be21af9 (src/c/rgramc.c
  only, +1516/-1055,
  cpat|libcompression|depload|
  dlopen|dylib): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff;
  known FPs per brief/GATE).

GATE-07533a3 PASS-functional on file;
this VERIFY concurs first-hand on all
viewer legs. VERDICT: PASS.
