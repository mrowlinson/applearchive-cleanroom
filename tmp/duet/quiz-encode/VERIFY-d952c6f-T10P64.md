# VERIFY-d952c6f w2 T10P64 (n=39009..39036, +28): PASS

## first-hand (at-commit tree ver-d952c6f)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 39009..39036: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: 39008 CLOSED T10R62B off=255 (prev tier); 39037
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 39009 CLOSED T10P640 off=0; 39022 CLOSED T10P64A
  off=11; 39036 CLOSED T10P64B off=9.
- consts _T10P64S0/S1/AM/AC/BM/BC at lines 10134-10179,
  S0/S1 + AM/AC/BM/BC shape, non-vacuous.

## verdict: PASS
