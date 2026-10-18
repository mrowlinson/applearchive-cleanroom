# VERIFY-29845bb w2 T10R69 (n=41125..41444, +320, A+B shape): PASS

## first-hand (at-commit tree ver-29845bb)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 41125..41444: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 41124 CLOSED T10P70B off=9 (prev tier); 41445
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 41125 CLOSED T10R69A off=0; 41188 CLOSED T10R69A
  off=63; 41300 CLOSED T10R69B off=111; 41444 CLOSED
  T10R69B off=255. A+B 320-wide shape; QH ABSENT this tier.
- consts _T10R69AM/AQ/AC/BM/BC at lines 11009-11065,
  non-vacuous (no QH table).

## verdict: PASS
