# GATE-5db2d64 — band131 C-port T10R105 — PASS-functional

- Tree: lane-diff vs ae79d9e: src/c/rgramc.c only
  (+1011/-871). Tables 3/3 EQ vs py (R105: M16, C67,
  C_N67; full audit 1D 7244/0 + 2D 70696/0 + STR
  117/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6774/0 GREEN;
  PINS-RGRAM set-eq 6774/6774; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3387/3387 GREEN; full C battery 6774/0 GREEN (rc=0);
  own-loop fresh-oracle 54065..54320: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
