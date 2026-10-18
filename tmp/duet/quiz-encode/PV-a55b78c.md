# PV-a55b78c: parent-verify first-hand + merged 9e1e188

Worktree tmp/wt-pv-a55b78c (detached @a55b78c), TMPDIR=NVME
pv-a55b78c/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-a55b78c/build
  rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1628/1628 covered=1628/1628 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 3256). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..a55b78c grep 0 hits.
- Merge: 9e1e188 --no-ff --no-commit under merge.lock.d,
  master README kept. Net delta: rgramc.c band19 only.
  GATE-a55b78c PASS-functional + VERIFY-a55b78c PASS.
- NOTE: first rgram+smoke run's tool result arrived mismatched
  (showed a different command/output than sent); discarded as
  untrusted, re-ran with marker first-hand — GREEN confirmed.
