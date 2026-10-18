# VERIFY-11cfc70 T10R25 25877..26132: PASS

## first-hand (at-commit tree ver-11cfc70, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 25877..26132 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF (4 + 4; first grep
  missed 26000+ — re-ran, my pattern bug, no writer defect).
- boundary: 25876 CLOSED T10PQQ off=63 (prev tier intact);
  26133 "N out of scope" rc=2.
- verdict labels: R25 off=0/61/255 spots correct.
- consts non-vacuous: _T10R25M (m-tab NEW) + _T10R25C
  populated; q-tab reuses PQM per commit msg (no _T10R25Q),
  0 oracle violations across 256/256.

## verdict: PASS (T10R25 25877..26132 CLOSED 256/256)
