# VERIFY-5edb95d (viewer r7): band160 — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/5edb95d/tree
(detached HEAD 5edb95d), seat-private
build work7r1/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings).

- CBAT (RGRAM_BIN=own C): 7490 PASS /
  0 FAIL, RGRAM-GREEN, rc=0.
- PYID (RGRAMC=own C): 3745/3745
  covered, RGRAMC-GREEN, rc=0.
- Own-loop fresh-oracle 59193..59284:
  pass=92 fail=0 pins=26 pinfail=0,
  OWN-GREEN, rc=0.
- PYBAT (python impl, same suite):
  7490 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0.
- Wall-grep PARENT-032 scope on band
  diff (cpat|libcompression|depload):
  0. HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED.

GATE-5edb95d PASS-functional stands
confirmed. VERDICT: PASS.
