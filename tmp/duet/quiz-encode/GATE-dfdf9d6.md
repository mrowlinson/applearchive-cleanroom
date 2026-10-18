# GATE-dfdf9d6 — band98 C-port T10P87+T10R86 — PASS-functional

- Tree: lane-diff vs 2ed27ea merge: src/c/rgramc.c only
  (+1333/-742). py + PINS + test byte-identical. Tables
  13/13 EQ vs py (P87: S0,S1,AM16,AC72,BM10,BC69; R86:
  AM16,AQ4,AC62,BM16,BC63,B18,QH16). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 5716/0 GREEN;
  PINS-RGRAM set-eq 5716/5716; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2858/2858 GREEN; full C battery 5716/0 GREEN (rc=0);
  own-loop fresh-oracle 47013..47360: 348/0, pins 46/46.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band97).
- Verdict: PASS-functional. No RED, no FLAG.
