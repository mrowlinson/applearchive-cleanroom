# PV-c2fdbce: parent-verify first-hand + merged b5a426c

Worktree tmp/wt-pv-c2fdbce (detached @c2fdbce, HEAD verified
c2fdbceb68ab6753b14b9fcd80eae86e634185ca), TMPDIR=NVME
pv-c2fdbce/work, marker echoed first-hand.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-c2fdbce/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1736/1736 covered=1736/1736 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3472). SMOKE-GREEN (smoke.sh).
- Wall: STAGED delta (--cached after --no-commit, rgramc.c
  only) grep 0 hits.
- Merge: b5a426c --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band27 only.
  GATE-c2fdbce PASS-functional + VERIFY-c2fdbce PASS.
