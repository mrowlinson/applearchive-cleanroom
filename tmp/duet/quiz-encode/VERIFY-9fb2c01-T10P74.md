# VERIFY-9fb2c01 w2 T10P74 (n=42489..42516, +28): PASS

## first-hand (at-commit tree v-9fb2c01)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5092 pins, 0 FAIL).
- own loop 42489..42516: 28 pass / 0 fail (fresh oracle each N).
- sha pins 20/20 MATCH in range.
- boundary: 42488 CLOSED T10R72B off=255 (prev tier); 42517
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 42489 CLOSED T10P740 off=0; 42491 CLOSED T10P74A
  off=0; 42506 CLOSED T10P74A off=15; 42507 CLOSED T10P74B
  off=0; 42516 CLOSED T10P74B off=9.
- consts _T10P74S0/S1/AM/AC/BM/BC at lines 11496-11557:
  S0/S1 80B + AM16 w8 + AC70 + BM10 w11 + BC67, all uniq,
  non-vacuous.

## verdict: PASS
