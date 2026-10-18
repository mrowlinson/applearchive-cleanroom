# PV-f7cf078: parent-verify first-hand band121 + merged 1ec62b9

Worktree tmp/wt-pv-f7cf078 (detached @f7cf078), TMPDIR=NVME
pv-f7cf078/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-f7cf078/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3263/3263 covered=3263/3263 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-f7cf078 PASS-functional + VERIFY-f7cf078 PASS +
  no covering FLAG (FLAG-* checked, none for f7cf078).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-f7cf078/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
