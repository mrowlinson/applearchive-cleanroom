# NOTE-sweep2-r15-parked (b188 CLAIMED + interim GREEN; gate -> refill)

- b188 07533a3 CUT during run (T10P136
  n<=64156, 848 tiers). CLAIMED:
  CLAIM-sweep2-07533a3.md (even turf, no
  sweep conflict). r15 call-budget
  exhausted -> FULL first-hand gate goes to
  refill (overwrite claim, file
  GATE-07533a3.md; 0/2 bands gated this
  run).
- r15 b188 interim audits (first-hand, WS
  r15-interim/): seat build rc=0 0-warn
  (1929816 B); own-loop 64065..64156 92/0
  pins 28/28; tables-new 3/3 EQ
  (AC/BC/QC); wall-grep lane-diff 0 hits
  (diff = rgramc.c only +1516/-1055).
  Zero discrepancies.
- REFILL GATE RECIPE (WS
  tmp/encode-sweep2/r15b-<sha>/ or own):
  gate-tip.sh 07533a3 OUT (RGRAM py
  8180/8180 + PINS set-eq + legs); make
  BUILDDIR ownbuild (0-warn); test_rgram_c
  PYID expect 4090/4090 (seed pyid corpus
  hardlink); test_rgram RGRAM_BIN=C expect
  8180/0; own-loop.py 64065 64156;
  tables-new-eq.py + full audit-tables/
  strings/dicts + _N counts; wall-grep
  PARENT-032 (FPs: test_rb2 ctypes, libc,
  ZBM_DYLIB); scoped-legs inherit-compare
  vs b186 (HYG 13/CONTAM 43/LIBC 4).
- RUN SUMMARY: interim 8176 N green
  (39037..39732 b72-b74 + 40081..46664
  b76-b96 + 47013..51628 b98-b116 +
  51885..54064 b118-b130 + 54321..54760
  b132-b134 + 55017..56848 b136-b146 +
  64065..64156 b188), pins 1352/1352,
  24 builds 0-warn. Evidence floor b148
  -> b72. No commits. No QUESTION
  outstanding.
