# VERIFY-c418002: PASS (AEA pad/cks matrix, additive, honest)

- scope first-hand: tests +18 (PC 5x3 + RT + pad15 rc/msg), pins +18 rows. additive.
- code: PC direct-aea size pins; RT real cmp; pad15 rc+msg-first-line real. corroborates
  NOTE-w2s3-4 EXACT per GATE-c81821f (cks +2048/+8192 fixed; quantize-UP; pad15 rc1).
- wall: 0 hits (own grep). covered-within GATE-c81821f PASS; no FLAG.
