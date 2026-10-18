# VERIFY-3ea1405 w2 T10R55 (n=36253..36572, +320, A+B shape): PASS

## first-hand (at-commit tree ver-3ea1405)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 36253..36572: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=36252 CLOSED T10P56B off=9; next N=36573
 rc=2 (out of scope).
- labels: T10R55A at 36253 (off=0); T10R55B at 36412
 (off=95), 36572 (off=255).
- consts: _T10R55AM _T10R55AQ _T10R55AC _T10R55BM _T10R55QH
 _T10R55BC non-vacuous (QH present).

## verdict: PASS
