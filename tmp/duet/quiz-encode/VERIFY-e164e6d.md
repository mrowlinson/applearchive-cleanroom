# VERIFY-e164e6d w2 T10P46 (n=32745..32836, +92): PASS

## first-hand (at-commit tree ver-e164e6d)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 32745..32836: 92 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: prev N=32744 CLOSED T10R44 off=255; next N=32837
 rc=2 (out of scope).
- labels: T10P460 at 32745; T10P46Q at 32790 (off=17), 32836
 (off=63).
- consts: P460C P461C P46A P46AC P46B1 P46B1C P46B2 P46B2C
 P46M32 P46M P46Q P46QC present non-vacuous (B1/B2 split).

## verdict: PASS
