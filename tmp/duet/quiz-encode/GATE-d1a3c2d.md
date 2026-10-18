# GATE-d1a3c2d — band182 C-port T10P133 — PASS-functional

- Tree: lane-diff vs d1a3c2d^: src/c/rgramc.c only
  (+1484/-1034). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=75/BC_N=71/QC_N=62 C==py;
  full audit 1D 166/0 + 2D 824/0 + STR 248/0 +
  STRARR 1009/0 + dicts 11/0; added-string 7/7).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 8028/0 GREEN;
  PINS-RGRAM set-eq 8028/8028; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11, 1895688 bytes);
  RGRAMC-PYID 4014/4014 GREEN; full C battery 8028/0
  GREEN (rc=0); own-loop fresh-oracle 63021..63112:
  92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b180 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
- Provenance: sweep2-r13 first-hand in WS r13-d1a3c2d/
  (claim CLAIM-sweep2-d1a3c2d.md; viewer VERIFY claim
  independent per PARENT-068/069). Added-script rc=1 is
  a stale hardcoded ==8 expectation (b182 has 7 new
  string tables, all EQ) — content PASS, noted.
