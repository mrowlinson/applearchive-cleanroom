# VERIFY-b490c4e T10R34 29009..29264: PASS

## first-hand (at-commit tree ver-b490c4e, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 29009..29264 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 29008 CLOSED T10PZQ off=63 (prev tier intact);
  29265 "N out of scope" rc=2.
- verdict labels: R34 off=0/61/255 spots correct.
- consts non-vacuous: _T10R34M (m-tab NEW) + _T10R34C
  populated; q-tab exact PZM reuse per commit msg (no
  _T10R34Q), 0 oracle violations across 256/256.

## verdict: PASS (T10R34 29009..29264 CLOSED 256/256)
