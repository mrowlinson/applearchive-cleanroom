# NOTE-037 viewer heartbeat4: A-17 filed (eviction found), Q/A 17/17 effective

- answered misnumbered w1s2 skip-Q as A-17 (A-13 untouched per sweep FLAG). headline: TABLE EVICTION
  found first-hand (zeros-12K CHECK vs distinct-12K SKIP decisive; 50% ≈ 8.5K inserts; hard 0 @11.5K+;
  no phase dependence; steeper-than-uniform anomaly flagged) + tail no-start zone confirmed
  (chunklen-relative ~121-128; absolute limit rejected) + metadata hash lead NONE-FOUND (thin driver,
  no cache tool) + one-pass bounded (14/14 future-independent).
- apparatus: WS scratch-viewer3/lz4probe.py (bv41/LZ4 parser + oracle driver, self-tests green).
- read: GATE-ee9e454 (PASS concurs my VERIFY ✓), NOTE-035/036-sweep (22/22, RB2 legs live, Q-collision
  FLAG obeyed), PV-006 (rb2 + sweep legs MERGED).
- next: save eviction beds (bed3.py) + fresh re-run -> CR-122 clause commit. no DONE anywhere. claim HELD.
