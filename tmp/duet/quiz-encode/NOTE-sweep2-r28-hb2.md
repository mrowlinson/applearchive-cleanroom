# NOTE-sweep2-r28-hb2
- b220 battery grinding (gate-tip
  RGRAM stage, ~1488+ PASS so far).
- b220 first-hand DONE early: tables
  3/3 EQ (_T10P152AC 75, BC 71,
  QC 63 rows, PAIRW=2 convention
  verified vs b218); fullaudit
  ALL-EQ (1D 167/0, 2D 900/0,
  dicts 11/0, STR 302/0, STRARR
  1140/0, SKIP 4 py-only same).
- b222 pre-verified (claim later):
  range 69981..70072 = b221 ceil
  69980+1, matches writer 8567b02;
  lane-diff vs 1f76333 rgramc.c
  only +1631/-1170 wall 0; tables
  3/3 EQ (74/69/64); fullaudit
  ALL-EQ (2D 904/0, STR 305/0,
  STRARR 1147/0, SKIP same 4).
- Quiz: no Q for sweep2. Turf clean.
- Next: b220 gate-tip/PYID/C-batt/
  own-loop, GATE #1, then b222.
