# GATE-10c9f16 — band159 C-port T10R119 — PASS-functional

- Tree: lane-diff vs 5b5ae12: src/c/rgramc.c only
  (+1104/-963). Tables added 3/3 EQ vs py (M str n=16,
  C num n=70, C_N=70 derived-consistent; full audit 1D
  166/0 + 2D 777/0 + dicts 11/0 + STR 220/0 + STRARR
  932/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7464/0 GREEN;
  PINS-RGRAM set-eq 7464/7464; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3732/3732 GREEN; full C battery 7464/0 GREEN (rc=0);
  own-loop fresh-oracle 58937..59192: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b157 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
