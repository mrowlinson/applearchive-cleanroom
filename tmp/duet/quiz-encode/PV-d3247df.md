# PV-d3247df: parent-verify first-hand + merged 3267ce8

Worktree tmp/wt-pv-d3247df (detached @d3247df, HEAD verified
d3247df2162254345acc4fed6afce6bc80069850), TMPDIR=NVME
pv-d3247df/work, marker echoed first-hand.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-d3247df/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1706/1706 covered=1706/1706 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3412). SMOKE-GREEN (smoke.sh).
- Wall: STAGED delta (--cached after --no-commit, rgramc.c
  only) grep 0 hits.
- Merge: 3267ce8 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band25 only.
  GATE-d3247df PASS-functional + VERIFY-d3247df PASS.
