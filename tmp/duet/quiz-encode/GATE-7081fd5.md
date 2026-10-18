# GATE-7081fd5 — band124 C-port T10P104 — PASS-functional

- Tree: lane-diff vs dc5d75b: src/c/rgramc.c only
  (+1287/-847). Tables 13/13 EQ vs py (P104: S0,S1,
  AM16,BM10,M16,QR4,QT4, AC77,BC60,QC63 + 3 counts;
  full audit 1D 7031/0 + 2D 68910/0 + STR 110/0).
  Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 6600/0 GREEN;
  PINS-RGRAM set-eq 6600/6600; all other functional
  legs PASS (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
  OUTER2 leg flaked once under 6-way load (a-nondet
  283/284); isolated rerun 284/284 GREEN + pins
  set-eq 284/284 first-hand. Lane file cannot affect
  outer2 (rgramc.c-only).
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3300/3300 GREEN; full C battery 6600/0 GREEN (rc=0);
  own-loop fresh-oracle 52929..53020: 92/0, pins 24/24.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
