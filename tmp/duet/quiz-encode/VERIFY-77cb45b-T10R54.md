# VERIFY-77cb45b w2 T10R54 (n=35905..36224, +320, A+B shape): PASS

## first-hand (at-commit tree ver-77cb45b)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 35905..36224: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=35904 CLOSED T10P55B off=9; next N=36225
 rc=2 (out of scope).
- labels: T10R54A at 35905 (off=0); T10R54B at 36064
 (off=95), 36224 (off=255).
- consts: _T10R54AM _T10R54AQ _T10R54AC _T10R54BM _T10R54BC
 non-vacuous (no QH table).

## verdict: PASS
