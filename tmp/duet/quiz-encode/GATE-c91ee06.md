# GATE-c91ee06 — band137 C-port T10R108 — PASS-functional

- Tree: lane-diff vs 2aec499: src/c/rgramc.c only
  (+1030/-889). Tables 2/2 new EQ vs py (_T10R108C
  2D + _N=70 row-count derived-consistent, _T10R108M
  1D; full audit 1D 1031/0 + 2D 733/0 + dicts 11/0
  + STR 185/0 + _N 740/0; 4 missing-in-C legacy-
  explained: 3 dead in py, 1 inlined-equal bytes).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6922/0 GREEN;
  PINS-RGRAM set-eq 6922/6922; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3461/3461 GREEN; full C battery 6922/0 GREEN (rc=0);
  own-loop fresh-oracle 55109..55364: 256/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b136 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
