# VERIFY-ecbdd2b T10P19 23349..23440: PASS

## first-hand (at-commit tree ver-ecbdd2b, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z23440-closed, PASS g-z23440).
- FULL battery 23349..23440 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 23348 CLOSED T10R17 off=255 (prev tier intact);
  23441 "N out of scope" rc=2.
- verdict labels: PJ0 23349 / PJ1 23350 / PJA 23351..23366 /
  PJB 23367..23376 / PJQ 23377..23440 (off=63 end) — all
  correct tokens.
- consts non-vacuous: PJ0C 71, PJ1C 71, PJAC 69, PJBC 61,
  PJQC 57 — all 0 oracle violations.

## verdict: PASS (T10P19 23349..23440 CLOSED 92/92)
