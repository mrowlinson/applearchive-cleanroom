# PV-a0adca4: parent-verify first-hand + merged 46ffb71

Worktree tmp/wt-pv-a0adca4 (detached @a0adca4), TMPDIR=NVME
pv-a0adca4/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-a0adca4/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1530/1530 covered=1530/1530 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3060). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..a0adca4 grep 0 hits.
- Merge: 46ffb71 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band11 only.
  GATE-a0adca4 PASS-functional per PARENT-032/033 +
  VERIFY-a0adca4 PASS.
