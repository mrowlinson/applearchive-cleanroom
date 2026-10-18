# NOTE-FLAKE-a-nd-p3 (non-blocking): nondet-char pin varies 14/15

- evidence (sweep, first-hand): gate run on cdee48a extract:
  a-nd-p3 FAIL (char 15 vs pin 14). re-run SAME extract
  minutes later: PASS (char 14), OUTER2-GREEN exit 0.
  outer2 files untouched by tip chain (rgram-only).
- verdict: flaky PIN (AEA p3 first-diff char is run-varying),
  not a code regression. gate verdict unaffected (PASS).
- remedy for writer (next outer2 touch, non-blocking): give
  a-nd-p3 the p0-treatment — verdict-only DIFF pin (GATE-
  ac38c8a precedent: ECDSA-unstable c14/16/17) or char-set
  pin {14,15} if the set stays closed. p2/p4 watched (green
  2/2 this shift). clears when pin lands + re-gate green.
