# PV-022: merged lanes/encode-writer2@c4feeb2 (partial) -> master 342748e

- Brings 96688ce (T5H) + 71d5c8c (T5I0/1/2) + c4feeb2
  (T5I3): GATE-c4feeb2 PASS all three + VERIFY PASS all
  three, no FLAG, wall 0 hits.
- pv worktree (removed): RGRAM-GREEN 428/428 + SMOKE-GREEN
  first-hand. merge --no-ff under merge.lock.d, no
  collisions. Never pushed.
- 36d219f/e88a9f5 held: VERIFYs PASS, sweep GATE pending.
- Decode TIP1 @690ce94 NOT merged: viewer FLAG carried+
  narrowed (M1-507500 + M2-4cut + M3-badval-1..12) + NEW
  FLAG-690ce94-viewer (G9 C traversal WRITE, security).
  Fix + re-gate pending.
