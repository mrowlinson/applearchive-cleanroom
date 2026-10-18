# VERIFY-8da8428 T10P33 28221..28312: PASS

## first-hand (at-commit tree ver-8da8428, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 28221..28312 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 28220 CLOSED T10R31 off=255 (prev tier intact);
  28313 "N out of scope" rc=2.
- verdict labels: PX0 28221 / PX1 28222 / PXA 28223 off=0 /
  PXB 28239 off=0 / PXQ 28249 off=0, 28312 off=63 — all
  correct tokens, letter X collision-free (A-W taken).
- consts non-vacuous: 9 _T10PX tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P33 28221..28312 CLOSED 92/92)
