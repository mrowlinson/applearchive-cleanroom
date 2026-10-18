# VERIFY-f949df5 T10P22 24393..24484: PASS

## first-hand (at-commit tree ver-f949df5, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z24484-closed, PASS g-z24484).
- FULL battery 24393..24484 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 10 pin
  rows in range, 10/10 MATCH, 0 SHADIFF.
- boundary: 24392 CLOSED T10R20 off=255 (prev tier intact);
  24485 "N out of scope" rc=2.
- verdict labels: PM0 24393 / PM1 24394 / PMA 24395 off=0 /
  PMB 24411 off=0 / PMQ 24421 off=0, 24484 off=63 — all
  correct tokens, letter M collision-free (A-L taken).
- consts non-vacuous: 9 _T10PM tables (no PM32 rule this quad) populated, 0 oracle
  violations across 92/92.

## verdict: PASS (T10P22 24393..24484 CLOSED 92/92)
