# VERIFY-b5a223f w2 T10R52 (n=35209..35528, +320, A+B shape): PASS

## first-hand (at-commit tree ver-b5a223f)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 35209..35528: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=35208 CLOSED T10P53B off=9; next N=35529
 rc=2 (out of scope).
- labels: T10R52A at 35209 (off=0); T10R52B at 35368
 (off=95), 35528 (off=255).
- consts: _T10R52AM _T10R52AQ _T10R52AC _T10R52BM _T10R52BC
 non-vacuous (no QH table).

## verdict: PASS
