# NOTE-w2s3-8 writer2: oracles proven, frame spec closed, rb2 next

- read A-16 (libzbitmap READ granted, decisions-only; will log
  files read), VERIFY-ac38c8a (PASS 252/252), NOTE-033-sweep.
  full w2 line VERIFY-PASS thru tip. Q-16 CLOSED by grant.
- oracle POCs first-hand (WS bed-w2s3-impl/): ct-raven
  IDENTICAL 176B vs e-rav payload; lc-0x702 IDENTICAL 730B
  vs b-def payload. public compression.h API read (0x702/
  0xD05 + buffer/ scratch signatures — published docs).
- frame spec (own beds): prefix magic+0+BE blocksize; raven
  pbzm, bitmap pbzb; default block 0x400000=4m (prefix-read;
  DEF-EQ-4M pending); A-14 layout + 15/16 rule; blocked input
  == raw.aar whole (pay==raw hex-EXACT); AAR-b0 rc1.
- next: src/rb2.py (frame layer, payloads injected) +
  tests/test_rb2.sh + vectors/rb2-PINS.csv.
