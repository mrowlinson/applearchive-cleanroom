# NOTE-46 writer1s3 (FULL census committed 9895a19, baseline 36/24)

- COMMIT 9895a19: tests/test_lz4_full.sh (census, exit 0,
  non-gating; seedoff 0/1000/2000 = FULL/holdout/fresh).
- BASELINE: 36/24 on all three (identical BADLIST:
  const/periodic/runs >=1K + mix1m; random/text/small pass).
  finding frontier quantified on real shapes.
- LANE STATE: tip 9895a19. commits this shift: 30ce9d8
  (handoff) 4d61e87 (mod5) 7f80ea0 (rescan) 906081f (b0)
  9895a19 (census). gates: PASS thru 7f80ea0 (+HOLD m4m,
  now fixed, re-gate pending).
- OPEN: Q-32 (hash triplets) w/ viewer; P1/EXT parked
  pending true hash; C lz4 port (after finding converges).
