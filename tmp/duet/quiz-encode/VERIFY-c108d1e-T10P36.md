# VERIFY-c108d1e T10P36 29265..29356: PASS

## first-hand (at-commit tree ver-c108d1e, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 29265..29356 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 29264 CLOSED T10R34 off=255 (prev tier intact);
  29357 "N out of scope" rc=2.
- verdict labels: P360 29265 / P361 29266 / P36A 29267 off=0 /
  P36B 29283 off=0 / P36Q 29293 off=0, 29356 off=63 — all
  correct tokens. NUMERIC head scheme (A-Z exhausted at P35).
- consts non-vacuous: 9 _T10P36 tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P36 29265..29356 CLOSED 92/92)
