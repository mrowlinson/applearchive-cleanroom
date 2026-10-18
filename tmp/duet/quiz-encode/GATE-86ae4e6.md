# GATE-86ae4e6 — band167 C-port T10R123 — PASS-functional

- Tree: lane-diff vs 2c6eb79: src/c/rgramc.c only
  (+1129/-988). Tables added 3/3 EQ vs py (M str n=16,
  C num n=69, C_N=69 derived-consistent; full audit 1D
  166/0 + 2D 793/0 + dicts 11/0 + STR 229/0 + STRARR
  957/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7662/0 GREEN;
  PINS-RGRAM set-eq 7662/7662; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3831/3831 GREEN; full C battery 7662/0 GREEN (rc=0);
  own-loop fresh-oracle 60329..60584: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b165 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
