# PV-017: merged lanes/encode-writer2@bdf1372 (partial) -> master bbdc98c

- Brings 60a1484 (T4E1) + bdf1372 (T4F): GATE-bdf1372
  PASS both + VERIFY PASS both, no FLAG, wall 0 hits.
- pv worktree (removed): RGRAM-GREEN 238/238 + SMOKE-GREEN
  first-hand. merge --no-ff under merge.lock.d, no
  collisions. Never pushed.
- cb301db/c45da60/cdee48a held: VERIFYs PASS, sweep GATEs
  pending. Decode @ccd838d NOT merged: VERIFY PASS-staged
  but M-FLAGs still open at tip (fix round planned, not
  landed) + no sweep GATE.
