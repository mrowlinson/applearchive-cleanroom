# GATE-18f083f — band146 C-port T10P115 — PASS-functional

- Tree: lane-diff vs 4463b37: src/c/rgramc.c only
  (+1387/-915). Tables added 15/15 EQ vs py (S0/S1/
  S2/S3, AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  derived-consistent; full audit 1D 166/0 + 2D 752/0
  + dicts 11/0 + STR 203/0 + STRARR 892/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7142/0 GREEN;
  PINS-RGRAM set-eq 7142/7142; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3571/3571 GREEN; full C battery 7142/0 GREEN (rc=0);
  own-loop fresh-oracle 56757..56848: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b145 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
