# VERIFY-b8230b7 w2 T10R50 (n=34513..34832, +320, A+B shape): PASS

## first-hand (at-commit tree ver-b8230b7)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 34513..34832: 320 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=34512 CLOSED T10P51B off=9; next N=34833
 rc=2 (out of scope).
- labels: T10R50A at 34513 (off=0); T10R50B at 34672
 (off=95), 34832 (off=255).
- consts: _T10R50AM _T10R50QB40 _T10R50AQ _T10R50AC _T10R50BM
 _T10R50QH _T10R50BC non-vacuous (QB40 + QH present).

## verdict: PASS
