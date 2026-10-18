# GATE-e25ae48 — band100 C-port T10P89+T10R88 — PASS-functional

- Tree: lane-diff vs 2d41980 merge: src/c/rgramc.c only
  (+1316/-754). py + PINS + test byte-identical. Tables
  11/11 EQ vs py (P89: S0,S1,AM16,AC71,BM10,BC69; R88:
  AM16,AQ4,AC60,BM16,BC63). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 5808/0 GREEN;
  PINS-RGRAM set-eq 5808/5808; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2904/2904 GREEN; full C battery 5808/0 GREEN (rc=0);
  own-loop fresh-oracle 47709..48056: 348/0, pins 46/46.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band99).
- Verdict: PASS-functional. No RED, no FLAG.
