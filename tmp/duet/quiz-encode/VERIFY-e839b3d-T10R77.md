# VERIFY-e839b3d w2 T10R77 (n=43909..44228, +320, A+B shape): PASS

## first-hand (at-commit tree v-e839b3d)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5302 pins, 0 FAIL).
- own loop 43909..44228: 320 pass / 0 fail (fresh oracle each N).
- sha pins 26/26 MATCH in range.
- boundary: 43908 CLOSED T10P78B off=9 (prev tier); 44229
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 43909 CLOSED T10R77A off=0; 43972 CLOSED T10R77A
  off=63; 43973 CLOSED T10R77B off=0; 44228 CLOSED T10R77B
  off=255.
- consts _T10R77AM/AQ/AC/BM/BC at lines 12091-12160:
  AM16 w8 + AQ4 w10 + AC61 + BM16 w6 + BC64, all uniq,
  non-vacuous. B q=AM full (no BQ const, as committed).

## verdict: PASS
