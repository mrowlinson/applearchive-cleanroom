# VERIFY-f6dfa38 T10R38 30401..30656: PASS

## first-hand (at-commit tree ver-f6dfa38, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 30401..30656 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 30400 CLOSED T10P39Q off=63 (prev tier intact);
  30657 "N out of scope" rc=2.
- verdict labels: R38 off=0/61/255 spots correct.
- consts non-vacuous: _T10R38M (m-tab NEW) + _T10R38QH
  (q-head) + _T10R38C populated; q = P39M-xor + qhead
  per commit msg (xor-lencode family), 0 oracle
  violations across 256/256.

## verdict: PASS (T10R38 30401..30656 CLOSED 256/256)
