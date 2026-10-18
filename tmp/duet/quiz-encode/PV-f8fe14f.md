# PV-f8fe14f: parent-verify first-hand band108 + merged 59982e5

Worktree tmp/wt-pv-f8fe14f (detached @f8fe14f), TMPDIR=NVME
pv-f8fe14f/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-f8fe14f/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3067/3067 covered=3067/3067 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (6134 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-f8fe14f PASS-functional + VERIFY-f8fe14f PASS +
  no covering FLAG (FLAG-* checked, none for f8fe14f).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-f8fe14f/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
