# GATE-80b550e — band136 C-port T10P110 — PASS-functional

- Tree: lane-diff vs c72589f: src/c/rgramc.c only
  (+1330/-884). Tables 10/10 new EQ vs py (S0/S1,
  AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  76/67/66 derived-consistent; full audit 1D 1030/0
  + 2D 732/0 + dicts 11/0 + STR 185/0 + _N 739/0;
  4 missing-in-C legacy-explained: 3 dead in py,
  1 inlined-equal bytes). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6898/0 GREEN;
  PINS-RGRAM set-eq 6898/6898; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3449/3449 GREEN; full C battery 6898/0 GREEN (rc=0);
  own-loop fresh-oracle 55017..55108: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b135 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
