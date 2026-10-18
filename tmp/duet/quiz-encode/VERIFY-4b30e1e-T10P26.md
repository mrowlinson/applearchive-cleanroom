# VERIFY-4b30e1e T10P26 25785..25876: PASS

## first-hand (at-commit tree ver-4b30e1e, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN.
- FULL battery 25785..25876 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 25784 CLOSED T10R24 off=255 (prev tier intact);
  25877 "N out of scope" rc=2.
- verdict labels: PQ0 25785 / PQ1 25786 / PQA 25787 off=0 /
  PQB 25803 off=0 / PQQ 25813 off=0, 25876 off=63 — all
  correct tokens, letter Q collision-free (A-P taken).
- consts non-vacuous: 9 _T10PQ tables populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P26 25785..25876 CLOSED 92/92)
