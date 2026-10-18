# VERIFY-29272cc w2 T10R45 (n=32837..33092, +256): PASS

## first-hand (at-commit tree ver-29272cc)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 32837..33092: 256 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=32836 CLOSED T10P46Q off=63; next N=33093
 rc=2 (out of scope).
- labels: T10R45 at 32837 (off=0), 32964 (off=127), 33092
 (off=255).
- consts: _T10R45M + _T10R45QH head-words + _T10R45C
 non-vacuous.

## verdict: PASS
