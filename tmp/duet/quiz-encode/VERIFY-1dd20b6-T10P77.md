# VERIFY-1dd20b6 w2 T10P77 (n=43533..43560, +28): PASS

## first-hand (at-commit tree v-1dd20b6)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5230 pins, 0 FAIL).
- own loop 43533..43560: 28 pass / 0 fail (fresh oracle each N).
- sha pins 20/20 MATCH in range.
- boundary: 43532 CLOSED T10R75B off=255 (prev tier); 43561
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 43533 CLOSED T10P770 off=0; 43535 CLOSED T10P77A
  off=0; 43550 CLOSED T10P77A off=15; 43551 CLOSED T10P77B
  off=0; 43560 CLOSED T10P77B off=9.
- consts _T10P77S0/S1/AM/AC/BM/BC at lines 11894-11955:
  S0/S1 80B + AM16 w8 + AC71 + BM10 w16 split-sig + BC63,
  all uniq, non-vacuous.

## verdict: PASS
