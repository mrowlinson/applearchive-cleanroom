# VERIFY-f43ec6a T10P37 29613..29704: PASS

## first-hand (at-commit tree ver-f43ec6a, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 29613..29704 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 29612 CLOSED T10R35 off=255 (prev tier intact);
  29705 "N out of scope" rc=2.
- verdict labels: P370 29613 / P371 29614 / P37A 29615 off=0 /
  P37B 29631 off=0 / P37Q 29641 off=0, 29704 off=63 — all
  correct tokens (numeric scheme).
- consts non-vacuous: 9 _T10P37 tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P37 29613..29704 CLOSED 92/92)
