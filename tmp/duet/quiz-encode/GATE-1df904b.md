# GATE-1df904b — band133 C-port T10R106 — PASS-functional

- Tree: lane-diff vs 3495f7f: src/c/rgramc.c only
  (+1018/-877). Tables 3/3 EQ vs py (R106: M16, C68,
  C_N68 derived-consistent; full audit 1D 164/0 + 2D
  725/0 + dicts 11/0 + STR 186+850/0). Wall-grep
  lane-diff 0.
- Gate battery first-hand: RGRAM py 6824/0 GREEN;
  PINS-RGRAM set-eq 6824/6824; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3412/3412 GREEN; full C battery 6824/0 GREEN (rc=0);
  own-loop fresh-oracle 54413..54668: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b132 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
