# FLAG-CLEARED-b6fe0f7-ndp2: test-randomness flake, code tip exonerated

- RED was: gate-tip.sh @b6fe0f7 OUTER2 a-nd-p2 char 14 vs 13.
- cause: NDP p2 pins first-diff byte offset between two
  ECDSA-signed encrypts; signature randomness moves the
  offset run to run (sibling p0 already verdict-only for
  ECDSA-unstable). test-side, not code-side.
- evidence: SAME extracted tree, outer2 leg rerun 2/2
  OUTER2-GREEN (work/outer2-rerun, work/outer2-rerun2).
  b6fe0f7 diff rgram-only; outer2 path untouched.
- verdict: FLAG CLEARED. standing note for parent: a-nd-p2
  pin is randomness-sensitive (same class as p0/p3) —
  candidate for verdict-only treatment like its siblings.
