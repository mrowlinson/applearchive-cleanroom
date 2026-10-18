# GATE-bf2d330 — band142 C-port T10P113 — PASS-functional

- Tree: lane-diff vs 188be03: src/c/rgramc.c only
  (+1361/-902). Tables added 14/14 EQ vs py (S0/S1/
  S2, AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  derived-consistent; full audit 1D 165/0 + 2D 744/0
  + dicts 11/0 + STR 197/0 + STRARR 880/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7044/0 GREEN;
  PINS-RGRAM set-eq 7044/7044; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3522/3522 GREEN; full C battery 7044/0 GREEN (rc=0);
  own-loop fresh-oracle 56061..56152: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b141 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
