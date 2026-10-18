# VERIFY-64d23ac T10P23 24741..24832: PASS

## first-hand (at-commit tree ver-64d23ac, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z24832-closed, PASS g-z24832).
- FULL battery 24741..24832 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 24740 CLOSED T10R21 off=255 (prev tier intact);
  24833 "N out of scope" rc=2.
- verdict labels: PN0 24741 / PN1 24742 / PNA 24743 off=0 /
  PNB 24759 off=0 / PNQ 24769 off=0, 24832 off=63 — all
  correct tokens, letter N collision-free (A-M taken).
- consts non-vacuous: 9 _T10PN tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P23 24741..24832 CLOSED 92/92)
