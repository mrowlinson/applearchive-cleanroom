# VERIFY-648ac73 w2 T10P57 (n=36573..36600, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-648ac73)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 36573..36600: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=36572 CLOSED T10R55B off=255; next N=36601
 rc=2 (out of scope).
- labels: T10P570 at 36573 (off=0); T10P57A at 36586
 (off=11); T10P57B at 36600 (off=9). No Q tier.
- consts: P57S0 P57S1 P57AM P57AC P57BM P57BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
