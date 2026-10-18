# VERIFY-0b783f8 w2 T10P54 (n=35529..35556, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-0b783f8)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 35529..35556: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=35528 CLOSED T10R52B off=255; next N=35557
 rc=2 (out of scope).
- labels: T10P540 at 35529 (off=0); T10P54A at 35542
 (off=11); T10P54B at 35556 (off=9). No Q tier.
- consts: P54S0 P54S1 P54AM P54AC P54BM P54BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
