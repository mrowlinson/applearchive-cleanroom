# GATE-ead5f7c — band86 C-port T10P75+T10R74 — PASS-functional

- Tree: lane-diff vs cd3037c merge: C port P75+R74 tiers. Tables 11/11
  EQ vs py (P75: S0,S1,AM16,BM10,AC69,BC66; R74: AM16,AQ4,BM16,AC61,
  BC66). Wall-grep lane-diff 0.
- Gate battery first-hand: C-BUILD PASS w0; RGRAM py 5164/0 GREEN;
  PINS-RGRAM set-eq 5164/5164; all other functional legs PASS.
- C-side first-hand: full C battery 5164/0; parity 2582/2582 PYID
  covered GREEN; storm.sh 10/10 py=C (9 new-tier boundaries P75S0/S1/
  A/B + R74A/B, 1 out-of-scope rc=2 identical).
- HYGIENE/CONTAM/LIBCOMPRESSION FAILs scoped: pre-tip tree files only,
  none in lane-diff -> OBSERVED-inherited per PARENT-032.
- Verdict: PASS-functional. No RED, no FLAG.
