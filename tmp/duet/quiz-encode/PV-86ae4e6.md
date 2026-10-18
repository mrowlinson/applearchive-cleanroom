# PV-86ae4e6: parent-verify first-hand band167 (VERIFY on file)

Parent-side run of WS/bin/pv-band.sh 86ae4e6 (fresh detached
worktree tmp/wt-pv-86ae4e6, TMPDIR=NVME pv-86ae4e6/work).
- C-BUILD: cc -O2 -Wall -Wextra -std=c11 rc=0, 0 warnings
  (build.log first-hand).
- RGRAMC-PYID 3831/3831 covered=3831/3831 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- GATE-86ae4e6 PASS-functional + VERIFY-86ae4e6 PASS on
  file (viewer3 r1, PYID match). Wall 3504728..86ae4e6 =
  0 hits first-hand; no covering FLAG (FLAG-* checked).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-86ae4e6/
Verdict: PASS. Merge: --no-ff under merge.lock.d, oldest-first.
