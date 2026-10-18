# GATE-b6151b1 — band84 C-port T10R72+T10P74 — PASS-functional

- Tree: lane-diff vs de31018: src/c/rgramc.c + rgram.py +214 (w2 merge of
  R72+P74 tiers) + test-list ext (42169..42516) + pins +46. Tables 11/11
  tier-EQ vs py (R72: AM16,AQ4,BM16,AC63,BC65; P74: S0,S1,AM16,BM10,
  AC70,BC67). Wall-grep lane-diff 0.
- Gate battery first-hand: C-BUILD PASS w0; RGRAM py 5092/0 GREEN;
  PINS-RGRAM set-eq 5092/5092; all other functional legs PASS.
- C-side first-hand: full C battery 5092/0; parity 2546/2546 PYID
  covered GREEN; storm.sh 12/12 py=C (10 new-tier boundaries R72A/B +
  P74S0/S1/A/B, 2 out-of-scope rc=2 identical).
- HYGIENE/CONTAM/LIBCOMPRESSION FAILs scoped: same 10-file pre-tip tree
  set as band83 (README/docs/notes/proto DPROBE/spec), none in
  lane-diff -> OBSERVED-inherited per PARENT-032.
- Verdict: PASS-functional. No RED, no FLAG.
