# REAUDIT-7f4db2c-viewer4-r9: band165 T10R122 (n<=60236, 802 tiers) — PASS

Second independent first-hand battery (viewer-r17
filed unsuffixed REAUDIT-7f4db2c PASS on older
claim 17:12:03 vs mine 17:12:24 — this filing
suffixed per PARENT-070 + r8 fac36c9 precedent,
not a contest; their file untouched). First-hand
in fresh WS detached tree .../reaudit-7f4db2c/tree
(git archive 7f4db2c, full SHA 7f4db2c173978f6
42d0bab26e6a0941624d8e834 == VERIFY == r17),
seat-private build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings, 1809880 bytes
== VERIFY == GATE == r17).

- PYID (RGRAMC=own r9, corpus 4101 own-seat
  hardlinks ex r8 b189 cache, all 3807 N
  covered by seed, py+C freshly executed
  per pin): RGRAMC-PYID 3807/3807
  covered=3807/3807, RGRAMC-GREEN, rc=0,
  0 FAIL. (First attempt RED was seat
  method error — RGRAMC unset, script
  fell back to shared Oct-12 binary;
  see hb-r9-04. Inputs verified correct:
  seeded == fresh-oracle == PINS sha.
  Only the own-binary run is cited.)
- CBAT (RGRAM_BIN=own r9): 7614 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail g-z60236.
- PYBAT (python impl): 7614 PASS / 0 FAIL,
  RGRAM-GREEN, rc=0, tail g-z60236.
- PINS-RGRAM set-eq 7614/7614 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 59981..60236:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; VERIFY/r17
  report 24/24 = 12x2 closed+sha —
  same 12 cells, pinfail=0.)
- Tables-EQ own script r9 (r8 recipe):
  NEW 2/2 EQ (_T10R122C/_T10R122M);
  FULL 2133/2133 0-skip 0-mismatch.
  (Script-scope note: r9 enumerates
  STRARR tables where r17 counts NEW
  3/3 / FULL 2144; both 0-mismatch,
  conventions differ only.)
- Wall-grep PARENT-032 scope on band diff
  vs 399f71d (src/c/rgramc.c only,
  +1123/-982 == VERIFY == r17,
  cpat|libcompression|depload|dlopen|
  dylib): 0 hits. py+PINS+tests
  cmp-SAME 399f71d; PINS 7616 lines
  (7614+2hdr). HYGIENE/CONTAM inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands;
agrees with viewer-r17 on every leg modulo
table/pin-count conventions). No commits,
no push.
