# GATE-d68dbff — band87 C-port T10P76+T10R75 — PASS-functional

- Tree: lane-diff vs c179b2c merge: C port P76+R75 tiers. Tables 11/11
  EQ vs py (P76: S0,S1,AM16,BM10,AC70,BC68; R75: AM16,AQ4,BM16,AC62,
  BC63). Wall-grep lane-diff 0.
- Gate battery first-hand: C-BUILD PASS w0; RGRAM py 5210/0 GREEN;
  PINS-RGRAM set-eq 5210/5210; all other functional legs PASS.
- C-side first-hand: full C battery 5210/0; parity 2605/2605 PYID
  covered GREEN; storm.sh 10/10 py=C (9 new-tier boundaries P76S0/S1/
  A/B + R75A/B, 1 out-of-scope rc=2 identical).
- HYGIENE/CONTAM/LIBCOMPRESSION FAILs scoped: pre-tip tree files only,
  none in lane-diff -> OBSERVED-inherited per PARENT-032.
- Verdict: PASS-functional. No RED, no FLAG.
