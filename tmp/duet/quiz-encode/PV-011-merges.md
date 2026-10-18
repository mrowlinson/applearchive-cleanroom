# PV-011: merged lanes/encode-writer2@956cb83 -> master 445303b

- GATE-956cb83 PASS + VERIFY-956cb83 PASS; FLAG-q15 = quiz
  hygiene, non-blocking, other turf (does not cover merge point).
- Parent wall-grep on diff: 0 hits. pv worktree
  tmp/wt-pv-w2-956cb83 (removed post-merge): RAVFRAME-GREEN
  181/181 + SMOKE-GREEN first-hand.
- merge --no-ff under merge.lock.d (held only by this merge);
  no FF collisions (no tmp/ in diff). Never pushed.
- decode-writer @e62ee07 NOT merged: FLAG-e62ee07-viewer OPEN
  (hsize-boundary stderr divergence + C/proto mirror break;
  prescribed fix pending + re-gate).
