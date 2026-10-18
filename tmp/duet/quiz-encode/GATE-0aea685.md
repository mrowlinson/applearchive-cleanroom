# GATE-0aea685 — band119 C-port T10R99 — PASS-functional

- Tree: lane-diff vs 0323580: src/c/rgramc.c only
  (+975/-834). Tables 1/1 EQ vs py (R99: C; full
  audit 1D 164/0 + 2D 697/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6476/0 GREEN;
  PINS-RGRAM set-eq 6476/6476; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3238/3238 GREEN; full C battery 6476/0 GREEN (rc=0);
  own-loop fresh-oracle 51977..52232: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
