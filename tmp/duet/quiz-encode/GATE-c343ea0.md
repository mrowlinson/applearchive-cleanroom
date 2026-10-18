# GATE-c343ea0 — band114 C-port T10R96 — PASS-functional

- Tree: lane-diff vs 6df65ce: src/c/rgramc.c only
  (+975/-816). Tables 1/1 EQ vs py (R96: C; full
  audit 1D 164/0 + 2D 685/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6312/0 GREEN;
  PINS-RGRAM set-eq 6312/6312; all other functional
  legs PASS 18/18 (RAWENC/PBZE/LZMA/LZ4 + -C,
  SMOKE/IMPL, OUTER2, RB2, RAVFRAME, UNITS, LZ4C,
  OSS nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3156/3156 GREEN; full C battery 6312/0 GREEN (rc=0);
  own-loop fresh-oracle 50933..51188: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
