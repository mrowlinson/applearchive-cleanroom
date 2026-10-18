# PV-fecaa3d: parent-verify first-hand band94 + merged 00b11f0

Worktree tmp/wt-pv-fecaa3d (detached @fecaa3d), TMPDIR=NVME
pv-fecaa3d/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-fecaa3d/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 2766/2766 covered=2766/2766 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (5532 pins, test_rgram.sh). SMOKE-GREEN (smoke.sh 6/6).
- Wall: lane.diff (rgramc.c only, +1280/-718) added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-fecaa3d PASS-functional + VERIFY-fecaa3d PASS +
  no covering FLAG (FLAG-* checked, none for fecaa3d).

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-fecaa3d/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
