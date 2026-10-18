# VERIFY-34f853f T10R36 29705..29960: PASS

## first-hand (at-commit tree ver-34f853f, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 29705..29960 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 29704 CLOSED T10P37Q off=63 (prev tier intact);
  29961 "N out of scope" rc=2.
- verdict labels: R36 off=0/61/255 spots correct.
- consts non-vacuous: _T10R36M (m-tab NEW) + _T10R36QH
  (q-head) + _T10R36C populated; q = P37M-tail + qhead
  per commit msg (partial TAIL reuse, no full Q tab),
  0 oracle violations across 256/256.

## verdict: PASS (T10R36 29705..29960 CLOSED 256/256)
