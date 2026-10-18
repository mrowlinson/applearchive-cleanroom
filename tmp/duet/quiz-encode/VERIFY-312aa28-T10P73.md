# VERIFY-312aa28 w2 T10P73 (n=42141..42168, +28): PASS

## first-hand (at-commit tree ver-312aa28)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 42141..42168: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: 42140 CLOSED T10R71B off=255 (prev tier); 42169
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 42141 CLOSED T10P730 off=0; 42154 CLOSED T10P73A
  off=11; 42168 CLOSED T10P73B off=9.
- consts _T10P73S0/S1/AM/AC/BM/BC at lines 11364-11412,
  S0/S1 + AM/AC/BM/BC shape, non-vacuous.

## verdict: PASS
