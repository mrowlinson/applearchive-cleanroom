# VERIFY-b1f4334 T10R37 30053..30308: PASS

## first-hand (at-commit tree ver-b1f4334, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 30053..30308 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 30052 CLOSED T10P38Q off=63 (prev tier intact);
  30309 "N out of scope" rc=2.
- verdict labels: R37 off=0/61/255 spots correct.
- consts non-vacuous: _T10R37M (m-tab NEW) + _T10R37QH
  (q-head) + _T10R37C populated; q = P38M-suf + qhead
  per commit msg (partial SUFFIX reuse, no full Q tab),
  0 oracle violations across 256/256.

## verdict: PASS (T10R37 30053..30308 CLOSED 256/256)
