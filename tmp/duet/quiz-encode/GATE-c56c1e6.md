# GATE-c56c1e6 — band139 C-port T10R109 — PASS-functional

- Tree: lane-diff vs c3a7a9b: src/c/rgramc.c only
  (+1036/-895). Tables 3/3 new EQ vs py (_T10R109C
  2D n=138 + _T10R109M str n=16 + _N=69 row-count
  derived-consistent; full audit 1D 164/0 + 2D 737/0
  + dicts 11/0 + STR 192/0 + STRARR 868/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6972/0 GREEN;
  PINS-RGRAM set-eq 6972/6972; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3486/3486 GREEN; full C battery 6972/0 GREEN (rc=0);
  own-loop fresh-oracle 55457..55712: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b138 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
