# GATE-f341d1b — band92 C-port T10P81+T10R80 — PASS-functional

- Tree: lane-diff vs 6cc4588 merge: src/c/rgramc.c only
  (+1268/-706). Tables 11/11 EQ vs py (P81: S0,S1,AM16,BM10,
  AC,BC; R80: AM16,AQ4,BM16,AC,BC). Wall-grep lane-diff 0.
- Gate battery first-hand: RGRAM py 5440/0 GREEN; PINS-RGRAM
  set-eq 5440/5440; all other functional legs PASS.
- C-side first-hand (seat-private build): C-BUILD PASS 0
  warnings (-O2 -Wall -Wextra -std=c11); RGRAMC-PYID 2720/2720
  GREEN; full C battery 5440/0 GREEN (rc=0). storm.sh absent
  at this tree -> SKIP.
- HYGIENE/CONTAM/LIBCOMPRESSION/ADOPT legs scoped: hits in
  pre-tip tree files only (selfgen .aar, DERIVATION prose,
  aad.c libcompression, harness adapter), none in lane-diff
  -> OBSERVED-inherited per PARENT-032 (gate-tip raw: FAIL).
- Verdict: PASS-functional. No RED, no FLAG.
