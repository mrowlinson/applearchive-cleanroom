# VERIFY-ed2117b w2 T10R72 (n=42169..42488, +320, A+B shape): PASS

## first-hand (at-commit tree v-ed2117b)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5072 pins, 0 FAIL).
- own loop 42169..42488: 320 pass / 0 fail (fresh oracle each N).
- sha pins 26/26 MATCH in range.
- boundary: 42168 CLOSED T10P73B off=9 (prev tier); 42489
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 42169 CLOSED T10R72A off=0; 42232 CLOSED T10R72A
  off=63; 42233 CLOSED T10R72B off=0; 42488 CLOSED T10R72B
  off=255.
- consts _T10R72AM/AQ/AC/BM/BC at lines 11426-11495:
  AM16 w6 + AQ4 w9 + AC63 + BM16 w7 + BC65, all uniq,
  non-vacuous. B q=AM full (no BQ const, as committed).

## verdict: PASS
