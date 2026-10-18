# PV-5db2d64: parent-verify first-hand band131 + merged 114f60d

Worktree tmp/wt-pv-5db2d64 (detached @5db2d64), TMPDIR=NVME
pv-5db2d64/work, binary + build on NVME.
- C-BUILD: make -C src/c BUILDDIR=NVME.../pv-5db2d64/build
  rgramc rc=0, 0 warnings/errors (grepped build.log first-hand).
- RGRAMC-PYID 3387/3387 covered=3387/3387 GREEN (FULL log).
- RGRAM-GREEN C (RGRAM_BIN=C) + RGRAM-GREEN python
  (test_rgram.sh). SMOKE-GREEN (smoke.sh).
- Wall: lane.diff added-lines
  grep vendor|disasm|hopper|ghidra|dylib|/usr/lib|__TEXT|
  otool|binja|radare|ctypes|libc|ZBM_DYLIB|libcompression|
  AppleArchive = 0 hits first-hand.
- GATE-5db2d64 PASS-functional + VERIFY-5db2d64 PASS +
  no covering FLAG (FLAG-* checked, none for 5db2d64).
- Post-merge cmp lane-vs-HEAD src/c/rgramc.c IDENTICAL.

Logs: /Volumes/NVME/applearchive-cleanroom-ws/tmp/pv-5db2d64/
Verdict: PASS. Merge: --no-ff under merge.lock.d.
