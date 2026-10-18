# VERIFY-55dcb98 T10P40 30657..30748: PASS

## first-hand (at-commit tree ver-55dcb98, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 30657..30748 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 30656 CLOSED T10R38 off=255 (prev tier intact);
  30749 "N out of scope" rc=2.
- verdict labels: P400 30657 / P401 30658 / P40A 30659 off=0 /
  P40B 30675 off=0 / P40Q 30685 off=0, 30748 off=63 — all
  correct tokens (numeric scheme).
- consts non-vacuous: 10 _T10P40 tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P40 30657..30748 CLOSED 92/92)
