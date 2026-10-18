# VERIFY-14a3807 w2 T9Z1 11x16 13429..13604 PASS

- at-commit tree (git archive 14a3807): test_rgram.sh
  RGRAM-GREEN (PASS g-z13604), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +47 (T9Z1 11x16 tab
  b6,b60-63 + 6B words + b5 HI[m]/LO[q] m11-edge),
  PINS +30 (1668 data rows; message counts 2
  csv comments per GATE-NIT).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-13604):
  len=84, sha=6ede35e6... == pinned g-z13604 EXACT.
- verdict: PASS. VERIFY 38/38 current.
