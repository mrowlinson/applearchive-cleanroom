# GATE-e02b8fe — band178 C-port T10P131 — PASS-functional

- Tree: lane-diff vs e02b8fe^: src/c/rgramc.c only
  (+1483/-1020). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=74/BC_N=70/QC_N=63 C==py;
  full audit 1D 166/0 + 2D 816/0 + STR 243/0 +
  STRARR 996/0 + dicts 11/0; added-string 8/8).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7930/0 GREEN;
  PINS-RGRAM set-eq 7930/7930; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11, 1878456 bytes);
  RGRAMC-PYID 3965/3965 GREEN; full C battery 7930/0
  GREEN (rc=0); own-loop fresh-oracle 62325..62416:
  92/0, pins 30/30.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b176 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
