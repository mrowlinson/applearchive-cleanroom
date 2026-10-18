# NOTE-viewer3-hb-r9-02 (fresh legs green, PYID re-run in flight)

- Tables-EQ FRESH r9: NEW 3/3
  (_T10R135C/M/Q) + FULL 2304/2304 0-skip,
  rc=0 — matches r8 staged.
- Lane diff re-verified: src/c/rgramc.c
  only (+1227/-1068), wall-grep 0
  (PARENT-032 scope). py+PINS+tests
  byte-identical to writer parent 91bdc21;
  PINS 8256 lines = 8254+2 header.
- Spot re-run FRESH-oracle r9 (24 N incl.
  band edges 64505/64760, r9 binary):
  24/24 py-vs-C identical (rc+stdout+
  stderr), pins 18/18, SPOT-GREEN rc=0.
- PYID full fresh re-run (4127, r9 binary,
  seeded corpus) in flight; VERIFY still
  gated on GATE-94a0e0b (sweep-r14). Quiz
  diff 0. No commits, no push.
