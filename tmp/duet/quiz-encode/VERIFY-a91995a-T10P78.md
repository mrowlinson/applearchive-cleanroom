# VERIFY-a91995a w2 T10P78 (n=43881..43908, +28): PASS

## first-hand (at-commit tree v-a91995a)
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5276 pins, 0 FAIL).
- own loop 43881..43908: 28 pass / 0 fail (fresh oracle each N).
- sha pins 20/20 MATCH in range.
- boundary: 43880 CLOSED T10R76B off=255 (prev tier); 43909
  N out of scope rc=2 (next zone unwritten) — correct.
- labels: 43881 CLOSED T10P780 off=0; 43883 CLOSED T10P78A
  off=0; 43898 CLOSED T10P78A off=15; 43899 CLOSED T10P78B
  off=0; 43908 CLOSED T10P78B off=9.
- consts _T10P78S0/S1/AM/AC/BM/BC at lines 12030-12090:
  S0/S1 80B + AM16 w6 + AC73 + BM10 w18 interleaved-sig
  + BC60, all uniq, non-vacuous.

## verdict: PASS
