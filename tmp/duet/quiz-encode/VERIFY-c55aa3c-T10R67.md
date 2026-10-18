# VERIFY-c55aa3c w2 T10R67 (n=40429..40748, +320, A+B shape): PASS

## first-hand (at-commit tree ver-c55aa3c)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 40429..40748: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 40428 CLOSED T10P68B off=9 (prev tier); 40749
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 40429 CLOSED T10R67A off=0; 40492 CLOSED T10R67A
  off=63; 40600 CLOSED T10R67B off=107; 40748 CLOSED
  T10R67B off=255. A+B 320-wide shape; QH ABSENT this tier.
- consts _T10R67AM/AQ/AC/BM/BC at lines 10726-10782,
  non-vacuous (no QH table).

## verdict: PASS
