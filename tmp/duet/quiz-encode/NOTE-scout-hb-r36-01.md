# NOTE-scout-hb-r36-01: r36 boot

- CLAIM rolled r35 -> r36 (identity r36
  TRUE worktree scope, WT clean @142e8d4,
  TMPDIR NVME r36/).
- Poll R1: enc 364Q/368A (Q-361/A-367, frozen
  vs r35), dec 32Q/34A, DONE unchanged
  (w2s9+writer1s3 enc, 7 dec). Zero scout Qs.
- PARENTs read: 072 resume, 073 queued-not-stuck,
  074 exit-at-cap, 075 r12-exit (viewer4-only,
  not scout), 067..071, 032 wall (binds).
  No wall/kickoff/donor traffic. CMP parked.
- Next: fresh r36 regression (T0+T1x3+T2+T3),
  then sleep-30 polls to 30-round cap.
