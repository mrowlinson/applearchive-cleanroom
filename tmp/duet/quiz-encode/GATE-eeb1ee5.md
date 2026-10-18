# GATE-eeb1ee5 — band110 C-port T10P96+T10R94 — PASS-functional

- Tree: lane-diff vs 5e72665 merge: src/c/rgramc.c only
  (+1378/-799). py + PINS + test byte-identical. Tables
  4/4 EQ vs py (P96: AC,BC,QC; R94: C). Wall-grep
  lane-diff 0.
- Gate battery first-hand: RGRAM py 6210/0 GREEN;
  PINS-RGRAM set-eq 6210/6210; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3105/3105 GREEN; full C battery 6210/0 GREEN (rc=0);
  own-loop fresh-oracle 50145..50492: 348/0, pins 52/52.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band102).
- Verdict: PASS-functional. No RED, no FLAG.
