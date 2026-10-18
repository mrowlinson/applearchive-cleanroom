# VERIFY-5832f8b w2 T10R51 (n=34861..35180, +320, A+B shape): PASS

## first-hand (at-commit tree ver-5832f8b)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 34861..35180: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=34860 CLOSED T10P52B off=9; next N=35181
 rc=2 (out of scope).
- labels: T10R51A at 34861 (off=0); T10R51B at 35020
 (off=95), 35180 (off=255).
- consts: _T10R51AM _T10R51AQ _T10R51AC _T10R51BM _T10R51QH
 _T10R51BC non-vacuous.

## verdict: PASS
