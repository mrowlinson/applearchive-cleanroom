# PV-c12fcc6: parent-verify first-hand + merged ff02b82

Worktree tmp/wt-pv-c12fcc6 (detached @c12fcc6), TMPDIR=NVME
pv-c12fcc6/work, binary + build on NVME.
- C-BUILD: make -C src/c rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 855/855 covered=855/1411 GREEN.
- RGRAM-GREEN (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: diff ee8a9b5..c12fcc6 (rgramc.c +15869/-3272 regen)
  grep 0 hits.
- Merge: ff02b82 --no-ff under merge.lock.d, clean.
  GATE-c12fcc6 functional PASS + VERIFY-c12fcc6 PASS +
  PARENT-032 ruling. Note: msg top "T9B2" actually T9A2Q
  (n<=13696); tiers 169 not 165 (writer self-corrected).
