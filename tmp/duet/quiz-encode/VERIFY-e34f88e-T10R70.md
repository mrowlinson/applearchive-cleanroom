# VERIFY-e34f88e w2 T10R70 (n=41473..41792, +320, A+B shape): PASS

## first-hand (at-commit tree ver-e34f88e)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 41473..41792: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 41472 CLOSED T10P71B off=9 (prev tier); 41793
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 41473 CLOSED T10R70A off=0; 41536 CLOSED T10R70A
  off=63; 41650 CLOSED T10R70B off=113; 41792 CLOSED
  T10R70B off=255. A+B 320-wide shape; QH ABSENT this tier.
- consts _T10R70AM/AQ/AC/BM/BC at lines 11142-11198,
  non-vacuous (no QH table).

## verdict: PASS
