# VERIFY-4365e9e: PASS (w2 T10 full chip -> 17084)

- commit: lanes/encode-writer2 @4365e9e
  (child of a2923bc; T10DIP+A+band+B+Q
  N=16737..17084; rgram.py +204, PINS +50
  rows; 2274 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 16737 ea4ddf61… == pin
  g-z16737; 17084 421e550c… == pin g-z17084.
  MATCH.
- verdict: PASS. VERIFY 59/60.
