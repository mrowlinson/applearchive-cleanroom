# GATE-ee6b913 — band107 C-port T10R92 — PASS-functional

- Tree: lane-diff vs 8a131dc merge: src/c/rgramc.c only
  (+934/-793). py + PINS + test byte-identical. Tables
  1/1 EQ vs py (R92: C). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6112/0 GREEN;
  PINS-RGRAM set-eq 6112/6112; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3056/3056 GREEN; full C battery 6112/0 GREEN (rc=0);
  own-loop fresh-oracle 49541..49796: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band102).
- Verdict: PASS-functional. No RED, no FLAG.
