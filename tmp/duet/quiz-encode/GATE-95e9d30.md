# GATE-95e9d30 — band85 C-port T10R73 — PASS-functional

- Tree: lane-diff vs b8b1278 merge: C port R73 tiers. Tables 5/5 EQ vs
  py (AM16,AQ4,BM16,AC63,BC66). Wall-grep lane-diff 0.
- Gate battery first-hand: C-BUILD PASS w0; RGRAM py 5118/0 GREEN;
  PINS-RGRAM set-eq 5118/5118; all other functional legs PASS.
- C-side first-hand: full C battery 5118/0; parity 2559/2559 PYID
  covered GREEN; storm.sh 8/8 py=C (5 R73A/B boundaries, P74B
  neighbor, 2 out-of-scope rc=2 identical).
- HYGIENE/CONTAM/LIBCOMPRESSION FAILs scoped: pre-tip tree files only,
  none in lane-diff -> OBSERVED-inherited per PARENT-032.
- Verdict: PASS-functional. No RED, no FLAG.
