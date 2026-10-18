# GATE-9e30e0b — band123 C-port T10R101 — PASS-functional

- Tree: lane-diff vs cb0ab6f: src/c/rgramc.c only
  (+987/-846). Tables 3/3 EQ vs py (R101: M16, C67,
  C_N67; full audit 1D 6981/0 + 2D 68510/0 + STR
  108/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6576/0 GREEN;
  PINS-RGRAM set-eq 6576/6576; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3288/3288 GREEN; full C battery 6576/0 GREEN (rc=0);
  own-loop fresh-oracle 52673..52928: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
