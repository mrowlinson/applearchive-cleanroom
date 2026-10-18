# VERIFY-ea1b509 w2 T10P44 (n=32049..32140, +92): PASS

## first-hand (at-commit tree ver-ea1b509)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 32049..32140: 92 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=32048 CLOSED T10R42 off=255; next N=32141
 rc=2 (out of scope).
- labels: T10P440 at 32049; T10P44Q at 32094 (off=17), 32140
 (off=63).
- consts: P440C P441C P44A P44AC P44B P44BC P44M P44Q P44QC
 present non-vacuous.

## verdict: PASS
