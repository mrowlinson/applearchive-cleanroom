# VERIFY-9783bf5 T10P25 25437..25528: PASS

## first-hand (at-commit tree ver-9783bf5, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 25437..25528 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 25436 CLOSED T10R23 off=255 (prev tier intact);
  25529 "N out of scope" rc=2.
- verdict labels: PP0 25437 / PP1 25438 / PPA 25439 off=0 /
  PPB 25455 off=0 / PPQ 25465 off=0, 25528 off=63 — all
  correct tokens, letter P collision-free (A-O taken).
- consts non-vacuous: 10 _T10PP tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P25 25437..25528 CLOSED 92/92)
