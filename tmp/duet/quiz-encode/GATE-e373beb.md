# GATE-e373beb — band140 C-port T10P112 — PASS-functional

- Tree: lane-diff vs 5e5947a: src/c/rgramc.c only
  (+1348/-896). Tables 14/14 new EQ vs py (S0/S1,
  AM/AC, BM/BC, M, XB 16/16, QR/QT/QC + 3 _N
  row-counts derived-consistent; full audit 1D 165/0
  + 2D 740/0 + dicts 11/0 + STR 194/0 + STRARR
  873/0; verify-added XB "Clen=27" = tool artifact,
  single-line decl regex overrun into QR strings,
  hand-verified 16/16 EQ + audit-tables 1D EQ).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6996/0 GREEN;
  PINS-RGRAM set-eq 6996/6996; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3498/3498 GREEN; full C battery 6996/0 GREEN (rc=0);
  own-loop fresh-oracle 55713..55804: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b139 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
