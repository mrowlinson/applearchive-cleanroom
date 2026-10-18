# VERIFY-4673e2e w2 T9X1 storm+Q 13257..13348 PASS

- at-commit tree (git archive 4673e2e): test_rgram.sh
  RGRAM-GREEN (PASS g-z13348), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +121 (T9X1 storm
  13257..13285 + Q 13286..13348; tab b48,49,
  b56-59 + 11B words), PINS +38 (1618 data rows;
  message counts 2 csv comments per GATE-NIT).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-13348):
  len=84, sha=5252c2fb... == pinned g-z13348 EXACT.
- verdict: PASS. VERIFY 36/36 current.
