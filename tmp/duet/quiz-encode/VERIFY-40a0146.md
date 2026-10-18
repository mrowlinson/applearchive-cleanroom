# VERIFY-40a0146: PASS (w2 T9K1+K1Q -> 15436)

- commit: lanes/encode-writer2 @40a0146
  (T9K1 N=15345..15372 + K1Q 4x16
  15373..15436; rgram.py +116, PINS +38
  rows; 2030 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 15345 86099b48… == pin
  g-z15345; 15436 f7b4fc7a… == pin g-z15436.
  MATCH.
- verdict: PASS. VERIFY 50/50.
