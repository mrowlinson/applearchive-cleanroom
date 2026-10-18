# VERIFY-1492d3a T10P28 26481..26572: PASS

## first-hand (at-commit tree ver-1492d3a, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 26481..26572 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 26480 CLOSED T10R26 off=255 (prev tier intact);
  26573 "N out of scope" rc=2.
- verdict labels: PS0 26481 / PS1 26482 / PSA 26483 off=0 /
  PSB 26499 off=0 / PSQ 26509 off=0, 26572 off=63 — all
  correct tokens, letter S collision-free (A-R taken).
- consts non-vacuous: 9 _T10PS tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P28 26481..26572 CLOSED 92/92)
