# PV-64b7f1a: parent-verify first-hand + merged 79e2871

Worktree tmp/wt-pv-64b7f1a (detached @64b7f1a), TMPDIR=NVME
pv-64b7f1a/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-64b7f1a/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1602/1602 covered=1602/1602 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3204). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..64b7f1a grep 0 hits.
- Merge: 79e2871 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band17 only.
  GATE-64b7f1a PASS-functional + VERIFY-64b7f1a PASS.
