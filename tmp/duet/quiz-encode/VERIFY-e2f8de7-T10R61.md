# VERIFY-e2f8de7 w2 T10R61 (n=38341..38660, +320, A+B shape): PASS

## first-hand (at-commit tree ver-e2f8de7)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 38341..38660: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=38340 CLOSED T10P62B off=9; next N=38661
 rc=2 (out of scope).
- labels: T10R61A at 38341 (off=0); T10R61B at 38500
 (off=95), 38660 (off=255).
- consts: _T10R61AM _T10R61AQ _T10R61AC _T10R61BM _T10R61BC
 non-vacuous (no QH table).

## verdict: PASS
