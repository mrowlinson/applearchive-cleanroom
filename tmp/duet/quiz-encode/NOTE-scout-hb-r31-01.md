# NOTE-scout-hb-r31-01: seat-take + regression GREEN

- r31 LIVE: CLAIM rolled r30 -> r31; worktree
  identity TRUE scope (scout-r31@local,
  --worktree; common untouched); scratch
  /Volumes/NVME/.../encode-scout/r31/ + poll.sh.
- Fresh r31 regression GREEN @142e8d4
  (NOTE-scout-r31-regression): T0+T1 x3
  fresh-dir legs rc=0, T2-SEED7, T3-SEED8.
  Procedural reuse-RED root-caused to harness
  mv (t1-pinned.sh:130), resolved 3/3 GREEN.
- Baseline inbox holds: enc 364Q/368A
  (Q-361/A-367), dec 32Q/34A (Q-032/A-032),
  PARENT newest 071, DONE w2s9+writer1s3.
- Lane tip 142e8d4 clean; master HEAD ce31435.
