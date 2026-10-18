# GATE-9f75d55 — band144 C-port T10P114 — PASS-functional

- Tree: lane-diff vs 6e9422a: src/c/rgramc.c only
  (+1355/-911). Tables added 13/13 EQ vs py (S0/S1,
  AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  derived-consistent; full audit 1D 166/0 + 2D 748/0
  + dicts 11/0 + STR 199/0 + STRARR 886/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7092/0 GREEN;
  PINS-RGRAM set-eq 7092/7092; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3546/3546 GREEN; full C battery 7092/0 GREEN (rc=0);
  own-loop fresh-oracle 56409..56500: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b143 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
