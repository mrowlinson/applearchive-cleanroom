# VERIFY-795f3f8 w2 T10R76 (n=43561..43880, +320, A+B shape): PASS

## first-hand (at-commit tree v-795f3f8)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5256 pins, 0 FAIL).
- own loop 43561..43880: 320 pass / 0 fail (fresh oracle each N).
- sha pins 26/26 MATCH in range.
- boundary: 43560 CLOSED T10P77B off=9 (prev tier); 43881
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 43561 CLOSED T10R76A off=0; 43624 CLOSED T10R76A
  off=63; 43625 CLOSED T10R76B off=0; 43880 CLOSED T10R76B
  off=255.
- consts _T10R76AM/AQ/AC/BM/QH/BC at lines 11956-12029:
  AM16 w8 + AQ4 w10 + AC61 + BM16 w7 + QH16 w5 + BC62.
  QH 13/16 distinct (6dd9ff8aff x4 q6-9) — matches oracle
  prefixes first-hand (A-48), non-vacuous. B q=AM-tail4+QH.

## verdict: PASS
