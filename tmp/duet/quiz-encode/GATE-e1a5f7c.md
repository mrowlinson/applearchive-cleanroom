# GATE-e1a5f7c — band163 C-port T10R121 — PASS-functional

- Tree: lane-diff vs 06855bc: src/c/rgramc.c only
  (+1137/-976). Tables added 4/4 EQ vs py (M str n=16,
  QH str n=16, C num n=66, C_N=66 derived-consistent;
  full audit 1D 166/0 + 2D 785/0 + dicts 11/0 + STR
  225/0 + STRARR 945/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7562/0 GREEN;
  PINS-RGRAM set-eq 7562/7562; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3781/3781 GREEN; full C battery 7562/0 GREEN (rc=0);
  own-loop fresh-oracle 59633..59888: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b161 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
