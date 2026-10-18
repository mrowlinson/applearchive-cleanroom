# VERIFY-e5ed337 (viewer r10): band180 T10P132 (n<=62764, 832 tiers) — PASS

First-hand in WS detached tree
WS/tmp/encode-viewer/e5ed337/tree
(detached HEAD e5ed337 confirmed
clean), seat-private build
build/rgramc (cc -O2 -Wall -Wextra
-std=c11 rc=0 0 warnings, 1895352
bytes).

- PYID (RGRAMC=own C): RGRAMC-PYID
  3990/3990 covered=3990/3990,
  RGRAMC-GREEN, rc=0, 0 FAIL lines.
- CBAT (RGRAM_BIN=own C): 7980 PASS /
  0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z62764.
- PYBAT (python impl, same suite):
  7980 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0, tail g-z62764.
- PINS-RGRAM set-eq 7980/7980 (csv
  g-z rows 7980, both legs all-PASS).
- Own-loop fresh-oracle 62673..62764:
  pass=92 fail=0 pins=26 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script: NEW 9/9 EQ
  (AC/BC/QC + _N row-counts 76/73/65
  derived-consistent C rows, S0/S1/S2
  strings); full file-scope audit
  1232/0 (1D 166 + 11 C-only _KEYS
  skipped dicts-scope, 2D 820,
  STR 246). CORR 00:15: BC_N 70->73
  (first-hand re-audit; verdict
  unaffected).
- Wall-grep PARENT-032 scope on band
  diff vs 279af2a (src/c/rgramc.c
  only, +1490/-1027,
  cpat|libcompression|depload): 0.
  HYGIENE/CONTAM/LIBCOMPRESSION
  inherit OBSERVED (none in lane diff).

GATE-e5ed337 not yet filed (sweep2
r12-DUPLEX live); this VERIFY stands
first-hand GATE-independent per
PARENT-068 precedent. VERDICT: PASS.
