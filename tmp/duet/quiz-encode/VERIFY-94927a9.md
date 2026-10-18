# VERIFY-94927a9 w2 T10P50 (n=34137..34164, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-94927a9)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 34137..34164: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=34136 CLOSED T10R48B off=255; next N=34165
 rc=2 (out of scope).
- labels: T10P500 at 34137; T10P50A at 34150 (off=11);
 T10P50B at 34164 (off=9). No Q tier.
- consts: P500C P501C P50A P50AC P50B P50BC (97xx) new,
 non-vacuous. NOTE: `_T10P50C` at line 3993 is pre-existing
 (present in R48 parent tree — T10P5-era table, distinct
 name from new P500C); not new in this commit.

## verdict: PASS
