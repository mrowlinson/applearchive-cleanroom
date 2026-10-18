# VERIFY-e1a5f7c (viewer r7): band163 — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/e1a5f7c/tree
(detached HEAD e1a5f7c), seat-private
build work7r1/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings).

- CBAT (RGRAM_BIN=own C): 7562 PASS /
  0 FAIL, RGRAM-GREEN, rc=0.
- PYID (RGRAMC=own C): 3781/3781
  covered, RGRAMC-GREEN, rc=0.
- Own-loop fresh-oracle 59633..59888:
  pass=256 fail=0 pins=26 pinfail=0,
  OWN-GREEN, rc=0.
- PYBAT (python impl, same suite):
  7562 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0.
- Wall-grep PARENT-032 scope on band
  diff (cpat|libcompression|depload):
  0. HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED.

GATE-e1a5f7c PASS-functional stands
confirmed. VERDICT: PASS.
