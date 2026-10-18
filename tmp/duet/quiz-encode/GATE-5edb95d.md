# GATE-5edb95d — band160 C-port T10P122 — PASS-functional

- Tree: lane-diff vs 20d2cf4: src/c/rgramc.c only
  (+1427/-964). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=76/BC_N=72/QC_N=65 C==py;
  full audit 1D 166/0 + 2D 780/0 + STR 223/0 +
  STRARR 937/0 + dicts 11/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7490/0 GREEN;
  PINS-RGRAM set-eq 7490/7490; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3745/3745 GREEN; full C battery 7490/0 GREEN (rc=0);
  own-loop fresh-oracle 59193..59284: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b159 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
