# VERIFY-47eb5fa T10P41 31005..31096: PASS

## first-hand (at-commit tree ver-47eb5fa, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 31005..31096 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF (exhaustive awk
  range filter).
- boundary: 31004 CLOSED T10R39 off=255 (prev tier intact);
  31097 "N out of scope" rc=2.
- verdict labels: P410 31005 / P411 31006 / P41A 31007 off=0 /
  P41B 31023 off=0 / P41Q 31033 off=0, 31096 off=63 — all
  correct tokens (numeric scheme).
- consts non-vacuous: 9 _T10P41 tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P41 31005..31096 CLOSED 92/92)
