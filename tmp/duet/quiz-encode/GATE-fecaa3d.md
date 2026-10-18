# GATE-fecaa3d — band94 C-port T10P83+T10R82 — PASS-functional

- Tree: lane-diff vs 8233b06 merge: src/c/rgramc.c only
  (+1280/-718). py + PINS + test byte-identical. Tables
  11/11 EQ vs py (P83: S0,S1,AM16,AC73,BM10,BC64; R82:
  AM16,AQ4,AC61,BM16,BC64). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 5532/0 GREEN;
  PINS-RGRAM set-eq 5532/5532; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2766/2766 GREEN; full C battery 5532/0 GREEN (rc=0);
  own-loop fresh-oracle 45621..45968: 348/0, pins 46/46.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band93).
- Verdict: PASS-functional. No RED, no FLAG.
