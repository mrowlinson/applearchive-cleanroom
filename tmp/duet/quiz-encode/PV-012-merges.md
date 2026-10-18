# PV-012: merged lanes/encode-writer2@f858176 -> master 52818ec

- Brings 89c57df (rgram verifier+battery) + f858176 (T2
  regimes): GATE+VERIFY PASS on BOTH, no FLAG, wall-clean
  both diffs (0 hits).
- pv worktree tmp/wt-pv-w2-f858176 (removed): RGRAM-GREEN
  46/46 + SMOKE-GREEN first-hand.
- merge --no-ff under merge.lock.d; no tmp/ in diff, no
  collisions. Never pushed.
- decode side NOT merged: c929cf6 viewer FLAG narrowed but
  OPEN (M1/M2/M3 mid-chain+exactness; hsize cleared, hsbig
  refute UPHELD); 7eab5c5 VERIFY PASS but no sweep GATE yet.
