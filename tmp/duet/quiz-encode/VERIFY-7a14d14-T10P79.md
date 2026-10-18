# VERIFY-7a14d14 w2 T10P79 (n=44229..44256, +28): PASS

## first-hand (at-commit tree v-7a14d14)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5322 pins, 0 FAIL).
- own loop 44229..44256: 28 pass / 0 fail (fresh oracle each N).
- sha pins 20/20 MATCH in range.
- boundary: 44228 CLOSED T10R77B off=255 (prev tier); 44257
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 44229 CLOSED T10P790 off=0; 44231 CLOSED T10P79A
  off=0; 44246 CLOSED T10P79A off=15; 44247 CLOSED T10P79B
  off=0; 44256 CLOSED T10P79B off=9.
- consts _T10P79S0/S1/AM/AC/BM/BC at lines 12161-12223:
  S0/S1 80B + AM16 w7 + AC72 + BM10 w10 + BC69, all uniq,
  non-vacuous, FULL-80 both, no tab/const overlap.
- OBSERVED (NOTE-1093): commit-note prose lists wrong tab
  positions (copied from P77). Code matches oracle sweep
  exactly (A varies b13-15,72-75; B varies b13-18,76-79;
  B sig uniform e1790100). Note text only, no code defect.

## verdict: PASS
