# VERIFY-007375f w2 T9B2 16x16 13697..13952 PASS

- at-commit tree (git archive 007375f): test_rgram.sh
  RGRAM-GREEN (PASS g-z13952), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +46 (T9B2 16x16 tab
  b24-29 + 8B words + b30 rule; b5 eb->ec->ed),
  PINS +20 (1730 data rows; message counts 2
  csv comments per GATE-NIT).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-13952):
  len=84, sha=b3084511... == pinned g-z13952 EXACT.
- verdict: PASS. VERIFY 40/40 current.
