# GATE-6436cf2 — band102 C-port T10P91+T10R90 — PASS-functional

- Tree: lane-diff vs 76fbe66 merge: src/c/rgramc.c only
  (+1329/-767). py + PINS + test byte-identical. Tables
  4/4 EQ vs py (P91: AC,BC,QC; R90: C). Wall-grep
  lane-diff 0.
- Gate battery first-hand: RGRAM py 5930/0 GREEN;
  PINS-RGRAM set-eq 5930/5930; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2965/2965 GREEN; full C battery 5930/0 GREEN (rc=0);
  own-loop fresh-oracle 48405..48752: 348/0, pins 60/60.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band98).
- Verdict: PASS-functional. No RED, no FLAG.
