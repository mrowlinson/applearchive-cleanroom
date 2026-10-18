# VERIFY-a2923bc: PASS (w2 T10HEAD 16x16 -> 16736)

- commit: lanes/encode-writer2 @a2923bc
  (child of b25a422; T10HEAD 16x16 72B
  N=16481..16736; rgram.py +50/-1, PINS +16
  rows; 2224 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 16481 ddfc5a8b… == pin
  g-z16481; 16736 80bce2d1… == pin g-z16736.
  MATCH.
- verdict: PASS. VERIFY 58/59.
