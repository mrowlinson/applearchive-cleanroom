# GATE-e5ed337 — band180 C-port T10P132 — PASS-functional

- Tree: lane-diff vs e5ed337^: src/c/rgramc.c only
  (+1490/-1027). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=76/BC_N=73/QC_N=65 C==py;
  full audit 1D 166/0 + 2D 820/0 + STR 246/0 +
  STRARR 1003/0 + dicts 11/0; added-string 8/8).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 7980/0 GREEN;
  PINS-RGRAM set-eq 7980/7980; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11, 1895352 bytes);
  RGRAMC-PYID 3990/3990 GREEN; full C battery 7980/0
  GREEN (rc=0); own-loop fresh-oracle 62673..62764:
  92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b178 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
- Provenance: r12 takeover of stale r12b claim (see
  CLAIM-sweep2-e5ed337-r12.md); all evidence first-hand
  in WS r12-e5ed337/, sibling r12b-* untouched.
