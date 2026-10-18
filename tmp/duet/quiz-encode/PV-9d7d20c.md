# PV-9d7d20c: parent-verify first-hand + merged 30d5f98

Worktree tmp/wt-pv-9d7d20c (detached @9d7d20c), TMPDIR=NVME
pv-9d7d20c/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-9d7d20c/build
  rgramc rc=0, 0 warnings/errors. Makefile fix (ee40fd9) in
  history: BUILDDIR now respected, binary lands in NVME dir.
- RGRAMC-PYID 1494/1494 covered=1494/1494 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 2988). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..9d7d20c grep 0 hits.
- Merge: 30d5f98 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band7 only.
  GATE-9d7d20c functional PASS + VERIFY-9d7d20c PASS +
  PARENT-032 ruling.
