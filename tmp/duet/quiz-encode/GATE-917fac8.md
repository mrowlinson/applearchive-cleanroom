# GATE-917fac8 — band112 C-port T10R95 — PASS-functional

- Tree: lane-diff vs 4313132: src/c/rgramc.c only
  (+951/-810). Tables 1/1 EQ vs py (R95: C; full
  audit 1D 164/0 + 2D 681/0). Wall-grep lane-diff 0.
- Gate battery: RGRAM py 6264/0 GREEN; PINS-RGRAM
  set-eq 6264/6264; all other functional legs PASS
  (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
  (gate-tip log reaped verified-complete from prior
  seat run, same script+tree; all C-side legs below
  rerun first-hand this seat.)
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3132/3132 GREEN; full C battery 6264/0 GREEN (rc=0);
  own-loop fresh-oracle 50585..50840: 256/0, pins 26/26.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file -> OBSERVED-inherited per PARENT-032
  (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
