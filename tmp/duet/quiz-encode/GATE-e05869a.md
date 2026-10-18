# GATE-e05869a — band117 C-port T10R98 — PASS-functional

- Tree: lane-diff vs 0563d71: src/c/rgramc.c only
  (+987/-828). Tables 1/1 EQ vs py (R98: C; full
  audit 1D 164/0 + 2D 693/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6422/0 GREEN;
  PINS-RGRAM set-eq 6422/6422; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3211/3211 GREEN; full C battery 6422/0 GREEN (rc=0);
  own-loop fresh-oracle 51629..51884: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
