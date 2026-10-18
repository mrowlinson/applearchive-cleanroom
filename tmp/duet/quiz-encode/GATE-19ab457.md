# GATE-19ab457 — band103 C-port T10P92+T10B91 — PASS-functional

- Tree: lane-diff vs 73df8f0 merge: src/c/rgramc.c only
  (+1374/-773). py + PINS + test byte-identical. Tables
  4/4 EQ vs py (P92: AC,BC,QC; B91: C). Wall-grep
  lane-diff 0.
- Gate battery first-hand: RGRAM py 5996/0 GREEN;
  PINS-RGRAM set-eq 5996/5996; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  2998/2998 GREEN; full C battery 5996/0 GREEN (rc=0);
  own-loop fresh-oracle 48753..49100: 348/0, pins 66/66.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band102).
- Verdict: PASS-functional. No RED, no FLAG.
