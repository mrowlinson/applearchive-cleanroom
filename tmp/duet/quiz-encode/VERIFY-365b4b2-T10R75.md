# VERIFY-365b4b2 w2 T10R75 (n=43213..43532, +320, A+B shape): PASS

## first-hand (at-commit tree v-365b4b2)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5210 pins, 0 FAIL).
- own loop 43213..43532: 320 pass / 0 fail (fresh oracle each N).
- sha pins 26/26 MATCH in range.
- boundary: 43212 CLOSED T10P76B off=9 (prev tier); 43533
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 43213 CLOSED T10R75A off=0; 43276 CLOSED T10R75A
  off=63; 43277 CLOSED T10R75B off=0; 43532 CLOSED T10R75B
  off=255.
- consts _T10R75AM/AQ/AC/BM/BC at lines 11824-11893:
  AM16 w7 + AQ4 w9 + AC62 + BM16 w8 + BC63, all uniq,
  non-vacuous. B q=AM full (no BQ const, as committed).

## verdict: PASS
