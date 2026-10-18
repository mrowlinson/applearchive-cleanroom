# VERIFY-66c84ba: PASS (w2 T9I1 16x16 -> 14996)

- commit: lanes/encode-writer2 @66c84ba
  (T9I1 16x16 N=14741..14996; rgram.py +47,
  PINS +24 rows; 1938 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 14741 cbe2f69e… == pin
  g-z14741; 14996 25c89148… == pin g-z14996.
  MATCH.
- verdict: PASS. VERIFY 47/47.
