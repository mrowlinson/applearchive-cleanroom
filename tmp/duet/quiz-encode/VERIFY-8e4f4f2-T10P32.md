# VERIFY-8e4f4f2 T10P32 27873..27964: PASS

## first-hand (at-commit tree ver-8e4f4f2, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 27873..27964 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 27872 CLOSED T10R30 off=255 (prev tier intact);
  27965 "N out of scope" rc=2.
- verdict labels: PW0 27873 / PW1 27874 / PWA 27875 off=0 /
  PWB 27891 off=0 / PWQ 27901 off=0, 27964 off=63 — all
  correct tokens, letter W collision-free (A-V taken).
- consts non-vacuous: 9 _T10PW tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P32 27873..27964 CLOSED 92/92)
