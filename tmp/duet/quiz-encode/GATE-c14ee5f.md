# GATE-c14ee5f — band130 C-port T10P107 — PASS-functional

- Tree: lane-diff vs bab78db: src/c/rgramc.c only
  (+1312/-866). Tables 13/13 EQ vs py (P107: S0,S1,
  AM16,BM10,M16,QR4,QT4, AC77,BC66,QC64 + 3 counts;
  full audit 1D 7228/0 + 2D 70562/0 + STR 117/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6750/0 GREEN;
  PINS-RGRAM set-eq 6750/6750; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  OUTER2, RB2, RAVFRAME, UNITS, LZ4C, OSS
  nominated-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3375/3375 GREEN; full C battery 6750/0 GREEN (rc=0);
  own-loop fresh-oracle 53973..54064: 92/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
