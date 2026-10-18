# VERIFY-b69a027 w2 T10P65 (n=39357..39384, +28): PASS

## first-hand (at-commit tree ver-b69a027)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 39357..39384: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: 39356 CLOSED T10R63B off=255 (prev tier); 39385
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 39357 CLOSED T10P650 off=0; 39370 CLOSED T10P65A
  off=11; 39384 CLOSED T10P65B off=9.
- consts _T10P65S0/S1/AM/AC/BM/BC at lines 10265-10312,
  S0/S1 + AM/AC/BM/BC shape, non-vacuous.

## verdict: PASS
