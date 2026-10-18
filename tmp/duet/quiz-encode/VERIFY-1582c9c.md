# VERIFY-1582c9c w2 T10P56 (n=36225..36252, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-1582c9c)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 36225..36252: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=36224 CLOSED T10R54B off=255; next N=36253
 rc=2 (out of scope).
- labels: T10P560 at 36225 (off=0); T10P56A at 36238
 (off=11); T10P56B at 36252 (off=9). No Q tier.
- consts: P56S0 P56S1 P56AM P56AC P56BM P56BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
