# VERIFY-d3afa19 T10R23 25181..25436: PASS

## first-hand (at-commit tree ver-d3afa19, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 25181..25436 (256/256, own loop, fresh
  compression_tool bytes): pass=256 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 8 pin
  rows in range, 8/8 MATCH, 0 SHADIFF.
- boundary: 25180 CLOSED T10POQ off=63 (prev tier intact);
  25437 "N out of scope" rc=2.
- verdict labels: R23 off=0/61/255 spots correct.
- consts non-vacuous: _T10R23M (8B m-tab) + _T10R23Q (6B
  q-tab) + _T10R23C populated, 0 oracle violations across
  256/256. (Q-38 reuse question: separate A-45 derivation.)

## verdict: PASS (T10R23 25181..25436 CLOSED 256/256)
