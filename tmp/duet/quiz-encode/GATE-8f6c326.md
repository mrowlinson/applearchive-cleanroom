# GATE-8f6c326 — band105 C-port T10R91 — PASS-functional

- Tree: lane-diff vs 79abb83 merge: src/c/rgramc.c only
  (+922/-785). py + PINS + test byte-identical. Tables
  1/1 EQ vs py (R91: C). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6058/0 GREEN;
  PINS-RGRAM set-eq 6058/6058; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3029/3029 GREEN; full C battery 6058/0 GREEN (rc=0);
  own-loop fresh-oracle 49193..49448: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band102).
- Verdict: PASS-functional. No RED, no FLAG.
