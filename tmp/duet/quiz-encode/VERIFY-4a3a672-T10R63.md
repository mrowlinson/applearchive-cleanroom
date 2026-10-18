# VERIFY-4a3a672 w2 T10R63 (n=39037..39356, +320, A+B shape): PASS

## first-hand (at-commit tree ver-4a3a672)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- own loop 39037..39356: 320 pass / 0 fail (fresh oracle each N).
- sha pins 13/13 MATCH in range.
- boundary: 39036 CLOSED T10P64B off=9 (prev tier); 39357
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 39037 CLOSED T10R63A off=0; 39100 CLOSED T10R63A
  off=63; 39200 CLOSED T10R63B off=99; 39356 CLOSED
  T10R63B off=255. A+B 320-wide shape; QH present.
- consts _T10R63AM/AQ/AC/BM/QH/BC at lines 10134-10191,
  non-vacuous.

## verdict: PASS
