# VERIFY-3917ba1 w2 T10P62 (n=38313..38340, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-3917ba1)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 38313..38340: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=38312 CLOSED T10R60B off=255; next N=38341
 rc=2 (out of scope).
- labels: T10P620 at 38313 (off=0); T10P62A at 38326
 (off=11); T10P62B at 38340 (off=9). No Q tier.
- consts: P62S0 P62S1 P62AM P62AC P62BM P62BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
