# GATE-ae7c8dd — band172 C-port T10P128 — PASS-functional

- Tree: lane-diff vs ae7c8dd^: src/c/rgramc.c only
  (+1481/-1001). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=76/BC_N=72/QC_N=65 C==py;
  full audit 1D 166/0 + 2D 804/0 + STR 235/0 +
  STRARR 976/0 + dicts 11/0; added-string 9/9).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7780/0 GREEN;
  PINS-RGRAM set-eq 7780/7780; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3890/3890 GREEN; full C battery 7780/0 GREEN (rc=0);
  own-loop fresh-oracle 61281..61372: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b170 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
