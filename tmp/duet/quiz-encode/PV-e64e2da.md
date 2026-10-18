# PV-e64e2da: parent-verify first-hand + merged 88e786e

Worktree tmp/wt-pv-e64e2da (detached @e64e2da), TMPDIR=NVME
pv-e64e2da/work, binary + build on NVME.
- C-BUILD: make -C src/c rgramc rc=0, 0 warnings/errors.
- RGRAMC-PYID 1484/1484 covered=1484/1484 GREEN (FULL).
- RGRAM-GREEN (test_rgram.sh, 2968). SMOKE-GREEN (smoke.sh).
- Wall: merge-base..e64e2da grep 0 hits.
- Merge: 88e786e --no-ff --no-commit under merge.lock.d, then
  master README restored pre-commit (lane carries stale 10-07
  README via partial master-merges; CORRECTION-5 lesson applied
  inline). Net delta: rgramc.c band6 only.
  GATE-e64e2da functional PASS + VERIFY-e64e2da PASS +
  PARENT-032 ruling.
