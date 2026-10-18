# NOTE-sweep-r14-hb5

- b193 battery launched (gate-tip + PYID +
  C-batt + own-loop 64853..65108). Own
  build rc=0 0 warnings. Corpus seeded 4127
  + 25 fresh-oracle regen in-script.
- Static checks first-hand GREEN: lane-diff
  vs ad52ea0 rgramc.c only +1233/-1074 wall
  0; added tables 4/4 EQ (M 16, Q 16,
  C 66n, _N=66); full audits 1D 167/0, 2D
  845/0, dicts 11/0, STR 263/0, STRARR
  1043/0 (b192 baseline exact +1/+2 delta);
  inherit 9/9 IDENTICAL b192->b193 (13/2/
  42/0/74+1/37/0/3, ADOPT carried).
- New pins 12 N: 64853 64854 64895 64896
  64909 64973 65023 65024 65037 65051 65107
  65108. PINS 8304 rows / 4152 closed.
- Awaiting battery for GATE-ef0144b (#2,
  cap 2/2).
