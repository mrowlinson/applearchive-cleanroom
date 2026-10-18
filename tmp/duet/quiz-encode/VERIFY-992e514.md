# VERIFY-992e514: FAIL (w2 T9L1+L1Q, 1 cell RED)

- commit: lanes/encode-writer2 @992e514
  (T9L1 N=15693..15720 + L1Q 4x16
  15721..15784; 2090 pins).
- at-commit tree: RGRAM-RED (SMOKE-GREEN).
- single FAIL: `FAIL g15752 rgram:` —
  rgram.py exits `GRAMMAR-BREAK T9L1Q blk`
  rc=1 on N=15752 (L1Q off=31, m=15, q=1).
  reproduced direct; neighbors 15737/15753
  rc=0.
- verdict: FAIL. VERIFY 51/52 (48 PASS
  chain unbroken thru bed1c8b).
- recon: PRE-516b (derived vendor bytes +
  divergence point).
