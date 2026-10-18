# VERIFY-838cde4 w2 T10R48 (n=33817..34136, +320, A+B shape): PASS

## first-hand (at-commit tree ver-838cde4)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 33817..34136: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=33816 CLOSED T10P49B off=9; next N=34137
 rc=2 (out of scope).
- labels: T10R48A at 33817 (off=0); T10R48B at 33976
 (off=95), 34136 (off=255).
- consts: _T10R48AM _T10R48AQ _T10R48AC _T10R48BM _T10R48BC
 non-vacuous.

## verdict: PASS
