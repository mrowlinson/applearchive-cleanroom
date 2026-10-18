# VERIFY-055bb85 T10R20 24137..24392: PASS

## first-hand (at-commit tree ver-055bb85, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z24392-closed, PASS g-z24392).
- FULL battery 24137..24392 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 9 pin
  rows in range, 9/9 MATCH, 0 SHADIFF.
- boundary: 24136 CLOSED T10PLQ off=63 (prev tier intact);
  24393 "N out of scope" rc=2.
- verdict labels: R20 off=0/61/255 spots correct.
- consts non-vacuous: _T10R20M + _T10R20Q + _T10R20C
  populated, 0 oracle violations across 256/256.
- pins +16/-0, no unrelated deltas (3 files: rgram.py +
  test list + PINS).

## verdict: PASS (T10R20 24137..24392 CLOSED 256/256)
