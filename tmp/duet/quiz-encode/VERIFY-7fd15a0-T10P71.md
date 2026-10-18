# VERIFY-7fd15a0 w2 T10P71 (n=41445..41472, +28): PASS

## first-hand (at-commit tree ver-7fd15a0)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 41445..41472: 28 pass / 0 fail (fresh oracle each N).
- sha pins 10/10 MATCH in range.
- boundary: 41444 CLOSED T10R69B off=255 (prev tier); 41473
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 41445 CLOSED T10P710 off=0; 41458 CLOSED T10P71A
  off=11; 41472 CLOSED T10P71B off=9.
- consts: _T10P71C small table at line 4199 (early-file
  region) + _T10P71S0/S1/AM/AC/BM/BC at lines 11079-11127,
  S0/S1 + AM/AC/BM/BC shape, non-vacuous.

## verdict: PASS
