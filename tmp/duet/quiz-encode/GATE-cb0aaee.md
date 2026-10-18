# GATE-cb0aaee sweep: PASS (rgram 762/762, T7D/E; covers 7f80ec2)

- tip: lanes/encode-writer2 @cb0aaee (chain 818ac6c->7f80ec2(T7D)->cb0aaee(T7E)).
  src +172/-0 rgram.py, pure append.
- coverage: 65/65 writer tips gated (64 battery-PASS + 1 RED-held w1 lzma).
- code read: T7D solo dip6645 + D0/D1-15/D2S/D2-9 + D3 4x16 shared tab b48-51;
  T7E 14x16 walk D3T[0..13] b48-51 + tab b55-59 + b5 @743/871. ordering verified.
- battery: GATE-PASS, HYGIENE no-artifacts, CONTAM 0-hits, RGRAM n=762,
  PINS-RGRAM set-eq 762/762, OSS none (outdir gate-w2-cb0aaee-s2).
- pins: 726->762, +36 append-only (26 D + 10 E).
- viewer: VERIFY-7f80ec2 PASS concur (752/752). E VERIFY pending.
