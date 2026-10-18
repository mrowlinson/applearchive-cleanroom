# VERIFY-b568b7a w2 T10R49 (n=34165..34484, +320, A+B shape): PASS

## first-hand (at-commit tree ver-b568b7a)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 34165..34484: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=34164 CLOSED T10P50B off=9; next N=34485
 rc=2 (out of scope).
- labels: T10R49A at 34165 (off=0); T10R49B at 34324
 (off=95), 34484 (off=255).
- consts: _T10R49AM _T10R49AQ _T10R49AC _T10R49BM _T10R49QH
 _T10R49BC non-vacuous (QH present, unlike R47/R48).

## verdict: PASS
