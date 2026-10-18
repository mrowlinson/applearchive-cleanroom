# VERIFY-cc646bf w2 T10P51 (n=34485..34512, +28, short/no-Q): PASS

## first-hand (at-commit tree ver-cc646bf)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 34485..34512: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=34484 CLOSED T10R49B off=255; next N=34513
 rc=2 (out of scope).
- labels: T10P510 at 34485; T10P51A at 34498 (off=11);
 T10P51B at 34512 (off=9). No Q tier.
- consts: P510C P511C P51A P51AC P51B P51BC new,
 non-vacuous (no old-name collision for P51).

## verdict: PASS
