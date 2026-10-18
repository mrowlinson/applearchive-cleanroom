# VERIFY-cf113e3 w2 T10R42 (n=31793..32048, +256): PASS

## first-hand (at-commit tree ver-cf113e3)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 31793..32048: 256 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=31792 CLOSED T10P43Q off=63; next N=32049
 rc=2 (out of scope).
- labels: T10R42 at 31793 (off=0), 31920 (off=127), 32048
 (off=255).
- consts: _T10R42M multi-entry + _T10R42QH head-words +
 _T10R42C pair-table non-vacuous.

## verdict: PASS
