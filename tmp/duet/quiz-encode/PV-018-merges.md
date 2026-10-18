# PV-018: merged lanes/encode-writer2@cdee48a (partial) -> master 3185c0d

- Brings cb301db (T4G) + c45da60 (T4H) + cdee48a (T4I):
  GATE-cdee48a PASS all three + VERIFY PASS all three, no
  FLAG, wall 0 hits (rgram-only diff).
- pv worktree (removed): RGRAM-GREEN 280/280 + SMOKE-GREEN
  first-hand. merge --no-ff under merge.lock.d, no
  collisions. Never pushed.
- OUTER2 flake (a-nd-p3 283/284, pre-existing AEA nondet):
  lane re-ran GREEN + filed NOTE-FLAKE; w2 tip 9bf8951
  carries p0-treatment fix. Not merge-blocking.
- a873f7e/889144c/9bf8951 held: VERIFY-889144c PASS, sweep
  GATEs pending. Decode @ccd838d NOT merged: M-FLAGs stay
  OPEN covering tip (sweep re-spotted residuals).
