# PV-8ed30d1: parent-verify first-hand band157 (VERIFY on file)

Parent-side run of WS/bin/pv-band.sh 8ed30d1 (fresh detached
worktree tmp/wt-pv-8ed30d1, TMPDIR=NVME pv-8ed30d1/work).
- C-BUILD: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings
  (build.log first-hand).
- RGRAMC-PYID 3706/3706 covered=3706/3706 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: git diff c9dd7f8..8ed30d1 added-lines PARENT-032 set
  = 0 hits first-hand.
- GATE-8ed30d1 PASS-functional + VERIFY-8ed30d1 PASS +
  no covering FLAG (FLAG-* checked, none for 8ed30d1).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-8ed30d1/
Verdict: PASS. Merge: --no-ff under merge.lock.d, oldest-first.
