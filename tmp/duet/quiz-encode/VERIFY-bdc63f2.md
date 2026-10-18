# VERIFY-bdc63f2 w2 T9E2 15-row+single+Q 14030..14285 PASS

- at-commit tree (git archive bdc63f2): test_rgram.sh
  RGRAM-GREEN (PASS g-z14285), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +89 (T9E2 15-row 14030..14044
  + single + Q 15x16 14046..14285; tab
  b40-43,47,52,53 + 8B words), PINS +40 (1808
  data rows; message counts 2 csv comments per
  GATE-NIT).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-14285):
  len=84, sha=731f9e1d... == pinned g-z14285 EXACT.
- verdict: PASS. VERIFY 42/42 current.
