# GATE-885fc37 — band151 C-port T10R115 — PASS-functional

- Tree: lane-diff vs a4866a6: src/c/rgramc.c only
  (+1077/-936). Tables added 3/3 EQ vs py (M str n=16,
  C num n=67, C_N=67 derived-consistent; full audit 1D
  166/0 + 2D 761/0 + dicts 11/0 + STR 209/0 + STRARR
  906/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7262/0 GREEN;
  PINS-RGRAM set-eq 7262/7262; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3631/3631 GREEN; full C battery 7262/0 GREEN (rc=0);
  own-loop fresh-oracle 57545..57800: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b149 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
