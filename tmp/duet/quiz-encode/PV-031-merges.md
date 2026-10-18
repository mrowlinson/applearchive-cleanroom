# PV-031: merged lanes/encode-writer2@bb84ec7 (partial) -> master f258bef

- Brings e514e4b (T7M) + bb84ec7 (T7RB): GATE-bb84ec7 PASS
  both + VERIFY PASS both, no FLAG, wall 0 hits.
- pv worktree (removed): RGRAM-GREEN 902/902 + SMOKE-GREEN
  first-hand. merge --no-ff under merge.lock.d, no
  collisions. Never pushed.
- bbfd87c (T7N) held: no GATE/VERIFY yet. Decode TIP2c
  @462e86f NOT merged: sweep GREEN but NEW viewer
  FLAG-462e86f (single-block over-fire) + carried
  e62ee07 items. Fix + re-gate pending.
