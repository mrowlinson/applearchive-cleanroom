# VERIFY-0c7b7fe w2 T10R41 (n=31445..31700, +256): PASS

## first-hand (at-commit tree ver-0c7b7fe)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 31445..31700: 256 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=31444 CLOSED T10P42Q off=63; next N=31701
 rc=2 (out of scope).
- labels: T10R41 at 31445 (off=0), 31572 (off=127), 31700
 (off=255).
- consts: _T10R41M multi-entry + _T10R41QH head + _T10R41C
 pair-table non-vacuous.

## verdict: PASS
