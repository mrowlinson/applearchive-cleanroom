# VERIFY-3dfc862 w2 T10R56 (n=36601..36920, +320, A+B shape): PASS

## first-hand (at-commit tree ver-3dfc862)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 36601..36920: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=36600 CLOSED T10P57B off=9; next N=36921
 rc=2 (out of scope).
- labels: T10R56A at 36601 (off=0); T10R56B at 36760
 (off=95), 36920 (off=255).
- consts: _T10R56AM _T10R56AQ _T10R56AC _T10R56BM _T10R56BC
 non-vacuous (no QH table).

## verdict: PASS
