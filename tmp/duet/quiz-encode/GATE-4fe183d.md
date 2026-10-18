# GATE-4fe183d — band95 C-port T10P84+T10R83 — PASS-functional

- Tree: lane-diff vs 234bf1b merge: src/c/rgramc.c only
  (+1287/-724). py + PINS + test byte-identical. Tables
  11/11 EQ vs py (P84: S0,S1,AM16,AC73,BM10,BC69; R83:
  AM16,AQ4,AC64,BM16,BC66). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 5578/0 GREEN;
  PINS-RGRAM set-eq 5578/5578; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2789/2789 GREEN; full C battery 5578/0 GREEN (rc=0);
  own-loop fresh-oracle 45969..46316: 348/0, pins 46/46.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band94).
- Verdict: PASS-functional. No RED, no FLAG.
