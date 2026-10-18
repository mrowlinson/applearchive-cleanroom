# VERIFY-4c5b869 T10R28 26921..27176: PASS

## first-hand (at-commit tree ver-4c5b869, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 26921..27176 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF.
- boundary: 26920 CLOSED T10PTQ off=63 (prev tier intact);
  27177 "N out of scope" rc=2.
- verdict labels: R28 off=0/61/255 spots correct.
- consts non-vacuous: _T10R28M (m-tab NEW) + _T10R28C
  populated; q-tab reuses PTM per commit msg (no _T10R28Q),
  0 oracle violations across 256/256.

## verdict: PASS (T10R28 26921..27176 CLOSED 256/256)
