# VERIFY-012efda w2 T10R64 (n=39385..39704, +320, A+B shape): PASS

## first-hand (at-commit tree ver-012efda)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 39385..39704: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 39384 CLOSED T10P65B off=9 (prev tier); 39705
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 39385 CLOSED T10R64A off=0; 39448 CLOSED T10R64A
  off=63; 39600 CLOSED T10R64B off=151; 39704 CLOSED
  T10R64B off=255. A+B 320-wide shape; QH ABSENT this tier.
- consts _T10R64AM/AQ/AC/BM/BC at lines 10327-10383,
  non-vacuous (no QH table).

## verdict: PASS
