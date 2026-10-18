# GATE-d86b95a — band141 C-port T10R110 — PASS-functional

- Tree: lane-diff vs ef02d89: src/c/rgramc.c only
  (+1062/-901). Tables added 4/4 EQ vs py (M/QH
  str n=16, C num n=67, C_N=67 derived-consistent;
  full audit 1D 165/0 + 2D 741/0 + dicts 11/0 +
  STR 194/0 + STRARR 875/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7020/0 GREEN;
  PINS-RGRAM set-eq 7020/7020; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3510/3510 GREEN; full C battery 7020/0 GREEN (rc=0);
  own-loop fresh-oracle 55805..56060: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b140 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
