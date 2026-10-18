# GATE-fd438da — band147 C-port T10R113 — PASS-functional

- Tree: lane-diff vs cddf1f3: src/c/rgramc.c only
  (+1083/-922). Tables added 4/4 EQ vs py (M/QH str
  n=16, C num n=66, C_N=66 derived-consistent;
  full audit 1D 166/0 + 2D 753/0 + dicts 11/0 +
  STR 203/0 + STRARR 894/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7166/0 GREEN;
  PINS-RGRAM set-eq 7166/7166; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3583/3583 GREEN; full C battery 7166/0 GREEN (rc=0);
  own-loop fresh-oracle 56849..57104: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b146 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
