# VERIFY-aeefa70 w2 T9C2 storm+Q 13953..14029 PASS

- at-commit tree (git archive aeefa70): test_rgram.sh
  RGRAM-GREEN (PASS g-z14029), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +116 (T9C2 storm
  13953..13981 + Q 13982..14029; tab b40-45 +
  8B words, b34/b23/b24 edges), PINS +38 (1768
  data rows; message counts 2 csv comments per
  GATE-NIT).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-14029):
  len=84, sha=f04c7b5c... == pinned g-z14029 EXACT.
- verdict: PASS. VERIFY 41/41 current.
