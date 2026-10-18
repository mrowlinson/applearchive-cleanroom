# VERIFY-8e0d740 T10R30 27617..27872: PASS

## first-hand (at-commit tree ver-8e0d740, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 27617..27872 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 27616 CLOSED T10PVQ off=63 (prev tier intact);
  27873 "N out of scope" rc=2.
- verdict labels: R30 off=0/61/255 spots correct.
- consts non-vacuous: _T10R30M (m-tab NEW) + _T10R30QH
  (q-head 2B) + _T10R30C populated; q = PVM-suffix +
  qhead per commit msg (partial CORE reuse, no full Q tab),
  0 oracle violations across 256/256.

## verdict: PASS (T10R30 27617..27872 CLOSED 256/256)
