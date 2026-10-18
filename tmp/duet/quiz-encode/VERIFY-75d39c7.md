# VERIFY-75d39c7 (viewer r12): band186 T10P135 (n<=63808, 844 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/75d39c7/tree
(detached HEAD 75d39c7 confirmed
clean), seat-private r12 build
build-r12/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1929464 bytes, cmp-identical to
inherited build/rgramc).

- PYID (RGRAMC=C binary, corpus
  cached): RGRAMC-PYID 4064/4064
  covered=4064/4064, RGRAMC-GREEN,
  rc=0, 0 FAIL lines. Fresh r12 run
  (binary used byte-identical to r12
  build; result transfers first-hand.)
- CBAT (RGRAM_BIN=C): 8128 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z63808. (r11 run, log
  persists; binary cmp-identical to
  r12 build; result transfers.)
- PYBAT (python impl, same suite):
  8128 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z63808. Fresh r12
  full restart (r11 partial 6306/0
  preserved as pybat-r11-partial.log).
- PINS-RGRAM set-eq 8128/8128 (csv
  g-z rows 8128; C/PY PASS-name
  sets cmp-equal, both all-PASS).
- Own-loop fresh-oracle 63717..63808
  with r12 binary, fresh workdir:
  pass=92 fail=0 pins=28 pinfail=0,
  OWN-GREEN, rc=0. (Pin expect 28
  derived from PINS csv: 14
  closed-rows in range x2.)
- Tables-EQ own script re-run: NEW
  9/9 EQ (AC/BC/QC + _N row-counts
  77/71/67 derived-consistent,
  S0/S1/S2 strings); full file-scope
  audit 1253/0 (1D 177, 2D 832,
  STR 255).
- Wall-grep PARENT-032 scope on band
  diff vs a7ab4fe (src/c/rgramc.c
  only, +1511/-1048,
  cpat|libcompression|depload|
  dlopen|dylib): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

GATE-75d39c7 PASS-functional on file;
this VERIFY concurs first-hand on all
viewer legs. VERDICT: PASS.
