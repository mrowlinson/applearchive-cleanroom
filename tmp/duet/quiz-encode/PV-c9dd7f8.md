# PV-c9dd7f8: parent-verify first-hand band155 (VERIFY on file)

Worktree tmp/wt-pv-c9dd7f8 (detached @c9dd7f8), TMPDIR=NVME
pv-c9dd7f8/work, binary + build on NVME.
- C-BUILD: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings
  (build.log first-hand).
- RGRAMC-PYID 3681/3681 covered=3681/3681 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: git diff 91763c1..c9dd7f8 added-lines PARENT-032 set
  = 0 hits first-hand.
- GATE-c9dd7f8 PASS-functional + VERIFY-c9dd7f8 PASS +
  no covering FLAG (FLAG-* checked, none for c9dd7f8).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-c9dd7f8/
Verdict: PASS. Merge: --no-ff under merge.lock.d, oldest-first.
