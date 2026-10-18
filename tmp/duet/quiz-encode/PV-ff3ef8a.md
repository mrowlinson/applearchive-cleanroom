# PV-ff3ef8a: parent-verify first-hand + merged 3caa309

Worktree tmp/wt-pv-ff3ef8a (detached @ff3ef8a), TMPDIR=NVME
pv-ff3ef8a/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-ff3ef8a/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1566/1566 covered=1566/1566 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3132). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..ff3ef8a grep 0 hits.
- Merge: 3caa309 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band14 only.
  GATE-ff3ef8a PASS-functional + VERIFY-ff3ef8a PASS.
