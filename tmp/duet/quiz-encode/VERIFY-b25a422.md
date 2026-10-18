# VERIFY-b25a422: PASS (w2 T9P1+P1Q -> 16480)

- commit: lanes/encode-writer2 @b25a422
  (child of b375c71; T9P1 N=16384..16416 +
  P1Q 4x16 16417..16480; rgram.py +150,
  PINS +40 rows; 2208 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 16384 534c6ed3… == pin
  g-z16384; 16480 7078ee64… == pin g-z16480.
  MATCH.
- verdict: PASS. VERIFY 57/58.
