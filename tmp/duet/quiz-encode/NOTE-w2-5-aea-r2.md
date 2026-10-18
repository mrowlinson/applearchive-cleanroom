# NOTE-w2-5 writer2: adapter loopback-green, AEA r1+r2 (55 cells)

- RACE entry FILED: harness/impl2-adapter.sh (pure router, per-command
  $IMPL2_* override, oracle loopback default, probe declares routing).
  BACKEND=impl2 smoke: SMOKE-GREEN 6/6 first-hand. unknown-cmd exit 2.
  honestly loopback; parent picks vs writer1 impl-backed entry.
- AEA r1 (33 cells): header AEA1+profileLE+0s+random@12 CONFIRMED (own);
  size map MATCHES PRE-001 all 5 pts (0->160 ... 5000->24576); zeros==random
  sizes (content-independent); p1==p5 sizes; pad/cks deltas MATCH (-956,
  -8704, adaptive==dflt, sha256==dflt); roundtrips 3/3 RT-OK; id 64-hex.
- AEA r2 (22 cells): rep-diff char 13 EXACT (both profiles); alg x zeros
  all 19456 (compress-then-encrypt; min data envelope); id RE-RUN-DIFFERS
  (same plaintext -> different id => ciphertext-derived, not plaintext);
  -b 4k/64k/1m no-op at 5KB; 16384->36864 MATCH; 100000->118784 NEW;
  p0-bare rc=1 needs -sign-priv/-pub (EC round next).
- read: PARENT-002 (COMPLYING: no pyc in lane; gitignore next commit),
  PARENT-003 (no OSS deps in lane; nomination-before-add noted),
  PRE-001 (all confirmed independently), NOTE-7 (turf ack: AEA+matrix
  ceded to w2; writer1 keeps other-alg IMPL incl raven/bitmap — writer2
  runs BLACK-BOX alg beds only, no impl files there), Q-9 (a: flips now
  writer1-asked; w2 will read A-9, no dup).
- gap: g-aea r3 NEXT (id-flip, size sweep, EC profiles, key forms,
  murmur64, big -b, pw floor); g-adapter FILED (green-loopback);
  g-pins (outer2-PINS.csv + test_outer2.sh) after AEA beds settle.
