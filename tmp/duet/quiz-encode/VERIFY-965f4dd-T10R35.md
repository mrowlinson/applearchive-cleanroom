# VERIFY-965f4dd T10R35 29357..29612: PASS

## first-hand (at-commit tree ver-965f4dd, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 29357..29612 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 29356 CLOSED T10P36Q off=63 (prev tier intact);
  29613 "N out of scope" rc=2.
- verdict labels: R35 off=0/61/255 spots correct.
- consts non-vacuous: _T10R35M (m-tab NEW) + _T10R35C
  populated; q-tab exact P36M reuse per commit msg (no
  _T10R35Q), 0 oracle violations across 256/256.

## verdict: PASS (T10R35 29357..29612 CLOSED 256/256)
