# VERIFY-804eb41 w2 T10R46 (n=33185..33440, +256): PASS

## first-hand (at-commit tree ver-804eb41)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 33185..33440: 256 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=33184 CLOSED T10P47Q off=63; next N=33441
 rc=2 (out of scope).
- labels: T10R46 at 33185 (off=0), 33312 (off=127), 33440
 (off=255).
- consts: _T10R46M + _T10R46C non-vacuous (no QH table).

## verdict: PASS
