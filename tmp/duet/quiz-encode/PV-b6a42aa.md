# PV-b6a42aa: parent-verify first-hand + merged f4b6018

Worktree tmp/wt-pv-b6a42aa (detached @b6a42aa), TMPDIR=NVME
pv-b6a42aa/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-b6a42aa/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1502/1502 covered=1502/1502 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3004). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..b6a42aa grep 0 hits.
- Merge: f4b6018 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band8 only.
  GATE-b6a42aa functional PASS + VERIFY-b6a42aa PASS +
  PARENT-032 ruling.
