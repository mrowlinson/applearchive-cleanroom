# GATE-f7cf078 — band121 C-port T10R100 — PASS-functional

- Tree: lane-diff vs 0a076a6: src/c/rgramc.c only
  (+981/-840). Tables 3/3 EQ vs py (R100: M16, C67,
  C_N67; full audit 1D 6911/0 + 2D 67986/0 + STR
  106/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6526/0 GREEN;
  PINS-RGRAM set-eq 6526/6526; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3263/3263 GREEN; full C battery 6526/0 GREEN (rc=0);
  own-loop fresh-oracle 52325..52580: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
