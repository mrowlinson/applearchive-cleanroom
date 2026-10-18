# VERIFY-004a2c2 T10R29 27269..27524: PASS

## first-hand (at-commit tree ver-004a2c2, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 27269..27524 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF (loop covered 13 incl
  5 P30-tail, all MATCH — over-wide pattern, no writer defect).
- boundary: 27268 CLOSED T10PUQ off=63 (prev tier intact);
  27525 "N out of scope" rc=2.
- verdict labels: R29 off=0/61/255 spots correct.
- consts non-vacuous: _T10R29M (m-tab NEW) + _T10R29B5
  (b5-mtab) + _T10R29C populated; q-tab reuses PUM per
  commit msg (no _T10R29Q), 0 oracle violations across 256/256.

## verdict: PASS (T10R29 27269..27524 CLOSED 256/256)
