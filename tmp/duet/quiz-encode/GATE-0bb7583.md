# GATE-0bb7583 — band148 C-port T10P116 — PASS-functional

- Tree: lane-diff vs fd02d44: src/c/rgramc.c only
  (+1383/-923). Tables added 14/14 EQ vs py (S0/S1/
  S2, AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  derived-consistent; full audit 1D 166/0 + 2D 756/0
  + dicts 11/0 + STR 206/0 + STRARR 899/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7190/0 GREEN;
  PINS-RGRAM set-eq 7190/7190; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3595/3595 GREEN; full C battery 7190/0 GREEN (rc=0);
  own-loop fresh-oracle 57105..57196: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b147 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
