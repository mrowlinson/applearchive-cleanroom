# VERIFY-a6bf95f w2 T10P69 (n=40749..40776, +28): PASS

## first-hand (at-commit tree ver-a6bf95f)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 40749..40776: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: 40748 CLOSED T10R67B off=255 (prev tier); 40777
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 40749 CLOSED T10P690 off=0; 40762 CLOSED T10P69A
  off=11; 40776 CLOSED T10P69B off=9.
- consts _T10P69S0/S1/AM/AC/BM/BC at lines 10796-10844,
  S0/S1 + AM/AC/BM/BC shape, non-vacuous.

## verdict: PASS
