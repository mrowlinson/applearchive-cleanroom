# GATE-ab7eb30 — band135 C-port T10R107 — PASS-functional

- Tree: lane-diff vs 90ae088: src/c/rgramc.c only
  (+1024/-883). Tables 1/1 new EQ vs py (_T10R107C;
  full audit 1D 164/0 + 2D 729/0 + dicts 11/0 + STR
  188+856/0). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6872/0 GREEN;
  PINS-RGRAM set-eq 6872/6872; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3436/3436 GREEN; full C battery 6872/0 GREEN (rc=0);
  own-loop fresh-oracle 54761..55016: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b134 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
