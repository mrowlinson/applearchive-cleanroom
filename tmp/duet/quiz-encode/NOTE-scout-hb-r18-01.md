# NOTE-scout-hb-r18-01: seat taken, regression next

- r18 LIVE @142e8d4 (clean, verified tip). Identity TRUE worktree
  scope (scout-r18@local, config.worktree). TMPDIR NVME r18/
  (regr/, regr-t2/, regr-t3/). CLAIM rolled r17 -> r18.
- Round 1 poll: Q 364 / A 368 frozen (newest Q-361 w2,
  A-367 w2 geometry); zero scout Qs (encode + decode);
  PARENT newest 069; DONE unchanged (w2s9 + writer1s3);
  post-r17 traffic = other lanes' heartbeats/reaudits +
  GATE-75d39c7 (cport b186, peeked) + sweep-r11-parked
  (peeked) — no scout relevance. No wall/kickoff/donor
  traffic. CMP PARKED.
- Next: ONE fresh full regression (T0+T1+T2-SEED7+T3-SEED8),
  then hold 30 rounds sleep-60.
