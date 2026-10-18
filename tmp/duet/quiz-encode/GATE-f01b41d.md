# GATE-f01b41d — band168 C-port T10P126 — PASS-functional

- Tree: lane-diff vs f01b41d^: src/c/rgramc.c only
  (+1439/-989). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=75/BC_N=72/QC_N=62 C==py;
  full audit 1D 166/0 + 2D 796/0 + STR 231/0 +
  STRARR 962/0 + dicts 11/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7686/0 GREEN;
  PINS-RGRAM set-eq 7686/7686; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3843/3843 GREEN; full C battery 7686/0 GREEN (rc=0);
  own-loop fresh-oracle 60585..60676: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b166 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
