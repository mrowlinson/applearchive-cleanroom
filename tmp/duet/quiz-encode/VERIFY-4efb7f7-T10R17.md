# VERIFY-4efb7f7 T10R17 23093..23348: PASS

## first-hand (at-commit tree ver-4efb7f7, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z23348-closed, PASS g-z23348).
- FULL battery 23093..23348 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF.
- boundary: 23092 CLOSED T10PIQ off=63 (prev tier intact);
  23349 "N out of scope" rc=2.
- verdict labels: T10R17 off=0/57/157/255 spots correct.
- consts non-vacuous: _T10R17C len 61, 0 oracle violations.

## verdict: PASS (T10R17 23093..23348 CLOSED 256/256)
