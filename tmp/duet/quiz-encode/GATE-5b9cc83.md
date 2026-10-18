# GATE-5b9cc83 — band158 C-port T10P121 — PASS-functional

- Tree: lane-diff vs 8e3537c: src/c/rgramc.c only
  (+1408/-958). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=75/BC_N=72/QC_N=65 C==py;
  full audit 1D 166/0 + 2D 776/0 + STR 220/0 +
  STRARR 931/0 + dicts 11/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7438/0 GREEN;
  PINS-RGRAM set-eq 7438/7438; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3719/3719 GREEN; full C battery 7438/0 GREEN (rc=0);
  own-loop fresh-oracle 58845..58936: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b157 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
