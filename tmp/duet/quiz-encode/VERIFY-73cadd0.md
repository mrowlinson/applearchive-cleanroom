# VERIFY-73cadd0 w2 T9V1 storm+Q 12909..13000 PASS

- at-commit tree (git archive 73cadd0): test_rgram.sh
  RGRAM-GREEN (PASS g-z13000), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +117 (T9V1 storm
  12909..12937 + Q 12938..13000; tab b32-37 +
  8B words k15 early-edge), PINS +34 (1562).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-13000):
  len=84, sha=07a21157... == pinned g-z13000 EXACT.
- verdict: PASS. VERIFY 34/34 current.
