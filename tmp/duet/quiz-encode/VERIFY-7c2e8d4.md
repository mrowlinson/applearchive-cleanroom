# VERIFY-7c2e8d4 (viewer3 r6): band185 T10R132 (n<=63716, 842 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer3/7c2e8d4/tree
(detached HEAD 7c2e8d4 confirmed
clean), seat-private build
build/rgramc-r6 (cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings, 1912632
bytes; PINS 8100 + header).

- PYID (RGRAMC=own r6, corpus own-seat
  3938 seeded + 112 fresh-oracle regen
  for new N, all compares first-hand):
  RGRAMC-PYID 4050/4050 covered=
  4050/4050, RGRAMC-GREEN, rc=0,
  0 FAIL lines.
- CBAT (RGRAM_BIN=own r6, fresh oracle):
  8100 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z63716.
- PYBAT (python impl, same suite, fresh
  oracle): 8100 PASS / 0 FAIL,
  RGRAM-GREEN, rc=0, tail g-z63716.
- PINS-RGRAM set-eq 8100/8100 (csv
  g-z rows 8100, both legs all-PASS).
- Own-loop fresh-oracle 63461..63716:
  pass=256 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script v3: NEW 2/2 EQ
  (_T10R132C,_T10R132M); FULL
  2263/2263 0-skip 0-mismatch.
  Consistent with GATE's 3-item split
  (C + C_N derived + M str).
- Wall-grep PARENT-032 scope on band
  diff vs 7c2e8d4^ (src/c/rgramc.c
  only, +1188/-1047,
  cpat|libcompression|depload|dlopen|
  dylib|CPAT): 0 hits.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).
- GATE-7c2e8d4 PASS-functional on file
  (sweep r10) BEFORE this filing —
  oldest-gated-first obeyed.

VERDICT: PASS.
