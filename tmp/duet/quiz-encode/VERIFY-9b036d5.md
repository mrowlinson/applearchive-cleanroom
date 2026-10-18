# VERIFY-9b036d5 w2 T9T1 4x16 12589..12652 PASS

- at-commit tree (git archive 9b036d5): test_rgram.sh
  RGRAM-GREEN (PASS g-z12652), smoke.sh SMOKE-GREEN.
- scope: src/rgram.py +38 (T9T1 16-row tab
  b13,14,b64-67 x4 + 8B block words b5,6,7,12,
  b60-63), PINS +16 (1508 total).
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-12652):
  len=84, sha=5d838adc... == pinned g-z12652 EXACT.
- NOTE-w2s7-82-t9t1 acked (cont 0..12652 CLOSED;
  68-tier 12653+ next; 80-tier viewer marks stand
  ready via PRE-184b..191b).
- verdict: PASS. VERIFY 32/32 current.
