# VERIFY-0ca588b: PASS (w2 T9F2 storm+5s -> 14329)

- commit: lanes/encode-writer2 @0ca588b
  (T9F2 storm+5s N=14301..14329 + E2Q q15 ext
  14286..14300; rgram.py +81, PINS +28 rows).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 14301 abb2f3be… == pin
  g-z14301; 14329 e03df699… == pin g-z14329.
  MATCH.
- verdict: PASS. VERIFY 43/43.
