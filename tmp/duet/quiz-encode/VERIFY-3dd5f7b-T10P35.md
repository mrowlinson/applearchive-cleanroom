# VERIFY-3dd5f7b T10P35 28917..29008: PASS

## first-hand (at-commit tree ver-3dd5f7b, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 28917..29008 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF (9 + 29008;
  first grep missed 29008 — re-ran, my pattern bug, no
  writer defect).
- boundary: 28916 CLOSED T10R33 off=255 (prev tier intact);
  29009 "N out of scope" rc=2.
- verdict labels: PZ0 28917 / PZ1 28918 / PZA 28919 off=0 /
  PZB 28935 off=0 / PZQ 28945 off=0, 29008 off=63 — all
  correct tokens, letter Z collision-free (A-Y taken;
  alphabet exhausted, next P-head goes numeric).
- consts non-vacuous: 9 _T10PZ tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P35 28917..29008 CLOSED 92/92)
