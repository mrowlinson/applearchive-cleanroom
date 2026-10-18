# GATE-6606cc1 — band116 C-port T10R97+T10P100 — PASS-functional

- Tree: lane-diff vs e90d885: src/c/rgramc.c only
  (+1401/-822). Tables 4/4 EQ vs py (R97: C; P100:
  AC,BC,QC; full audit 1D 164/0 + 2D 692/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6396/0 GREEN;
  PINS-RGRAM set-eq 6396/6396; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3198/3198 GREEN; full C battery 6396/0 GREEN (rc=0);
  own-loop fresh-oracle 51281..51628: 348/0, pins 54/54.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
