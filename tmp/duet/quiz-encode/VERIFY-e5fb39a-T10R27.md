# VERIFY-e5fb39a T10R27 26573..26828: PASS

## first-hand (at-commit tree ver-e5fb39a, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 26573..26828 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF.
- boundary: 26572 CLOSED T10PSQ off=63 (prev tier intact);
  26829 "N out of scope" rc=2.
- verdict labels: R27 off=0/61/255 spots correct.
- consts non-vacuous: _T10R27M (m-tab NEW) + _T10R27C
  populated; q-tab reuses PSM per commit msg (no _T10R27Q),
  0 oracle violations across 256/256.

## verdict: PASS (T10R27 26573..26828 CLOSED 256/256)
