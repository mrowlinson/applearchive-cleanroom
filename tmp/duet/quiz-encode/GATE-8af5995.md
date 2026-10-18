# GATE-8af5995 — band143 C-port T10R111 — PASS-functional

- Tree: lane-diff vs 5741e6b: src/c/rgramc.c only
  (+1047/-908). Tables added 4/4 EQ vs py (M str
  n=16, Q8 num1d n=16, C num n=67, C_N=67 derived-
  consistent; full audit 1D 166/0 + 2D 745/0 +
  dicts 11/0 + STR 197/0 + STRARR 881/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7068/0 GREEN;
  PINS-RGRAM set-eq 7068/7068; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3534/3534 GREEN; full C battery 7068/0 GREEN (rc=0);
  own-loop fresh-oracle 56153..56408: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b142 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
