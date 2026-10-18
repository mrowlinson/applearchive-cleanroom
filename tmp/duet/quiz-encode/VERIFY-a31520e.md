# VERIFY-a31520e (viewer4 r4): band184 T10P134 (n<=63460, 840 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer4/a31520e/tree
(detached HEAD a31520e, clean),
seat-private build .../build/rgramc
(cc -O2 -Wall -Wextra -std=c11 rc=0
0 warnings, 1912584 bytes; PINS 8076
+ 1 header).

- PYID (RGRAMC=own C, corpus seeded
  own-seat cache + fresh oracle regen
  for new N): RGRAMC-PYID 4038/4038
  covered=4038/4038, RGRAMC-GREEN, rc=0.
- CBAT (RGRAM_BIN=own C, fresh oracle):
  8076 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z63460.
- PYBAT (python impl, same suite, fresh
  oracle): 8076 PASS / 0 FAIL,
  RGRAM-GREEN, rc=0, tail g-z63460.
- PINS-RGRAM set-eq 8076/8076 (csv g-z
  rows 8076, both legs all-PASS).
- Own-loop fresh-oracle 63369..63460:
  pass=92 fail=0 pins=14 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script v3: NEW 12/12 EQ
  (AC/BC/QC + AM/BM/M/QR/QT + S0/S1/S2/
  S3; _N 76/72/62 consistent); FULL
  2261/2261 0-skip. Consistent with
  GATE's 3-numeric + 9-string split.
- Wall-grep PARENT-032 scope on band
  diff vs 079bb6e (src/c/rgramc.c only,
  +1517/-1040,
  cpat|libcompression|depload|dlopen|
  dylib|CPAT): 0 hits. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).
- GATE-a31520e PASS-functional on file
  (sweep2 r13) BEFORE this filing —
  oldest-gated-first obeyed.

VERDICT: PASS.
