# VERIFY-f67973d T10R21 24485..24740: PASS

## first-hand (at-commit tree ver-f67973d, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z24740-closed, PASS g-z24740).
- FULL battery 24485..24740 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF.
- boundary: 24484 CLOSED T10PMQ off=63 (prev tier intact);
  24741 "N out of scope" rc=2.
- verdict labels: R21 off=0/61/255 spots correct.
- consts non-vacuous: _T10R21M (m-tab NEW) + _T10R21B5
  (b5-tab) + _T10R21C populated; q-tab reuses PMM per
  commit msg (no _T10R21Q — reuse, not omission),
  0 oracle violations across 256/256.

## verdict: PASS (T10R21 24485..24740 CLOSED 256/256)
