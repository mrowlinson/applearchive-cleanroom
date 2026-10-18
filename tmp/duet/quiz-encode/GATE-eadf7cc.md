# GATE-eadf7cc — band106 C-port T10P94 — PASS-functional

- Tree: lane-diff vs 9507514 merge: src/c/rgramc.c only
  (+1323/-786). py + PINS + test byte-identical. Tables
  5/5 EQ vs py (P94: QR,AC,M10C,M16C,QC). Wall-grep
  lane-diff 0.
- Gate battery first-hand: RGRAM py 6086/0 GREEN;
  PINS-RGRAM set-eq 6086/6086; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3043/3043 GREEN; full C battery 6086/0 GREEN (rc=0);
  own-loop fresh-oracle 49449..49540: 92/0, pins 28/28.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band102).
- Verdict: PASS-functional. No RED, no FLAG.
