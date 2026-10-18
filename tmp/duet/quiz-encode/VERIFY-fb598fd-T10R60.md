# VERIFY-fb598fd w2 T10R60 (n=37993..38312, +320, A+B shape): PASS

## first-hand (at-commit tree ver-fb598fd)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 37993..38312: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=37992 CLOSED T10P61B off=9; next N=38313
 rc=2 (out of scope).
- labels: T10R60A at 37993 (off=0); T10R60B at 38152
 (off=95), 38312 (off=255).
- consts: _T10R60AM _T10R60AQ _T10R60AC _T10R60BM _T10R60BC
 non-vacuous (no QH table).

## verdict: PASS
