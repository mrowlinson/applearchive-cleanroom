# PV-ee8a9b5: parent-verify first-hand + merged f701f2c

Worktree tmp/wt-pv-ee8a9b5 (detached @ee8a9b5), TMPDIR=NVME
pv-ee8a9b5/work, binary + build on NVME.
- C-BUILD: make -C src/c rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 341/341 covered=341/1411 GREEN.
- RGRAM-GREEN (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: diff 0f57814..ee8a9b5 (rgramc.c +5617 single file)
  grep 0 hits.
- Merge: f701f2c --no-ff under merge.lock.d, clean.
  GATE-ee8a9b5 functional PASS + VERIFY-ee8a9b5 PASS +
  PARENT-032 ruling. Note: commit msg says T3..T7D3 but top
  tier = T6M3-6 (n<=6040); sweep observation, no impact.
