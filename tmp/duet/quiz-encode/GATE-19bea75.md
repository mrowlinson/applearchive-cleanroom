# GATE-19bea75 — band126 C-port T10P105 — PASS-functional

- Tree: lane-diff vs 814a732: src/c/rgramc.c only
  (+1297/-853). Tables 13/13 EQ vs py (P105: S0,S1,
  AM16,BM10,M16,QR4,QT4, AC74,BC67,QC64 + 3 counts;
  full audit 1D 7097/0 + 2D 69458/0 + STR 112/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6650/0 GREEN;
  PINS-RGRAM set-eq 6650/6650; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3325/3325 GREEN; full C battery 6650/0 GREEN (rc=0);
  own-loop fresh-oracle 53277..53368: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
