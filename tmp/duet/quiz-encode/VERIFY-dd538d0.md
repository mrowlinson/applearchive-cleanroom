# VERIFY-dd538d0: PASS (w2 T9G2 16x16 -> 14648)

- commit: lanes/encode-writer2 @dd538d0
  (T9F2Q ext to 14392 + T9G2 16x16
  N=14393..14648; rgram.py +46, PINS +24
  rows; 1878 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 14392 6c866bdc… == pin
  g-z14392; 14648 9f1dd17e… == pin g-z14648.
  MATCH.
- verdict: PASS. VERIFY 45/45.
