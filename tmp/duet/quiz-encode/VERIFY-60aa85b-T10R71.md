# VERIFY-60aa85b w2 T10R71 (n=41821..42140, +320, A+B shape): PASS

## first-hand (at-commit tree ver-60aa85b)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 41821..42140: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 41820 CLOSED T10P72B off=9 (prev tier); 42141
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 41821 CLOSED T10R71A off=0; 41884 CLOSED T10R71A
  off=63; 42000 CLOSED T10R71B off=115; 42140 CLOSED
  T10R71B off=255. A+B 320-wide shape; QH PRESENT this tier.
- consts _T10R71AM/AQ/AC/BM/QH/BC at lines 11275-11350,
  non-vacuous.

## verdict: PASS
