# GATE-f8fe14f — band108 C-port T10P95 — PASS-functional

- Tree: lane-diff vs 8da55b7 merge: src/c/rgramc.c only
  (+1239/-793). py + PINS + test byte-identical. Tables
  4/4 EQ vs py (P95: AC,BC,QR,QC). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6134/0 GREEN;
  PINS-RGRAM set-eq 6134/6134; all other functional legs
  PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3067/3067 GREEN; full C battery 6134/0 GREEN (rc=0);
  own-loop fresh-oracle 49797..49888: 92/0, pins 22/22.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression), none in lane-diff ->
  OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
  ADOPT WARN diff (as band102).
- Verdict: PASS-functional. No RED, no FLAG.
