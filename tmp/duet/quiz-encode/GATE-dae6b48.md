# GATE-dae6b48 — band152 C-port T10P118 — PASS-functional

- Tree: lane-diff vs d497e00: src/c/rgramc.c only
  (+1400/-937). Tables added 14/14 EQ vs py (S0/S1/
  S2, AM/AC, BM/BC, M, QR/QT/QC + 3 _N row-counts
  AC_N=76/BC_N=72/QC_N=64 C-rows==py-rows; full audit
  1D 166/0 + 2D 764/0 + dicts 11/0 + STR 212/0 +
  STRARR 911/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7288/0 GREEN;
  PINS-RGRAM set-eq 7288/7288; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3644/3644 GREEN; full C battery 7288/0 GREEN (rc=0);
  own-loop fresh-oracle 57801..57892: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b151 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
