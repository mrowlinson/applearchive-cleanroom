# PV-4ad7a4d: parent-verify first-hand + merged 4bcefa6

Worktree tmp/wt-pv-4ad7a4d (detached @4ad7a4d), TMPDIR=NVME
pv-4ad7a4d/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-4ad7a4d/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1592/1592 covered=1592/1592 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3184). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..4ad7a4d grep 0 hits.
- Merge: 4bcefa6 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band16 only.
  GATE-4ad7a4d PASS-functional + VERIFY-4ad7a4d PASS.
