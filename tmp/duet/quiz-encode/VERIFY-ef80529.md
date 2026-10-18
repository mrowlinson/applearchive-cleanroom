# VERIFY-ef80529 w2 T10P45 (n=32397..32488, +92): PASS

## first-hand (at-commit tree ver-ef80529)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 32397..32488: 92 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=32396 CLOSED T10R43 off=255; next N=32489
 GRAMMAR-BREAK paylen 80 rc=1 (80B-tier transition signal,
 first occurrence — R44 is the first 80B tier).
- labels: T10P450 at 32397; T10P45Q at 32442 (off=17), 32488
 (off=63).
- consts: P450C P451C P45A P45AC P45B P45BC P45M14 P45M25
 P45M P45Q P45QC present non-vacuous.

## verdict: PASS
