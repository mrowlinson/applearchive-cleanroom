# VERIFY-3e687c6 w2 T10R53 (n=35557..35876, +320, A+B shape): PASS

## first-hand (at-commit tree ver-3e687c6)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 35557..35876: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=35556 CLOSED T10P54B off=9; next N=35877
 rc=2 (out of scope).
- labels: T10R53A at 35557 (off=0); T10R53B at 35716
 (off=95), 35876 (off=255).
- consts: _T10R53AM _T10R53AQ _T10R53AC _T10R53BM _T10R53BC
 non-vacuous (no QH table).

## verdict: PASS
