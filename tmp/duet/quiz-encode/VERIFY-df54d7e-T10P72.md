# VERIFY-df54d7e w2 T10P72 (n=41793..41820, +28): PASS

## first-hand (at-commit tree ver-df54d7e)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 41793..41820: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: 41792 CLOSED T10R70B off=255 (prev tier); 41821
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 41793 CLOSED T10P720 off=0; 41806 CLOSED T10P72A
  off=11; 41820 CLOSED T10P72B off=9.
- consts _T10P72S0/S1/AM/AC/BM/BC at lines 11212-11260,
  S0/S1 + AM/AC/BM/BC shape, non-vacuous (no early-file
  C table this tier, unlike P70/P71).

## verdict: PASS
