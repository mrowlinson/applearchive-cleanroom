# NOTE-scout-hb-r35-01: r35 boot, PROD-01 answered

- CLAIM rolled r34 -> r35 (identity r35
  TRUE worktree scope, WT clean @142e8d4,
  TMPDIR NVME r35/).
- Poll R1: enc 364Q/368A (Q-361/A-367, frozen
  vs r34), dec 32Q/34A, DONE unchanged
  (w2s9+writer1s3 enc, 7 dec). Zero scout Qs.
- PARENTs read: 072 resume, 073 queued-not-stuck,
  074 exit-at-cap, 067..071, 032 wall (binds),
  PROD-01 (this prod) + PROD-02..04 cport-only.
  No wall/kickoff/donor traffic. CMP parked.
- Next: fresh r35 regression (T0+T1x3+T2+T3),
  then sleep-30 polls to 30-round cap.
