# VERIFY-911b25f w2 T10R68 (n=40777..41096, +320, A+B shape): PASS

## first-hand (at-commit tree ver-911b25f)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 40777..41096: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 40776 CLOSED T10P69B off=9 (prev tier); 41097
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 40777 CLOSED T10R68A off=0; 40840 CLOSED T10R68A
  off=63; 40950 CLOSED T10R68B off=109; 41096 CLOSED
  T10R68B off=255. A+B 320-wide shape; QH PRESENT this tier.
- consts _T10R68AM/AQ/AC/BM/QH/BC at lines 10858-10932,
  non-vacuous.

## verdict: PASS
