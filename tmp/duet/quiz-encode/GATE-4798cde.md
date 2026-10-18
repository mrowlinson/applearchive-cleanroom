# GATE-4798cde — band101 C-port T10P90+T10R89 — PASS-functional

- Tree: lane-diff vs 174f8a4 merge: src/c/rgramc.c only
  (+1365/-760). py + PINS + test byte-identical. Tables
  14/14 EQ vs py (P90: S0,S1,SS,AM16,AC73,BM9,BC68,
  QC60,QM16,QR4,QT4; R89: C64,M16,Q16). Wall-grep
  lane-diff 0.
- Gate battery first-hand: RGRAM py 5870/0 GREEN;
  PINS-RGRAM set-eq 5870/5870; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2935/2935 GREEN; full C battery 5870/0 GREEN (rc=0);
  own-loop fresh-oracle 48057..48404: 348/0, pins 62/62.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band100).
- Verdict: PASS-functional. No RED, no FLAG.
