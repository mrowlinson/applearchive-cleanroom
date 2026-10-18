# VERIFY-4b20deb w2 T10R65 (n=39733..40052, +320, A+B shape): PASS

## first-hand (at-commit tree ver-4b20deb)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 39733..40052: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 39732 CLOSED T10P66B off=9 (prev tier); 40053
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 39733 CLOSED T10R65A off=0; 39800 CLOSED T10R65B
  off=3; 39950 CLOSED T10R65B off=153; 40052 CLOSED
  T10R65B off=255. A+B 320-wide shape, short A-block;
  QH ABSENT this tier.
- consts _T10R65AM/AQ/AC/BM/BC at lines 10461-10517,
  non-vacuous (no QH table).

## verdict: PASS
