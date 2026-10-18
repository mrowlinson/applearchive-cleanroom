# GATE-cf2775e — band150 C-port T10P117 — PASS-functional

- Tree: lane-diff vs 56782d2: src/c/rgramc.c only
  (+1390/-930). Tables added 14/14 EQ vs py (S0/S1/
  S2, AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  AC_N=74/BC_N=67/QC_N=66 C-rows==py-rows; full audit
  1D 166/0 + 2D 760/0 + dicts 11/0 + STR 209/0 +
  STRARR 905/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7238/0 GREEN;
  PINS-RGRAM set-eq 7238/7238; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3619/3619 GREEN; full C battery 7238/0 GREEN (rc=0);
  own-loop fresh-oracle 57453..57544: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b149 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
