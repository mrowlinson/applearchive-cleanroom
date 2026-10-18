# GATE-0e64e61 — band97 C-port T10P86+T10R85 — PASS-functional

- Tree: lane-diff vs fa89957 merge: src/c/rgramc.c only
  (+1298/-736). py + PINS + test byte-identical. Tables
  11/11 EQ vs py (P86: S0,S1,AM16,AC73,BM10,BC68; R85:
  AM16,AQ4,AC63,BM16,BC65). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 5670/0 GREEN;
  PINS-RGRAM set-eq 5670/5670; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2835/2835 GREEN; full C battery 5670/0 GREEN (rc=0);
  own-loop fresh-oracle 46665..47012: 348/0, pins 46/46.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band96).
- Verdict: PASS-functional. No RED, no FLAG.
