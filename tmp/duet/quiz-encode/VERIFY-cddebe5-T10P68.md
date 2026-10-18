# VERIFY-cddebe5 w2 T10P68 (n=40401..40428, +28): PASS

## first-hand (at-commit tree ver-cddebe5)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 40401..40428: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: 40400 CLOSED T10R66B off=255 (prev tier); 40429
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 40401 CLOSED T10P680 off=0; 40414 CLOSED T10P68A
  off=11; 40428 CLOSED T10P68B off=9.
- consts _T10P68S0/S1/AM/AC/BM/BC at lines 10663-10711,
  S0/S1 + AM/AC/BM/BC shape, non-vacuous.

## verdict: PASS
