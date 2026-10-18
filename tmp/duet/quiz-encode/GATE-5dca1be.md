# GATE-5dca1be — band111 C-port T10P97 — PASS-functional

- Tree: lane-diff vs 8147e8f: src/c/rgramc.c only
  (+1243/-805). Tables 3/3 EQ vs py (P97: AC,BC,QC;
  full audit 1D 164/0 + 2D 680/0). Wall-grep
  lane-diff 0.
- Gate battery: RGRAM py 6238/0 GREEN; PINS-RGRAM
  set-eq 6238/6238; all other functional legs PASS
  (RAWENC/PBZE/LZMA/LZ4 + -C, SMOKE/IMPL, OUTER2,
  RB2, RAVFRAME, UNITS, LZ4C, OSS nominated-only).
  (gate-tip log reaped verified-complete from prior
  seat run, same script+tree; all C-side legs below
  rerun first-hand this seat.)
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID
  3119/3119 GREEN; full C battery 6238/0 GREEN (rc=0);
  own-loop fresh-oracle 50493..50584: 92/0, pins 28/28.
- HYGIENE/CONTAM/LIBCOMPRESSION legs scoped: 0 hits in
  lane file (selfgen .aar, DERIVATION/docs prose,
  aad.c libcompression) -> OBSERVED-inherited per
  PARENT-032 (gate-tip raw: FAIL). ADOPT WARN diff.
- Verdict: PASS-functional. No RED, no FLAG.
