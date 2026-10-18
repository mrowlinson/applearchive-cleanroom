# VERIFY-5e0909c w2 T10P63 (n=38661..38688, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-5e0909c)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 38661..38688: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=38660 CLOSED T10R61B off=255; next N=38689
 rc=2 (out of scope).
- labels: T10P630 at 38661 (off=0); T10P63A at 38674
 (off=11); T10P63B at 38688 (off=9). No Q tier.
- consts: P63S0 P63S1 P63AM P63AC P63BM P63BC new,
 non-vacuous (S-singletons + AM/AC/BM/BC shape).

## verdict: PASS
