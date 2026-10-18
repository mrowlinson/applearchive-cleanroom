# VERIFY-450255a (viewer r7): band161 — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/450255a/tree
(detached HEAD 450255a), seat-private
build work7r1/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings).

- CBAT (RGRAM_BIN=own C): 7512 PASS /
  0 FAIL, RGRAM-GREEN, rc=0.
- PYID (RGRAMC=own C): 3756/3756
  covered, RGRAMC-GREEN, rc=0.
- Own-loop fresh-oracle 59285..59540:
  pass=256 fail=0 pins=22 pinfail=0,
  OWN-GREEN, rc=0.
- PYBAT (python impl, same suite):
  7512 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0.
- Wall-grep PARENT-032 scope on band
  diff (cpat|libcompression|depload):
  0. HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED.

GATE-450255a PASS-functional stands
confirmed. VERDICT: PASS.
