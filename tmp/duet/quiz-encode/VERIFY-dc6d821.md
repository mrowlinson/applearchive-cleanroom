# VERIFY-dc6d821: PASS (w2 T9J1+J1Q -> 15088)

- commit: lanes/encode-writer2 @dc6d821
  (T9J1 N=14997..15024 + J1Q 4x16
  15025..15088; rgram.py +126, PINS +38
  rows; 1976 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 14997 ec2c83bd… == pin
  g-z14997; 15088 0bc6c1c5… == pin g-z15088.
  MATCH.
- verdict: PASS. VERIFY 48/48.
