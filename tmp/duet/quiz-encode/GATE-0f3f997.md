# GATE-0f3f997 — band96 C-port T10P85+T10R84 — PASS-functional

- Tree: lane-diff vs f66b1b7 merge: src/c/rgramc.c only
  (+1321/-730). py + PINS + test byte-identical. Tables
  13/13 EQ vs py (P85: S0,S1,AM16,AC71,BM10,BC67; R84:
  AM16,AQ4,AC61,BM16,BC65,M29,QH16). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 5624/0 GREEN;
  PINS-RGRAM set-eq 5624/5624; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2812/2812 GREEN; full C battery 5624/0 GREEN (rc=0);
  own-loop fresh-oracle 46317..46664: 348/0, pins 46/46.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band95).
- Verdict: PASS-functional. No RED, no FLAG.
