# VERIFY-3ef1563: PASS (w2 T9M1Q 16x16 -> 16040)

- commit: lanes/encode-writer2 @3ef1563
  (child of 48ebfe0; T9M1Q 16x16
  N=15785..16040; rgram.py +44, PINS +20
  rows; 2110 pins).
- at-commit tree: RGRAM-GREEN + SMOKE-GREEN.
- independent vendor sha (compression_tool,
  fresh zeros-N): 15785 3acc4ce7… == pin
  g-z15785; 16040 ac2e558d… == pin g-z16040.
  MATCH.
- FLAG persists: 15752 still out of GCELL
  loop (15743 in its place); regression pin
  recommended (vendor sha bed9ad92… on
  record in VERIFY-48ebfe0).
- verdict: PASS. VERIFY 53/54.
