# VERIFY-074bf0a w2 T10R44 (n=32489..32744, +256, first 80B): PASS

## first-hand (at-commit tree ver-074bf0a)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 32489..32744: 256 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=32488 CLOSED T10P45Q off=63; next N=32745
 rc=2 (out of scope).
- labels: T10R44 at 32489 (off=0), 32616 (off=127), 32744
 (off=255).
- consts: _T10R44M + _T10R44QH head-words + _T10R44C
 non-vacuous.

## verdict: PASS
