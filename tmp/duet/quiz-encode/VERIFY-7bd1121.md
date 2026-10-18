# VERIFY-7bd1121 w2 T9D4 dip band 12579..12588 PASS

- at-commit tree (git archive 7bd1121): test_rgram.sh
  RGRAM-GREEN (PASS g-z12588; list += 12579, 12588).
- scope: src/rgram.py +31 (T9D4 10-row tab
  b5-9,b60-63, paylen 64, lencode rule), PINS +4.
- independent corroboration (first-hand vendor
  compression_tool -encode -a lzraven, zeros-12588):
  len=80, sha=a503f6a8...57014 == pinned g-z12588
  sha EXACT. (raw-framing b4 read differs from
  parsed-pay check; battery GREEN governs.)
- verdict: PASS. VERIFY 31/31 current.
