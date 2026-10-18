# PV-a99d06a: parent-verify first-hand + merged 4c2e04d

Worktree tmp/wt-pv-a99d06a (detached @a99d06a), TMPDIR=NVME
pv-a99d06a/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-a99d06a/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1520/1520 covered=1520/1520 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3040). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..a99d06a grep 0 hits.
- Merge: 4c2e04d --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band10 only.
  GATE-a99d06a functional PASS + VERIFY-a99d06a PASS +
  PARENT-032 ruling.
