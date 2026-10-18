# PV-027: merged lanes/encode-writer2@818ac6c (partial) -> master f9a0a39

- Brings 8819771 (T7B) + 818ac6c (T7C): GATE-818ac6c PASS
  both + VERIFY PASS both, no FLAG, wall 0 hits.
- pv worktree (removed): RGRAM-GREEN 726/726 + SMOKE-GREEN
  first-hand. merge --no-ff under merge.lock.d, no
  collisions. Never pushed.
- 7f80ec2/cb0aaee held: VERIFY-7f80ec2 PASS, sweep GATEs
  pending. w1 @4d61e87 (P1 mod5): VERIFY PASS, GATE
  pending — lane still RED-ancestor-blocked regardless.
- Decode TIP2a/TIP2b held: sweep GREEN on TIP2a, viewer
  VERIFYs pending both.
