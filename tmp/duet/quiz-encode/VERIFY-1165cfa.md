# VERIFY-1165cfa w2 T10P58 (n=36921..36948, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-1165cfa)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 36921..36948: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=36920 CLOSED T10R56B off=255; next N=36949
 rc=2 (out of scope).
- labels: T10P580 at 36921 (off=0); T10P58A at 36934
 (off=11); T10P58B at 36948 (off=9). No Q tier.
- consts: P58S0 P58S1 P58AM P58AC P58BM P58BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
