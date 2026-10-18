# VERIFY-43e6d43 w2 T10P60 (n=37617..37644, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-43e6d43)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 37617..37644: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=37616 CLOSED T10R58B off=255; next N=37645
 rc=2 (out of scope).
- labels: T10P600 at 37617 (off=0); T10P60A at 37630
 (off=11); T10P60B at 37644 (off=9). No Q tier.
- consts: P60S0 P60S1 P60AM P60AC P60BM P60BC (101xx) new,
 non-vacuous. NOTE: `_T10P60C` at line 4075 is pre-existing
 (present in R58 parent tree — T10P6-era table, distinct
 name from new P600C/S0); not new in this commit.

## verdict: PASS
