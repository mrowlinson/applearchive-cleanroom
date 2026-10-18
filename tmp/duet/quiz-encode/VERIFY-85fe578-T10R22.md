# VERIFY-85fe578 T10R22 24833..25088: PASS

## first-hand (at-commit tree ver-85fe578, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 24833..25088 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF (5 lower + 3 upper;
  first grep missed 250xx — re-ran, my pattern bug, no
  writer defect).
- boundary: 24832 CLOSED T10PNQ off=63 (prev tier intact);
  25089 "N out of scope" rc=2.
- verdict labels: R22 off=0/61/255 spots correct.
- consts non-vacuous: _T10R22M (m-tab NEW) + _T10R22C
  populated; q-tab reuses PNM per commit msg (no _T10R22Q),
  0 oracle violations across 256/256.

## verdict: PASS (T10R22 24833..25088 CLOSED 256/256)
