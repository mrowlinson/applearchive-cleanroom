# PV-015: merged lanes/encode-writer2@f08fc79 (partial) -> master 639945c

- Brings 6fa9921 (T4B4) + f08fc79 (unified T4B): GATE
  PASS-both + VERIFY PASS both, no FLAG, wall 0 hits.
- pv worktree (removed): RGRAM-GREEN 160/160 + SMOKE-GREEN
  first-hand. merge --no-ff under merge.lock.d, no
  collisions. Never pushed.
- Tip f97ce83 (T4C) held: VERIFY PASS, sweep GATE pending.
- decode M-fix @9db16e2 wall: 2 hits, both benign with
  context (commit-msg self-note + A-006 ZBM_DYLIB one-line).
  Awaits GATE/VERIFY.
