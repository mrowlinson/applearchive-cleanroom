# VERIFY-951dc3b w2 T10P76 (n=43185..43212, +28): PASS

## first-hand (at-commit tree v-951dc3b)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5184 pins, 0 FAIL).
- own loop 43185..43212: 28 pass / 0 fail (fresh oracle each N).
- sha pins 20/20 MATCH in range.
- boundary: 43184 CLOSED T10R74B off=255 (prev tier); 43213
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 43185 CLOSED T10P760 off=0; 43187 CLOSED T10P76A
  off=0; 43202 CLOSED T10P76A off=15; 43203 CLOSED T10P76B
  off=0; 43212 CLOSED T10P76B off=9.
- consts _T10P76S0/S1/AM/AC/BM/BC at lines 11762-11823:
  S0/S1 80B + AM16 w8 + AC70 + BM10 w10 + BC68, all uniq,
  non-vacuous.

## verdict: PASS
