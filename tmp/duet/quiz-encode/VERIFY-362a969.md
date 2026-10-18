# VERIFY-362a969 w2 T10P55 (n=35877..35904, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-362a969)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 35877..35904: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=35876 CLOSED T10R53B off=255; next N=35905
 rc=2 (out of scope).
- labels: T10P550 at 35877 (off=0); T10P55A at 35890
 (off=11); T10P55B at 35904 (off=9). No Q tier.
- consts: P55S0 P55S1 P55AM P55AC P55BM P55BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
