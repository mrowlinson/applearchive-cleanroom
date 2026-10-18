# GATE-a31520e — band184 C-port T10P134 — PASS-functional

- Tree: lane-diff vs a31520e^: src/c/rgramc.c only
  (+1517/-1040). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=76/BC_N=72/QC_N=62 C==py;
  full audit 1D 166/0 + 2D 828/0 + STR 252/0 +
  STRARR 1015/0 + dicts 11/0; added-string 9/9).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 8076/0 GREEN;
  PINS-RGRAM set-eq 8076/8076; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11, 1912584 bytes);
  RGRAMC-PYID 4038/4038 GREEN; full C battery 8076/0
  GREEN (rc=0); own-loop fresh-oracle 63369..63460:
  92/0, pins 28/28.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-set identical to b182 -> OBSERVED-
  inherited per PARENT-032 (gate-tip raw: FAIL). ADOPT
  WARN diff (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
- Provenance: sweep2-r13 first-hand in WS r13-a31520e/
  (claim CLAIM-sweep2-a31520e.md; viewer4 VERIFY claim
  independent per PARENT-068/069, awaits this GATE).
  Added-script rc=1 is a stale hardcoded ==8 expectation
  (b184 has 9 new string tables, all EQ) — content PASS.
