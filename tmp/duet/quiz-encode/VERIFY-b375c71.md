# VERIFY-b375c71: PASS (w2 T9O2Q 8x16+11 -> 16383)

- commit: lanes/encode-writer2 @b375c71
  (child of 20d3042; T9O2Q 8x16+11
  N=16245..16383; rgram.py +24, PINS +8
  rows; 2168 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 16245 94feb207… == pin
  g-z16245; 16383 50bd2319… == pin g-z16383.
  MATCH.
- verdict: PASS. VERIFY 56/57.
