# VERIFY-25b36b0 w2 T10P43 (n=31701..31792, +92): PASS

## first-hand (at-commit tree ver-25b36b0)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 31701..31792: 92 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=31700 CLOSED T10R41 off=255; next N=31793
 rc=2 (out of scope).
- labels: T10P430 at 31701; T10P43Q at 31746 (off=17), 31792
 (off=63).
- consts: P430C P431C P43A P43AC P43B P43BC P43M P43Q P43QC
 present non-vacuous (no P43MB — tier shape differs from P42).

## verdict: PASS
