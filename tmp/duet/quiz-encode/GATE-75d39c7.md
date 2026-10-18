# GATE-75d39c7 — band186 C-port T10P135 — PASS-functional

- Tree: lane-diff vs 75d39c7^: src/c/rgramc.c only
  (+1511/-1048). Tables-new 3/3 EQ vs py (AC/BC/QC +
  _N row-counts AC_N=77/BC_N=71/QC_N=67 C==py;
  full audit 1D 166/0 + 2D 832/0 + STR 255/0 +
  STRARR 1021/0 + dicts 11/0; added-string 8/8).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 8128/0 GREEN;
  PINS-RGRAM set-eq 8128/8128; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11, 1929464 bytes);
  RGRAMC-PYID 4064/4064 GREEN; full C battery 8128/0
  GREEN (rc=0); own-loop fresh-oracle 63717..63808:
  92/0, pins 28/28.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file + hit-sets identical to b184 (HYG 13/13,
  CONTAM 43/43, LIBC 4/4) -> OBSERVED-inherited per
  PARENT-032 (gate-tip raw: FAIL). ADOPT WARN diff
  (same c8f52713/c5f921d5).
- Verdict: PASS-functional. No RED, no FLAG.
- Provenance: sweep2-r14 first-hand in WS r14-75d39c7/
  (claim CLAIM-sweep2-75d39c7.md; PYID corpus seeded
  by hardlink from r14 b184 cache, py+C freshly
  executed per pin).
