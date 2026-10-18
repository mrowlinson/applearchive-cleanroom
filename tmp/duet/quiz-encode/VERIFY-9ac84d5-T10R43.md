# VERIFY-9ac84d5 w2 T10R43 (n=32141..32396, +256): PASS

## first-hand (at-commit tree ver-9ac84d5)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 32141..32396: 256 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=32140 CLOSED T10P44Q off=63; next N=32397
 rc=2 (out of scope).
- labels: T10R43 at 32141 (off=0), 32268 (off=127), 32396
 (off=255).
- consts: _T10R43M + _T10R43C non-vacuous (no QH table —
 tier shape differs from R41/R42).

## verdict: PASS
