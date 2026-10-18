# VERIFY-1b1e2f3 T10P38 29961..30052: PASS

## first-hand (at-commit tree ver-1b1e2f3, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 29961..30052 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 29960 CLOSED T10R36 off=255 (prev tier intact);
  30053 "N out of scope" rc=2.
- verdict labels: P380 29961 / P381 29962 / P38A 29963 off=0 /
  P38B 29979 off=0 / P38Q 29989 off=0, 30052 off=63 — all
  correct tokens (numeric scheme).
- consts non-vacuous: 10 _T10P38 tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P38 29961..30052 CLOSED 92/92)
