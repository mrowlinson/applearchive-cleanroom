# GATE-ef51ec3 — band162 C-port T10P123 — PASS-functional

- Tree: lane-diff vs ef51ec3^: src/c/rgramc.c only
  (+1422/-971). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=76/BC_N=70/QC_N=64 C==py;
  full audit 1D 166/0 + 2D 784/0 + STR 225/0 +
  STRARR 943/0 + dicts 11/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7536/0 GREEN;
  PINS-RGRAM set-eq 7536/7536; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3768/3768 GREEN; full C battery 7536/0 GREEN (rc=0);
  own-loop fresh-oracle 59541..59632: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b160 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
