# VERIFY-0cda438 T10R39 30749..31004: PASS

## first-hand (at-commit tree ver-0cda438, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 30749..31004 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF (9 + 31004;
  first grep missed 31000+ — re-ran, my pattern bug, no
  writer defect).
- boundary: 30748 CLOSED T10P40Q off=63 (prev tier intact);
  31005 "N out of scope" rc=2.
- verdict labels: R39 off=0/61/255 spots correct.
- consts non-vacuous: _T10R39M (m-tab NEW) + _T10R39C
  populated; q-tab exact P40M reuse per commit msg (no
  _T10R39Q), 0 oracle violations across 256/256.

## verdict: PASS (T10R39 30749..31004 CLOSED 256/256)
