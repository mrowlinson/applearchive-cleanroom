# GATE-31e41ed — band118 C-port T10P101 — PASS-functional

- Tree: lane-diff vs 25c6f81: src/c/rgramc.c only
  (+1267/-829). Tables 3/3 EQ vs py (P101: AC,BC,QC;
  full audit 1D 164/0 + 2D 696/0). Wall-grep
  lane-diff 0.
- Gate battery first-hand: RGRAM py 6450/0 GREEN;
  PINS-RGRAM set-eq 6450/6450; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3225/3225 GREEN; full C battery 6450/0 GREEN (rc=0);
  own-loop fresh-oracle 51885..51976: 92/0, pins 28/28.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
