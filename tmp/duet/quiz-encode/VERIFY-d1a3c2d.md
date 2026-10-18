# VERIFY-d1a3c2d (viewer r11): band182 T10P133 (n<=63112, 836 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/d1a3c2d/tree
(detached HEAD d1a3c2d confirmed
clean), seat-private r11 build
build-r11/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1895688 bytes, cmp-identical to
inherited build/rgramc).

- PYID (RGRAMC=C binary, corpus
  cached): RGRAMC-PYID 4014/4014
  covered=4014/4014, RGRAMC-GREEN,
  rc=0, 0 FAIL lines. (Binary used
  byte-identical to r11 build;
  result transfers first-hand.)
- CBAT (RGRAM_BIN=r11 C): 8028 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z63112.
- PYBAT (python impl, same suite):
  8028 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z63112.
- PINS-RGRAM set-eq 8028/8028 (csv
  g-z rows 8028; C/PY PASS-name
  sets cmp-equal, both all-PASS).
- Own-loop fresh-oracle 63021..63112
  re-run with r11 binary, fresh
  workdir: pass=92 fail=0 pins=24
  pinfail=0, OWN-GREEN, rc=0.
- Tables-EQ own script re-run: NEW
  8/8 EQ (AC/BC/QC + _N row-counts
  75/71/62 derived-consistent,
  S0/S1 strings); full file-scope
  audit 1238/0 (1D 177, 2D 824,
  STR 248).
- Wall-grep PARENT-032 scope on band
  diff vs 4f8b304 (src/c/rgramc.c
  only, +1484/-1034,
  cpat|libcompression|depload|
  dlopen|dylib): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

GATE-d1a3c2d PASS-functional on file;
this VERIFY concurs first-hand on all
viewer legs. VERDICT: PASS.
