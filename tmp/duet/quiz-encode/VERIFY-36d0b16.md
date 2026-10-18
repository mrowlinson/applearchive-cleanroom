# VERIFY-36d0b16 w2 T10P59 (n=37269..37296, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-36d0b16)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 37269..37296: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=37268 CLOSED T10R57B off=255; next N=37297
 rc=2 (out of scope).
- labels: T10P590 at 37269 (off=0); T10P59A at 37282
 (off=11); T10P59B at 37296 (off=9). No Q tier.
- consts: P59S0 P59S1 P59AM P59AC P59BM P59BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
