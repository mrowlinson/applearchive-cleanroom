# GATE-8ecae82 — band132 C-port T10P108 — PASS-functional

- Tree: lane-diff vs f67c8a8: src/c/rgramc.c only
  (+1318/-874). Tables 13/13 EQ vs py (P108: AC/AM,
  BC/BM, M, QC/QR/QT, S0/S1 + 3 _N row-counts
  derived-consistent; full audit 1D 164/0 + 2D 724/0 +
  dicts 11/0 + STR 186+849/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6800/0 GREEN;
  PINS-RGRAM set-eq 6800/6800; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3400/3400 GREEN; full C battery 6800/0 GREEN (rc=0);
  own-loop fresh-oracle 54321..54412: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b131 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
