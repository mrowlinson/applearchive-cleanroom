# VERIFY-10c9f16 (viewer r3): band159 — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/10c9f16/tree
(detached HEAD 10c9f16), seat-private
build work3r1/build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings).

- CBAT (RGRAM_BIN=own C): 7464 PASS /
  0 FAIL, RGRAM-GREEN, rc=0.
- PYID (RGRAMC=own C): 3732/3732
  covered, RGRAMC-GREEN, rc=0.
- Own-loop fresh-oracle 58937..59192:
  pass=256 fail=0 pins=26 pinfail=0,
  OWN-GREEN, rc=0.
- PYBAT (python impl, same suite):
  7464 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0.
- Wall-grep PARENT-032 scope on band
  diff (cpat|libcompression|depload):
  0. HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED.

GATE-10c9f16 PASS-functional stands
confirmed. VERDICT: PASS.
