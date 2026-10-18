# VERIFY-9a43b95 w2 T9Y1 5x16 13349..13428 PASS

- at-commit tree (git archive 9a43b95): test_rgram.sh
  RGRAM-GREEN (PASS g-z13428), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +38 (T9Y1 5x16 tab
  b5,6,b60-63 + 6B words b48,49,b56-59),
  PINS +20 (1638 data rows; message counts 2
  csv comments per GATE-NIT).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-13428):
  len=84, sha=10886b66... == pinned g-z13428 EXACT.
- verdict: PASS. VERIFY 37/37 current.
