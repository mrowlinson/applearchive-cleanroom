# VERIFY-599f93c w2 T10R59 (n=37645..37964, +320, A+B shape): PASS

## first-hand (at-commit tree ver-599f93c)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 37645..37964: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=37644 CLOSED T10P60B off=9; next N=37965
 rc=2 (out of scope).
- labels: T10R59A at 37645 (off=0); T10R59B at 37804
 (off=95), 37964 (off=255).
- consts: _T10R59AM _T10R59AQ _T10R59AC _T10R59BM _T10R59BC
 non-vacuous (no QH table).

## verdict: PASS
