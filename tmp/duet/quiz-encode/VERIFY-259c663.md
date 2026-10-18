# VERIFY-259c663 w2 T10P53 (n=35181..35208, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-259c663)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 35181..35208: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=35180 CLOSED T10R51B off=255; next N=35209
 rc=2 (out of scope).
- labels: T10P530 at 35181 (off=0); T10P53A at 35194
 (off=11); T10P53B at 35208 (off=9). No Q tier.
- consts: P53S0 P53S1 P53AM P53AC P53BM P53BC new,
 non-vacuous (new shape: S-singletons + AM/AC/BM/BC).

## verdict: PASS
