# PV-1de982e: parent-verify first-hand + merged c26589c

Worktree tmp/wt-pv-1de982e (detached @1de982e, HEAD verified
1de982e49b9946c2256527a5aebd922fe5c38e53), TMPDIR=NVME
pv-1de982e/work, marker echoed first-hand.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-1de982e/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1766/1766 covered=1766/1766 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3532). SMOKE-GREEN (smoke.sh).
- Wall: STAGED delta (--cached after --no-commit, rgramc.c
  only) grep 0 hits.
- Merge: c26589c --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band30 only.
  GATE-1de982e PASS-functional + VERIFY-1de982e PASS.
