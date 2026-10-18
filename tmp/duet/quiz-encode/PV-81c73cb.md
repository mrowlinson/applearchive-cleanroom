# PV-81c73cb: parent-verify first-hand + merged eaf3292

Worktree tmp/wt-pv-81c73cb (detached @81c73cb, HEAD verified
81c73cb35dbd77443b16d24a082cc3f7dbfe561e), TMPDIR=NVME
pv-81c73cb/work, marker echoed first-hand.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-81c73cb/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1756/1756 covered=1756/1756 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3512). SMOKE-GREEN (smoke.sh).
- Wall: STAGED delta (--cached after --no-commit, rgramc.c
  only) grep 0 hits.
- Merge: eaf3292 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band29 only.
  GATE-81c73cb PASS-functional + VERIFY-81c73cb PASS.
