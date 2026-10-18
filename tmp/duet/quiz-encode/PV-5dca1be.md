# PV-5dca1be: parent-verify first-hand band111 + merged 753ca57

Worktree tmp/wt-pv-5dca1be (detached @5dca1be), TMPDIR=NVME
pv-5dca1be/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-5dca1be/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3119/3119 covered=3119/3119 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (6238 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-5dca1be PASS-functional + VERIFY-5dca1be PASS +
  no covering FLAG (FLAG-* checked, none for 5dca1be).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-5dca1be/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
