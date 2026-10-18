# VERIFY-f03ca3b T10R26 26225..26480: PASS

## first-hand (at-commit tree ver-f03ca3b, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 26225..26480 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF.
- boundary: 26224 CLOSED T10PRQ off=63 (prev tier intact);
  26481 "N out of scope" rc=2.
- verdict labels: R26 off=0/61/255 spots correct.
- consts non-vacuous: _T10R26M (m-tab NEW) + _T10R26C
  populated; q-tab reuses PRM per commit msg (no _T10R26Q),
  0 oracle violations across 256/256.

## verdict: PASS (T10R26 26225..26480 CLOSED 256/256)
