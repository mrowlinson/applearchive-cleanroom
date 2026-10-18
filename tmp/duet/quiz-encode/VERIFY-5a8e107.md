# VERIFY-5a8e107 w2 T10P61 (n=37965..37992, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-5a8e107)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 37965..37992: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=37964 CLOSED T10R59B off=255; next N=37993
 rc=2 (out of scope).
- labels: T10P610 at 37965 (off=0); T10P61A at 37978
 (off=11); T10P61B at 37992 (off=9). No Q tier.
- consts: P61S0 P61S1 P61AM P61AC P61BM P61BC (101xx) new,
 non-vacuous. NOTE: `_T10P61C` at line 4090 is pre-existing
 (present in R59 parent tree — T10P6-era table, distinct
 name from new S0/S1); not new in this commit.

## verdict: PASS
