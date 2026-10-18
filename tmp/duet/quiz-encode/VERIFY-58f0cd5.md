# VERIFY-58f0cd5 w2 T9W1 16x16 13001..13256 PASS

- at-commit tree (git archive 58f0cd5): test_rgram.sh
  RGRAM-GREEN (PASS g-z13256), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +42 (T9W1 16x16 tab
  b40-45 + 6B words b32-37; b5 65->66->67),
  PINS +20 (1582 total).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-13256):
  len=84, sha=bbd2d94c... == pinned g-z13256 EXACT.
- verdict: PASS. VERIFY 35/35 current.
