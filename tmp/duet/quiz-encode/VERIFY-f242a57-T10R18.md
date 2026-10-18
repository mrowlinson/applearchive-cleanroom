# VERIFY-f242a57 T10R18 23441..23696: PASS

## first-hand (at-commit tree ver-f242a57, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z23696-closed, PASS g-z23696).
- FULL battery 23441..23696 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF.
- boundary: 23440 CLOSED T10PJQ off=63 (prev tier intact);
  23697 "N out of scope" rc=2.
- verdict labels: T10R18 off=0/59/159/255 spots correct.
- consts non-vacuous: _T10R18C len 60, 0 oracle violations.

## verdict: PASS (T10R18 23441..23696 CLOSED 256/256)
