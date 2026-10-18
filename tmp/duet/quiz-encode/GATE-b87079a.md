# GATE-b87079a — band138 C-port T10P111 — PASS-functional

- Tree: lane-diff vs e5b435f: src/c/rgramc.c only
  (+1336/-890). Tables 13/13 new EQ vs py (S0/S1
  plain, AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  76/67/63 derived-consistent; full audit 1D 164/0
  + 2D 736/0 + dicts 11/0 + STR 192/0 + STRARR
  867/0; py-only setdiff vs b137 = 5 new names, all
  C-present string tables = regex artifact, 0 new
  missing-in-C). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6948/0 GREEN;
  PINS-RGRAM set-eq 6948/6948; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3474/3474 GREEN; full C battery 6948/0 GREEN (rc=0);
  own-loop fresh-oracle 55365..55456: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b137 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
