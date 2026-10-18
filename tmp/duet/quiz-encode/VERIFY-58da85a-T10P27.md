# VERIFY-58da85a T10P27 26133..26224: PASS

## first-hand (at-commit tree ver-58da85a, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 26133..26224 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 26132 CLOSED T10R25 off=255 (prev tier intact);
  26225 "N out of scope" rc=2.
- verdict labels: PR0 26133 / PR1 26134 / PRA 26135 off=0 /
  PRB 26151 off=0 / PRQ 26161 off=0, 26224 off=63 — all
  correct tokens, letter R collision-free (A-Q taken).
- consts non-vacuous: 9 _T10PR tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P27 26133..26224 CLOSED 92/92)
