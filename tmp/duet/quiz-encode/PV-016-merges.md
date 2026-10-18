# PV-016: merged lanes/encode-writer2@b69560e (partial) -> master 45d5d65

- Brings f97ce83 (T4C) + b69560e (T4D): GATE-b69560e PASS
  both (covers f97ce83 same-gap) + VERIFY PASS both, no
  FLAG, wall 0 hits.
- pv worktree (removed): RGRAM-GREEN 204/204 + SMOKE-GREEN
  first-hand. merge --no-ff under merge.lock.d, no
  collisions. Never pushed.
- 60a1484/bdf1372 held: VERIFY-60a1484 PASS, sweep GATEs
  pending. Decode M-fix @9db16e2 NOT merged: viewer FLAG
  narrowed (M1-core fixed, M2 close, M3 residuals) + sweep
  FLAG narrowed to 3 residuals; fix + re-gate pending.
