# VERIFY-a9ac228 w2 T10R66 (n=40081..40400, +320, A+B shape): PASS

## first-hand (at-commit tree ver-a9ac228)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 40081..40400: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 40080 CLOSED T10P67B off=9 (prev tier); 40401
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 40081 CLOSED T10R66A off=0; 40144 CLOSED T10R66A
  off=63; 40300 CLOSED T10R66B off=155; 40400 CLOSED
  T10R66B off=255. A+B 320-wide shape; QH ABSENT this tier.
- consts _T10R66AM/AQ/AC/BM/BC at lines 10593-10649,
  non-vacuous (no QH table).

## verdict: PASS
